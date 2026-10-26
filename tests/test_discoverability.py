import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DiscoverabilityContractTests(unittest.TestCase):
    def test_skill_description_exposes_high_intent_capabilities(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
        match = re.search(r"^description:\s*(.+)$", text, flags=re.MULTILINE)
        self.assertIsNotNone(match)
        description = match.group(1).lower()
        for phrase in (
            "project audits",
            "hidden-capability discovery",
            "open-source transformation",
            "root-cause diagnosis",
            "ui/ux",
            "visual regression",
            "end-to-end uat",
            "project rescue",
            "release readiness",
        ):
            self.assertIn(phrase, description)
        self.assertIn("do not use for a narrow edit with a known solution", description)

    def test_agent_metadata_names_decision_domains(self):
        text = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8-sig")
        for phrase in (
            "视觉/UAT", "根因诊断", "项目救援", "发布决策",
            "compare mature open-source options",
        ):
            self.assertIn(phrase, text)

    def test_readmes_present_concrete_use_cases_near_the_top(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8-sig")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8-sig")
        self.assertLess(english.index("## Use OFE when"), english.index("## Why OFE exists"))
        self.assertLess(chinese.index("## 什么时候使用 OFE"), chinese.index("## 核心能力"))
        normalized_english = re.sub(r"\s+", " ", english)
        normalized_chinese = re.sub(r"\s+", "", chinese)
        for phrase in (
            "project audit", "open-source transformation", "root-cause analysis",
            "UI/UX audit", "project rescue", "release readiness",
            "Windows desktop wrapper", "AI Agent engineering",
        ):
            self.assertIn(phrase, normalized_english)
        for phrase in (
            "项目审计", "开源改造", "根因分析", "UI/UX 审计", "项目救援",
            "发布就绪", "Windows 客户端封装", "AI Agent 工程化",
        ):
            self.assertIn(phrase.replace(" ", ""), normalized_chinese)


if __name__ == "__main__":
    unittest.main()
