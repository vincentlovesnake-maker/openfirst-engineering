#!/usr/bin/env python3
"""Read-only project metadata inventory for OpenFirst Engineering."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

EXCLUDED_DIRS = {
    ".git", "node_modules", "vendor", ".venv", "venv", "__pycache__",
    ".cache", "dist", "build", "coverage", "browser-profile", "profiles",
}
SENSITIVE_NAMES = {
    ".env", ".env.local", ".env.production", "id_rsa", "id_ed25519",
    "credentials.json", "secrets.json", "auth.json", "cookies",
}
MANIFEST_NAMES = {
    "package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
    "composer.json", "composer.lock", "pyproject.toml", "requirements.txt",
    "poetry.lock", "go.mod", "go.sum", "cargo.toml", "cargo.lock",
    "gemfile", "gemfile.lock", "dockerfile", "compose.yaml",
    "docker-compose.yml", "license", "license.md", "notice",
}


def run_git(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=False,
            capture_output=True,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def is_sensitive(path: Path) -> bool:
    name = path.name.lower()
    if name in SENSITIVE_NAMES or name.startswith(".env."):
        return True
    return any(token in name for token in ("secret", "credential", "private_key"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(root: Path, hash_manifests: bool) -> dict:
    root = root.resolve(strict=True)
    counts: Counter[str] = Counter()
    manifests: list[dict] = []
    categories: dict[str, list[str]] = {
        "tests": [], "migrations": [], "deployment": [], "ci": [], "docs": []
    }
    total_bytes = 0
    file_count = 0
    omitted_sensitive = 0
    omitted_dirs: Counter[str] = Counter()

    for current, dirs, files in os.walk(root, topdown=True):
        kept = []
        for directory in dirs:
            if directory.lower() in EXCLUDED_DIRS:
                omitted_dirs[directory.lower()] += 1
            else:
                kept.append(directory)
        dirs[:] = kept

        current_path = Path(current)
        for filename in files:
            path = current_path / filename
            rel = path.relative_to(root).as_posix()
            if is_sensitive(path):
                omitted_sensitive += 1
                continue
            try:
                stat = path.stat()
            except OSError:
                continue
            file_count += 1
            total_bytes += stat.st_size
            suffix = path.suffix.lower() or "<none>"
            counts[suffix] += 1
            lower = rel.lower()

            manifest_match = filename.lower() in MANIFEST_NAMES
            if manifest_match:
                item = {"path": rel, "size": stat.st_size}
                if hash_manifests:
                    try:
                        item["sha256"] = sha256(path)
                    except OSError:
                        item["sha256"] = None
                manifests.append(item)

            if "/test" in f"/{lower}" or lower.startswith("tests/"):
                categories["tests"].append(rel)
            if "migration" in lower:
                categories["migrations"].append(rel)
            if any(token in lower for token in ("docker", "deploy", "helm", "terraform")):
                categories["deployment"].append(rel)
            if lower.startswith(".github/workflows/") or lower.startswith(".gitlab-ci"):
                categories["ci"].append(rel)
            if lower.startswith("docs/") or filename.lower().startswith("readme"):
                categories["docs"].append(rel)

    head = run_git(root, "rev-parse", "HEAD")
    branch = run_git(root, "branch", "--show-current")
    status = run_git(root, "status", "--porcelain=v1", "--branch")

    return {
        "schema": "ofe.inventory.v1",
        "root": str(root),
        "interpretation_warning": "File presence is not functional completion.",
        "git": {
            "is_repository": head is not None,
            "head": head,
            "branch": branch,
            "status": status.splitlines() if status else [],
        },
        "files": {
            "count": file_count,
            "bytes": total_bytes,
            "extensions": dict(counts.most_common()),
            "sensitive_files_omitted": omitted_sensitive,
            "excluded_directories": dict(omitted_dirs),
        },
        "manifests": sorted(manifests, key=lambda item: item["path"]),
        "indexes": {
            key: sorted(values)[:500] for key, values in categories.items()
        },
        "truncation": {
            key: max(0, len(values) - 500) for key, values in categories.items()
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Explicit project root")
    parser.add_argument("--output", help="Optional JSON output path; stdout otherwise")
    parser.add_argument("--hash-manifests", action="store_true")
    args = parser.parse_args()

    try:
        result = inventory(Path(args.root), args.hash_manifests)
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
