from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "resume-evidence-matcher"


class MarkdownOutputSafetyTests(unittest.TestCase):
    def test_user_content_templates_do_not_use_markdown_tables(self) -> None:
        for relative_path in (
            "assets/evidence-inventory-template.md",
            "assets/report-template.md",
        ):
            with self.subTest(relative_path=relative_path):
                text = (SKILL_DIR / relative_path).read_text(encoding="utf-8")
                table_rows = re.findall(r"(?m)^\s*\|.*\|\s*$", text)
                self.assertEqual(table_rows, [], relative_path)

    def test_skill_bundles_explicit_field_rendering_rules(self) -> None:
        reference_path = SKILL_DIR / "references" / "markdown-output-safety.md"
        self.assertTrue(reference_path.exists())

        reference = reference_path.read_text(encoding="utf-8")
        for required_fragment in (
            "&amp;",
            "&lt;",
            "&gt;",
            "&#124;",
            " ↩ ",
            "首个非空白字符",
            "`=`、`+`、`-` 或 `@`",
            "前置一个半角单引号",
        ):
            with self.subTest(required_fragment=required_fragment):
                self.assertIn(required_fragment, reference)

        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/markdown-output-safety.md", skill)


if __name__ == "__main__":
    unittest.main()
