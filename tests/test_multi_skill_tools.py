from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "tools" / "build_release.py"
INSTALL_SCRIPT = ROOT / "tools" / "install_skill.py"
CHECK_SCRIPT = ROOT / "tools" / "check_launch_ready.py"


class MultiSkillToolTests(unittest.TestCase):
    def test_build_rejects_unsupported_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(BUILD_SCRIPT),
                    "--skill",
                    "",
                    "--version",
                    "1.0.0",
                    "--output-dir",
                    directory,
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)

    def test_install_rejects_unsupported_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(INSTALL_SCRIPT),
                    "--skill",
                    "",
                    "--target",
                    "custom",
                    "--path",
                    directory,
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)

    def test_default_build_remains_backward_compatible(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            result = subprocess.run(
                [
                    sys.executable,
                    str(BUILD_SCRIPT),
                    "--version",
                    "1.0.0",
                    "--output-dir",
                    str(output_dir),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            release_dir = output_dir / "high-density-resume-v1.0.0"
            zip_path = release_dir / "high-density-resume-skill-v1.0.0.zip"
            self.assertTrue(zip_path.exists())
            self.assertTrue((release_dir / "assets" / "support-wechat.png").exists())
            self.assertTrue((release_dir / "check_launch_ready.py").exists())
            with zipfile.ZipFile(zip_path) as archive:
                names = set(archive.namelist())
            self.assertIn("manifest.yaml", names)
            self.assertIn("references/common-frameworks.md", names)

    def test_builds_selected_skill_release(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            result = subprocess.run(
                [
                    sys.executable,
                    str(BUILD_SCRIPT),
                    "--skill",
                    "resume-evidence-matcher",
                    "--version",
                    "1.0.0",
                    "--output-dir",
                    str(output_dir),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            zip_path = (
                output_dir
                / "resume-evidence-matcher-v1.0.0"
                / "resume-evidence-matcher-skill-v1.0.0.zip"
            )
            self.assertTrue(zip_path.exists())
            with zipfile.ZipFile(zip_path) as archive:
                names = set(archive.namelist())
                text_entries = "\n".join(
                    archive.read(name).decode("utf-8")
                    for name in names
                    if name.endswith((".md", ".yaml", ".json", ".py"))
                )
                user_templates = {
                    template_path: archive.read(template_path).decode("utf-8")
                    for template_path in (
                        "assets/evidence-inventory-template.md",
                        "assets/report-template.md",
                    )
                }
            self.assertIn("SKILL.md", names)
            self.assertIn("scripts/calculate_coverage.py", names)
            self.assertIn("scripts/select_resume_content.py", names)
            self.assertIn("references/evidence-chain.md", names)
            self.assertIn("references/selection-and-layout.md", names)
            self.assertIn("references/interview-and-proof-plan.md", names)
            self.assertIn("references/markdown-output-safety.md", names)
            self.assertIn("assets/evidence-inventory-template.md", names)
            self.assertIn("manifest.yaml", names)
            self.assertIn("LICENSE", names)
            self.assertFalse(any("openai" in name.lower() for name in names))
            self.assertNotIn("openai", text_entries.lower())
            for template_path, template in user_templates.items():
                self.assertFalse(
                    any(
                        line.strip().startswith("|") and line.strip().endswith("|")
                        for line in template.splitlines()
                    ),
                    template_path,
                )
            release_dir = zip_path.parent
            for filename in (
                "listing.zh.md",
                "listing.en.md",
                "package-checklist.md",
                "test-prompts.md",
                "test-report.md",
                "release-notes.md",
            ):
                self.assertTrue((release_dir / filename).exists(), filename)

    def test_installs_selected_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination_parent = Path(directory)
            result = subprocess.run(
                [
                    sys.executable,
                    str(INSTALL_SCRIPT),
                    "--skill",
                    "resume-evidence-matcher",
                    "--target",
                    "custom",
                    "--path",
                    str(destination_parent),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            destination = destination_parent / "resume-evidence-matcher"
            self.assertTrue((destination / "SKILL.md").exists())
            self.assertTrue((destination / "scripts" / "calculate_coverage.py").exists())
            self.assertFalse((destination_parent / "high-density-resume").exists())

    def test_default_install_remains_backward_compatible(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination_parent = Path(directory)
            result = subprocess.run(
                [
                    sys.executable,
                    str(INSTALL_SCRIPT),
                    "--target",
                    "custom",
                    "--path",
                    str(destination_parent),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            destination = destination_parent / "high-density-resume"
            self.assertTrue((destination / "SKILL.md").exists())
            self.assertTrue((destination / "scripts" / "evidence_builder.py").exists())

    def test_checks_selected_skill_without_release(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(CHECK_SCRIPT),
                "--skill",
                "resume-evidence-matcher",
                "--skip-release",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("skills/resume-evidence-matcher/SKILL.md", result.stdout)
        self.assertIn("Release readiness: PASS", result.stdout)

    def test_selected_release_passes_launch_check(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            build = subprocess.run(
                [
                    sys.executable,
                    str(BUILD_SCRIPT),
                    "--skill",
                    "resume-evidence-matcher",
                    "--version",
                    "1.0.0",
                    "--output-dir",
                    str(output_dir),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr)

            release_dir = output_dir / "resume-evidence-matcher-v1.0.0"
            check = subprocess.run(
                [
                    sys.executable,
                    str(CHECK_SCRIPT),
                    "--skill",
                    "resume-evidence-matcher",
                    "--release-dir",
                    str(release_dir),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
            self.assertIn("Release readiness: PASS", check.stdout)

    def test_default_check_remains_backward_compatible(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHECK_SCRIPT), "--skip-release"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("skills/high-density-resume/SKILL.md", result.stdout)
        self.assertIn("Release readiness: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
