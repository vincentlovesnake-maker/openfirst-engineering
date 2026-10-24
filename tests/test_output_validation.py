import sys
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from validate_outputs import validate_report


def base_report(mode="MODE-03", permission="PLAN_ONLY"):
    return {
        "mode": mode,
        "permission": permission,
        "baseline": "fixture-v1",
        "scope": "bounded fixture",
        "facts": ["current fact"],
        "inferences": [],
        "unknowns": [],
        "recommendations": ["keep scope small"],
        "decision": "KEEP",
        "verification": ["fixture inspected"],
        "completion_state": "COMPLETE",
        "tasks": []
    }


class OutputValidationTests(unittest.TestCase):
    def test_accepts_complete_rescue_contract(self):
        report = base_report("MODE-07", "READ_ONLY")
        report.update({
            "deliverable_scope": ["existing export"],
            "blockers": ["artifact mismatch"],
            "deferred_items": ["spacing"],
            "stop_work": ["duplicate export rewrite"],
            "completion_definition": "candidate hash matches tested build"
        })
        self.assertEqual(validate_report(report), [])

    def test_search_unavailable_requires_unknowns(self):
        report = base_report()
        report["open_source_gate"] = {
            "required": True,
            "search_status": "SEARCH_UNAVAILABLE",
            "decision": "DEFER",
            "local_capability": [],
            "unknowns": []
        }
        errors = validate_report(report)
        self.assertTrue(any("SEARCH_UNAVAILABLE" in error for error in errors))

    def test_read_only_cannot_claim_mutation(self):
        report = base_report("MODE-05", "READ_ONLY")
        report["findings"] = []
        report["mutations_performed"] = ["changed source"]
        errors = validate_report(report)
        self.assertTrue(any("cannot report mutations" in error for error in errors))

    def test_task_requires_acceptance_and_rollback(self):
        report = base_report()
        report["tasks"] = [{"id": "T1", "owner_role": "BE-01", "scope": "one module"}]
        errors = validate_report(report)
        self.assertTrue(any("tasks[0] missing" in error for error in errors))

    def test_ui_ux_gate_requires_rendered_and_separate_results(self):
        report = base_report("MODE-04", "IMPLEMENT_SCOPED")
        report["ui_ux_gate"] = {
            "required": True,
            "surface_type": "task-workbench",
            "users": ["operator"],
            "core_journeys": ["create and recover"],
            "states": ["normal", "failure"],
            "viewports": ["desktop", "mobile"],
            "input_methods": ["keyboard", "pointer"],
            "rendered_evidence": [],
            "functional_result": "PASSED",
            "visual_result": "UNVERIFIED",
            "interaction_result": "PASSED",
            "accessibility_result": "UNVERIFIED",
            "decision": "UI_QUALITY_ACCEPTANCE_READY",
        }
        errors = validate_report(report)
        self.assertTrue(any("rendered_evidence" in error for error in errors))
        self.assertTrue(any("all four quality results" in error for error in errors))

    def test_ui_ux_gate_accepts_bounded_complete_contract(self):
        report = base_report("MODE-04", "IMPLEMENT_SCOPED")
        report["ui_ux_gate"] = {
            "required": True,
            "surface_type": "task-workbench",
            "users": ["operator"],
            "core_journeys": ["create and recover"],
            "states": ["normal", "failure"],
            "viewports": ["desktop", "mobile"],
            "input_methods": ["keyboard", "pointer"],
            "rendered_evidence": ["browser run ui-001"],
            "functional_result": "PASSED",
            "visual_result": "PASSED",
            "interaction_result": "PASSED",
            "accessibility_result": "PASSED",
            "decision": "UI_QUALITY_ACCEPTANCE_READY",
        }
        self.assertEqual(validate_report(report), [])

    def test_ui_ux_no_change_requires_verified_quality(self):
        report = base_report("MODE-05", "READ_ONLY")
        report["findings"] = []
        report["ui_ux_gate"] = {
            "required": True,
            "surface_type": "task-workbench",
            "users": ["operator"],
            "core_journeys": ["review current state"],
            "states": ["normal"],
            "viewports": ["desktop"],
            "input_methods": ["keyboard", "pointer"],
            "rendered_evidence": ["browser run ui-002"],
            "functional_result": "PASSED",
            "visual_result": "UNVERIFIED",
            "interaction_result": "PASSED",
            "accessibility_result": "UNVERIFIED",
            "decision": "NO_UI_CHANGE_NEEDED",
        }
        errors = validate_report(report)
        self.assertTrue(any("all four quality results" in error for error in errors))

    def test_required_ui_ux_gate_cannot_be_not_applicable(self):
        report = base_report("MODE-04", "IMPLEMENT_SCOPED")
        report["ui_ux_gate"] = {
            "required": True,
            "surface_type": "task-workbench",
            "users": ["operator"],
            "core_journeys": ["submit"],
            "states": ["normal"],
            "viewports": ["desktop"],
            "input_methods": ["pointer"],
            "rendered_evidence": ["browser run ui-003"],
            "functional_result": "PASSED",
            "visual_result": "PASSED",
            "interaction_result": "PASSED",
            "accessibility_result": "PASSED",
            "decision": "NOT_APPLICABLE",
        }
        errors = validate_report(report)
        self.assertTrue(any("cannot be NOT_APPLICABLE" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
