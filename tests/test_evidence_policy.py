import sys
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from evidence_check import validate_findings


def valid_finding():
    return {
        "id": "SEC-001",
        "module": "auth",
        "finder_role": "APPSEC-01",
        "status": "CONFIRMED",
        "severity": "HIGH",
        "confidence": "HIGH",
        "baseline": "fixture-v1",
        "method": "static proof and failing test",
        "evidence_level": "E3",
        "evidence_location": "command:python -m unittest",
        "fact": "Unauthorized user is allowed.",
        "inference": "Ownership is not enforced.",
        "unknowns": [],
        "recommendation": "Compare user and owner identifiers.",
        "retest": "Unauthorized access returns false."
    }


class EvidencePolicyTests(unittest.TestCase):
    def test_valid_finding(self):
        self.assertEqual(validate_findings([valid_finding()]), [])

    def test_rejects_duplicate_and_weak_pass(self):
        first = valid_finding()
        first["status"] = "PASSED"
        first["evidence_level"] = "E1"
        second = valid_finding()
        errors = validate_findings([first, second])
        self.assertTrue(any("PASSED requires" in error for error in errors))
        self.assertTrue(any("duplicate" in error for error in errors))

    def test_resolved_requires_retest_result(self):
        item = valid_finding()
        item["status"] = "RESOLVED"
        errors = validate_findings([item])
        self.assertTrue(any("retest_result" in error for error in errors))

    def test_visual_finding_requires_traceable_runtime_fields(self):
        item = valid_finding()
        item["id"] = "UI-001"
        item["finding_type"] = "LAYOUT"
        errors = validate_findings([item])
        self.assertTrue(any("visual finding missing" in error for error in errors))

    def test_accepts_complete_visual_finding(self):
        item = valid_finding()
        item.update({
            "id": "UI-002",
            "finder_role": "QA-02",
            "finding_type": "BUSINESS_FLOW",
            "project_version": "fixture-v1@abc123",
            "route": "/broken-action",
            "user_role": "operator",
            "viewport": "800x600",
            "browser": "Chrome fixture",
            "design_reference": "NOT_APPLICABLE",
            "screenshot": "file:evidence/broken-action.png",
            "reproduction_steps": ["open page", "click Save", "reload"],
            "expected": "value remains after reload",
            "actual": "success text appears but value is not stored",
            "root_cause_evidence": "no API request and empty readback",
            "change_scope": "button submission binding",
            "regression_acceptance": "POST occurs and independent readback matches",
        })
        self.assertEqual(validate_findings([item]), [])


if __name__ == "__main__":
    unittest.main()
