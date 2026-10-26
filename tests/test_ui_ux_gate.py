import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class UiUxGateContractTests(unittest.TestCase):
    def test_skill_activates_cross_cutting_gate(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        self.assertIn("UI/UX quality gate", skill)
        self.assertIn("references/ui-ux-quality.md", skill)
        self.assertIn("MODE-09 through MODE-12", skill)

    def test_gate_contains_evidence_constraints_and_decisions(self):
        text = (ROOT / "references" / "ui-ux-quality.md").read_text(encoding="utf-8-sig")
        for required in (
            "actual rendered evidence",
            "Minimum coverage matrix",
            "functional, visual, interaction, and accessibility",
            "pilot acceptance before wider propagation",
            "UI_QUALITY_ACCEPTANCE_READY",
            "UI_QUALITY_BLOCKED",
            "NO_UI_CHANGE_NEEDED",
            "NOT_APPLICABLE",
        ):
            self.assertIn(required, text)
        for root_cause in ("UI-RC-01", "UI-RC-06", "UI-RC-12"):
            self.assertIn(root_cause, text)

    def test_user_facing_modes_link_the_gate(self):
        for name in (
            "project-inception.md",
            "open-source-transformation.md",
            "engineering-planning.md",
            "controlled-implementation.md",
            "project-audit.md",
            "root-cause-diagnosis.md",
            "project-rescue.md",
            "release-readiness.md",
        ):
            text = (ROOT / "references" / name).read_text(encoding="utf-8-sig")
            self.assertIn("ui-ux-quality.md", text, name)

    def test_template_separates_quality_results(self):
        text = (ROOT / "assets" / "ui-ux-audit-template.md").read_text(encoding="utf-8-sig")
        for result in (
            "Functional result", "Visual result", "Interaction result",
            "Accessibility result", "Pilot and propagation",
        ):
            self.assertIn(result, text)

    def test_behavioral_fixture_requires_gate_and_bounded_repair(self):
        fixture = json.loads(
            (ROOT / "tests" / "fixtures" / "ui-ux-defective-project.json").read_text(encoding="utf-8-sig")
        )
        self.assertEqual(fixture["expected"]["primary_mode"], "MODE-05")
        self.assertEqual(fixture["expected"]["companion_gate"], "UI_UX_QUALITY_GATE")
        self.assertIn("pilot before propagation", fixture["expected"]["required_constraints"])


if __name__ == "__main__":
    unittest.main()
