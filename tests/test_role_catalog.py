import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLE_PATTERN = re.compile(r"^\| ([A-Z][A-Z0-9-]+) /?[^|]*\|")


class RoleCatalogTests(unittest.TestCase):
    def test_exactly_81_unique_role_contracts(self):
        ids = []
        for path in (ROOT / "references" / "roles").glob("*.md"):
            for line in path.read_text(encoding="utf-8-sig").splitlines():
                match = ROLE_PATTERN.match(line)
                if match and match.group(1) != "ID":
                    ids.append(match.group(1))
                    self.assertGreaterEqual(line.count("|"), 8, line)
        self.assertEqual(len(ids), 81)
        self.assertEqual(len(set(ids)), 81)
        self.assertIn("OSS-01", ids)
        self.assertIn("QA-05", ids)

    def test_catalog_references_only_defined_role_ids(self):
        role_ids = set()
        for path in (ROOT / "references" / "roles").glob("*.md"):
            for line in path.read_text(encoding="utf-8-sig").splitlines():
                match = ROLE_PATTERN.match(line)
                if match and match.group(1) != "ID":
                    role_ids.add(match.group(1))
        catalog = (ROOT / "references" / "role-catalog.md").read_text(encoding="utf-8-sig")
        referenced = set(re.findall(r"\b[A-Z][A-Z0-9-]*-[0-9]{2}\b", catalog))
        self.assertTrue(referenced <= role_ids, referenced - role_ids)


if __name__ == "__main__":
    unittest.main()
