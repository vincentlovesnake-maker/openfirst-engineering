#!/usr/bin/env python3
"""Validate OFE finding records without judging whether conclusions are true."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

STATUSES = {
    "CONFIRMED", "RISK", "UNVERIFIED", "PASSED", "NOT_IMPLEMENTED",
    "OUT_OF_SCOPE", "RESOLVED", "DISPUTED",
}
LEVELS = {"E0", "E1", "E2", "E3", "E4", "E5"}
REQUIRED = {
    "id", "module", "finder_role", "status", "severity", "confidence",
    "baseline", "method", "evidence_level", "evidence_location",
    "fact", "inference", "unknowns", "recommendation", "retest",
}
VISUAL_TYPES = {
    "VISUAL", "LAYOUT", "INTERACTION", "ACCESSIBILITY", "RESPONSIVE",
    "BUSINESS_FLOW", "DATA_BINDING", "DEPLOYMENT_ASSET", "UNKNOWN",
}
VISUAL_REQUIRED = {
    "project_version", "route", "user_role", "viewport", "browser",
    "design_reference", "screenshot", "reproduction_steps", "expected",
    "actual", "finding_type", "root_cause_evidence", "change_scope",
    "regression_acceptance",
}


def validate_findings(data: object, root: Path | None = None) -> list[str]:
    findings = data.get("findings") if isinstance(data, dict) else data
    if not isinstance(findings, list):
        return ["Input must be a list or an object with a findings list."]

    errors: list[str] = []
    seen: set[str] = set()
    for index, finding in enumerate(findings):
        prefix = f"findings[{index}]"
        if not isinstance(finding, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        missing = sorted(REQUIRED - set(finding))
        if missing:
            errors.append(f"{prefix}: missing {'', ''.join(missing)}")
        fid = finding.get("id")
        if not isinstance(fid, str) or not fid.strip():
            errors.append(f"{prefix}.id: must be non-empty")
        elif fid in seen:
            errors.append(f"{prefix}.id: duplicate {fid}")
        else:
            seen.add(fid)
        if finding.get("status") not in STATUSES:
            errors.append(f"{prefix}.status: invalid")
        if finding.get("evidence_level") not in LEVELS:
            errors.append(f"{prefix}.evidence_level: invalid")
        if finding.get("status") == "PASSED":
            if finding.get("evidence_level") in {"E0", "E1"}:
                errors.append(f"{prefix}: PASSED requires E2 or stronger relevant evidence")
            if not finding.get("method") or not finding.get("retest"):
                errors.append(f"{prefix}: PASSED requires method and retest")
        if finding.get("status") == "CONFIRMED" and not finding.get("fact"):
            errors.append(f"{prefix}: CONFIRMED requires a verified fact")
        if finding.get("status") == "RESOLVED" and not finding.get("retest_result"):
            errors.append(f"{prefix}: RESOLVED requires retest_result")
        if "finding_type" in finding:
            if finding.get("finding_type") not in VISUAL_TYPES:
                errors.append(f"{prefix}.finding_type: invalid")
            missing_visual = sorted(VISUAL_REQUIRED - set(finding))
            if missing_visual:
                errors.append(f"{prefix}: visual finding missing {', '.join(missing_visual)}")
            for field in VISUAL_REQUIRED - {"finding_type"}:
                if field in finding and not isinstance(finding[field], (str, list, dict)):
                    errors.append(f"{prefix}.{field}: must be traceable text or structured evidence")
                elif field in finding and not finding[field]:
                    errors.append(f"{prefix}.{field}: must be non-empty")
        if root and isinstance(finding.get("evidence_location"), str):
            location = finding["evidence_location"]
            if location.startswith("file:"):
                candidate = (root / location[5:].split("#", 1)[0]).resolve()
                try:
                    candidate.relative_to(root.resolve())
                except ValueError:
                    errors.append(f"{prefix}.evidence_location: escapes root")
                else:
                    if not candidate.exists():
                        errors.append(f"{prefix}.evidence_location: file not found")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON finding file")
    parser.add_argument("--root", help="Optional project root for file evidence")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    errors = validate_findings(data, Path(args.root) if args.root else None)
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
