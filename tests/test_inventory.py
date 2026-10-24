import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from inventory import inventory


class InventoryTests(unittest.TestCase):
    def test_inventory_is_read_only_and_omits_secret_content(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "package.json").write_text('{"name":"sample"}', encoding="utf-8")
            (root / ".env").write_text("API_KEY=do-not-read", encoding="utf-8")
            (root / "tests").mkdir()
            (root / "tests" / "test_sample.py").write_text("pass\n", encoding="utf-8")
            before = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            result = inventory(root, hash_manifests=True)
            after = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            self.assertEqual(before, after)
            self.assertEqual(result["files"]["sensitive_files_omitted"], 1)
            payload = json.dumps(result)
            self.assertNotIn("do-not-read", payload)
            self.assertEqual(result["manifests"][0]["path"], "package.json")
            self.assertIn("sha256", result["manifests"][0])
            self.assertIn("tests/test_sample.py", result["indexes"]["tests"])


if __name__ == "__main__":
    unittest.main()
