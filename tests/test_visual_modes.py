import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class VisualModeContractTests(unittest.TestCase):
    def test_skill_routes_all_four_visual_modes(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        for number, name in (
            (9, "VISUAL_UX_AUDIT"),
            (10, "DESIGN_REFERENCE_IMPLEMENTATION"),
            (11, "VISUAL_REGRESSION"),
            (12, "END_TO_END_UAT"),
        ):
            self.assertIn(f"MODE-{number:02d} {name}", skill)

    def test_mode_references_and_templates_exist(self):
        pairs = (
            ("visual-ux-audit.md", "visual-audit-template.md"),
            ("design-reference-implementation.md", "design-reference-implementation-template.md"),
            ("visual-regression.md", "visual-regression-template.md"),
            ("end-to-end-uat.md", "end-to-end-uat-template.md"),
        )
        for reference, template in pairs:
            self.assertTrue((ROOT / "references" / reference).exists())
            self.assertTrue((ROOT / "assets" / template).exists())

    def test_visual_audit_prohibits_source_only_conclusions(self):
        text = (ROOT / "references" / "visual-ux-audit.md").read_text(encoding="utf-8-sig")
        self.assertIn("Source inspection alone cannot support a visual pass or defect conclusion", text)
        self.assertIn("UNVERIFIED", text)

    def test_design_reference_requires_authorization_and_real_business_mapping(self):
        text = (ROOT / "references" / "design-reference-implementation.md").read_text(encoding="utf-8-sig")
        self.assertIn("Default permission is `PLAN_ONLY`", text)
        self.assertIn("real route, component owner, permission, data source", text)
        self.assertIn("fake pages", text)

    def test_visual_regression_rejects_blind_baseline_updates(self):
        text = (ROOT / "references" / "visual-regression.md").read_text(encoding="utf-8-sig")
        self.assertIn("Do not update the baseline merely to make the test pass", text)
        self.assertIn("Pixel difference is evidence, not the quality decision", text)

    def test_uat_requires_persistence_and_real_ai_disclosure(self):
        text = (ROOT / "references" / "end-to-end-uat.md").read_text(encoding="utf-8-sig")
        self.assertIn("persistence", text)
        self.assertIn("real AI or Agent execution", text)
        self.assertIn("A success message or HTTP 2xx is not business completion", text)

    def test_role_routing_does_not_define_new_role_contracts(self):
        text = (ROOT / "references" / "visual-role-routing.md").read_text(encoding="utf-8-sig")
        self.assertIn("creates no new roles", text)
        self.assertIn("81-role contract", text)


if __name__ == "__main__":
    unittest.main()
