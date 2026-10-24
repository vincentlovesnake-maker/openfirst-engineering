import ast
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillIntegrityTests(unittest.TestCase):
    def test_skill_markdown_links_exist(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        links = re.findall(r"\[[^]]+\]\(([^)]+)\)", text)
        self.assertGreaterEqual(len(links), 10)
        for link in links:
            self.assertTrue((ROOT / link).exists(), link)

    def test_scripts_do_not_import_network_clients(self):
        banned = {"requests", "urllib", "httpx", "aiohttp", "socket", "ftplib", "paramiko"}
        for path in (ROOT / "scripts").glob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8-sig"))
            imports = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split(".")[0])
            self.assertFalse(imports & banned, f"{path.name}: {imports & banned}")

    def test_open_source_gate_has_all_decisions_and_unavailable_state(self):
        text = (ROOT / "references" / "open-source-first.md").read_text(encoding="utf-8-sig")
        for decision in (
            "KEEP", "REUSE_NATIVE", "INTEGRATE", "IMPROVE",
            "REPLACE", "MINIMAL_BUILD", "DEFER", "REJECT",
            "SEARCH_UNAVAILABLE",
        ):
            self.assertIn(decision, text)


if __name__ == "__main__":
    unittest.main()
