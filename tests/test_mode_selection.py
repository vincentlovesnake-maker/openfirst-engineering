import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALID_MODES = {f"MODE-{number:02d}" for number in range(1, 9)}
VALID_PERMISSIONS = {
    "READ_ONLY", "PLAN_ONLY", "IMPLEMENT_SCOPED",
    "TEST_IN_SANDBOX", "RELEASE_PREPARATION",
}
VALID_COMPANIONS = {"UI_UX_QUALITY_GATE"}


class ModeSelectionContractTests(unittest.TestCase):
    def test_behavioral_cases_have_bounded_mode_and_permission(self):
        cases = json.loads((ROOT / "tests" / "behavioral-cases.json").read_text(encoding="utf-8-sig"))
        self.assertGreaterEqual(len(cases), 4)
        for case in cases:
            self.assertIn(case["mode"], VALID_MODES)
            self.assertIn(case["permission"], VALID_PERMISSIONS)
            self.assertTrue((ROOT / "tests" / case["fixture"]).exists())
            companions = case.get("companions", [])
            self.assertIsInstance(companions, list)
            self.assertTrue(set(companions) <= VALID_COMPANIONS)

    def test_ui_ux_behavioral_case_activates_companion_gate(self):
        cases = json.loads((ROOT / "tests" / "behavioral-cases.json").read_text(encoding="utf-8-sig"))
        case = next(item for item in cases if item["id"] == "ui-ux-quality-gate")
        self.assertEqual(case["mode"], "MODE-05")
        self.assertIn("UI_UX_QUALITY_GATE", case["companions"])

    def test_planning_and_audit_cases_do_not_grant_implementation(self):
        cases = json.loads((ROOT / "tests" / "behavioral-cases.json").read_text(encoding="utf-8-sig"))
        for case in cases:
            if case["mode"] in {"MODE-01", "MODE-02", "MODE-03", "MODE-05", "MODE-07"}:
                self.assertNotEqual(case["permission"], "IMPLEMENT_SCOPED")


if __name__ == "__main__":
    unittest.main()
