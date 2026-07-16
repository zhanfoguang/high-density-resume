from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "skills"
    / "resume-evidence-matcher"
    / "scripts"
    / "calculate_coverage.py"
)
FIXTURE = (
    ROOT
    / "tests"
    / "fixtures"
    / "resume-evidence-matcher"
    / "sample-mapping.json"
)


class CoverageCliTests(unittest.TestCase):
    def run_cli(self, path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_sample_mapping(self) -> None:
        result = self.run_cli(FIXTURE)
        self.assertEqual(result.returncode, 0, result.stderr)

        payload = json.loads(result.stdout)
        self.assertEqual(payload["overall_coverage_percent"], 60.0)
        self.assertEqual(payload["must_coverage_percent"], 65.0)
        self.assertEqual(payload["preferred_coverage_percent"], 50.0)
        self.assertEqual(payload["critical_gap_ids"], ["R2"])
        self.assertEqual(payload["status_counts"]["gap"], 1)

    def test_gap_cannot_cite_evidence(self) -> None:
        payload = {
            "evidence": [{"id": "E1"}],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "gap",
                    "evidence_ids": ["E1"],
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_cli(path)

        self.assertEqual(result.returncode, 2)
        self.assertIn("gap status must not cite evidence", result.stderr)

    def test_non_gap_requires_evidence(self) -> None:
        payload = {
            "evidence": [{"id": "E1"}],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "preferred",
                    "status": "partial",
                    "evidence_ids": [],
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_cli(path)

        self.assertEqual(result.returncode, 2)
        self.assertIn("partial status must cite evidence", result.stderr)

    def test_empty_requirements_fail_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text('{"evidence": [], "requirements": []}', encoding="utf-8")
            result = self.run_cli(path)

        self.assertEqual(result.returncode, 2)
        self.assertIn("requirements must be a non-empty list", result.stderr)

    def test_invalid_json_fails_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text("{", encoding="utf-8")
            result = self.run_cli(path)

        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid JSON", result.stderr)

    def test_unknown_evidence_id_fails_cleanly(self) -> None:
        payload = {
            "evidence": [{"id": "E1"}],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E9"],
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_cli(path)

        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown evidence ids: E9", result.stderr)

    def test_conflict_evidence_cannot_support_coverage(self) -> None:
        payload = {
            "evidence": [{"id": "E1", "defensibility": "conflict"}],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E1"],
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_cli(path)

        self.assertEqual(result.returncode, 2)
        self.assertIn("conflict evidence ids: E1", result.stderr)

    def test_needs_detail_evidence_cannot_be_direct(self) -> None:
        payload = {
            "evidence": [{"id": "E1", "defensibility": "needs-detail"}],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E1"],
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_cli(path)

        self.assertEqual(result.returncode, 2)
        self.assertIn("needs-detail evidence ids: E1", result.stderr)

    def test_needs_detail_evidence_can_be_partial(self) -> None:
        payload = {
            "evidence": [{"id": "E1", "defensibility": "needs-detail"}],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "partial",
                    "evidence_ids": ["E1"],
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_cli(path)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["overall_coverage_percent"], 30.0)


if __name__ == "__main__":
    unittest.main()
