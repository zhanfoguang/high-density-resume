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
    / "select_resume_content.py"
)


class ResumeContentSelectorCliTests(unittest.TestCase):
    def run_cli(
        self, payload: dict[str, object], *extra_args: str
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mapping.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(path), *extra_args],
                check=False,
                capture_output=True,
                text=True,
            )

    def test_must_have_evidence_wins_limited_core_space(self) -> None:
        payload = {
            "evidence": [
                {
                    "id": "E1",
                    "strength": "strong",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["python"],
                },
                {
                    "id": "E2",
                    "strength": "strong",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["campus-operations"],
                },
            ],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E1"],
                },
                {
                    "id": "R2",
                    "importance": "preferred",
                    "status": "direct",
                    "evidence_ids": ["E2"],
                },
            ],
        }

        result = self.run_cli(payload, "--max-core", "1")

        self.assertEqual(result.returncode, 0, result.stderr)
        decisions = {
            item["evidence_id"]: item for item in json.loads(result.stdout)["decisions"]
        }
        payload_out = json.loads(result.stdout)
        self.assertEqual(decisions["E1"]["decision"], "core")
        self.assertEqual(decisions["E1"]["placement"], "first-third")
        self.assertEqual(decisions["E2"]["decision"], "support")
        self.assertEqual(payload_out["core_capability_tags"], ["python"])
        self.assertEqual(
            payload_out["decision_counts"],
            {"core": 1, "support": 1, "compress": 0, "hide": 0},
        )

    def test_conflicting_evidence_never_enters_final_resume(self) -> None:
        payload = {
            "evidence": [
                {
                    "id": "E1",
                    "strength": "strong",
                    "defensibility": "conflict",
                    "distinctive": False,
                    "capability_tags": ["python"],
                },
                {
                    "id": "E2",
                    "strength": "medium",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["data-analysis"],
                },
            ],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "gap",
                    "evidence_ids": [],
                },
                {
                    "id": "R2",
                    "importance": "must",
                    "status": "transferable",
                    "evidence_ids": ["E2"],
                },
            ],
        }

        result = self.run_cli(payload, "--max-core", "1")

        self.assertEqual(result.returncode, 0, result.stderr)
        decisions = {
            item["evidence_id"]: item for item in json.loads(result.stdout)["decisions"]
        }
        self.assertEqual(decisions["E1"]["decision"], "hide")
        self.assertFalse(decisions["E1"]["finalizable"])
        self.assertEqual(decisions["E2"]["decision"], "core")

    def test_redundant_capability_does_not_fill_core_space(self) -> None:
        payload = {
            "evidence": [
                {
                    "id": "E1",
                    "strength": "strong",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["python"],
                },
                {
                    "id": "E2",
                    "strength": "strong",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["python"],
                },
                {
                    "id": "E3",
                    "strength": "medium",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["reporting"],
                },
            ],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E1", "E2"],
                },
                {
                    "id": "R2",
                    "importance": "preferred",
                    "status": "direct",
                    "evidence_ids": ["E3"],
                },
            ],
        }

        result = self.run_cli(payload, "--max-core", "2")

        self.assertEqual(result.returncode, 0, result.stderr)
        decisions = {
            item["evidence_id"]: item for item in json.loads(result.stdout)["decisions"]
        }
        self.assertEqual(decisions["E1"]["decision"], "core")
        self.assertEqual(decisions["E2"]["decision"], "compress")
        self.assertEqual(decisions["E3"]["decision"], "core")

    def test_same_capability_can_be_core_when_it_covers_new_requirement(self) -> None:
        payload = {
            "evidence": [
                {
                    "id": "E1",
                    "strength": "strong",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["python"],
                },
                {
                    "id": "E2",
                    "strength": "strong",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["python"],
                },
            ],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E1"],
                },
                {
                    "id": "R2",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E2"],
                },
            ],
        }

        result = self.run_cli(payload, "--max-core", "2")

        self.assertEqual(result.returncode, 0, result.stderr)
        decisions = {
            item["evidence_id"]: item for item in json.loads(result.stdout)["decisions"]
        }
        self.assertEqual(decisions["E1"]["decision"], "core")
        self.assertEqual(decisions["E2"]["decision"], "core")

    def test_legacy_evidence_without_tags_is_compressed_when_requirement_repeats(
        self,
    ) -> None:
        payload = {
            "evidence": [
                {"id": "E1", "strength": "strong"},
                {"id": "E2", "strength": "medium"},
            ],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E1", "E2"],
                }
            ],
        }

        result = self.run_cli(payload, "--max-core", "2")

        self.assertEqual(result.returncode, 0, result.stderr)
        decisions = {
            item["evidence_id"]: item for item in json.loads(result.stdout)["decisions"]
        }
        self.assertEqual(decisions["E1"]["decision"], "core")
        self.assertEqual(decisions["E2"]["decision"], "compress")

    def test_redundant_support_evidence_is_compressed_after_core_limit(self) -> None:
        payload = {
            "evidence": [
                {
                    "id": "E1",
                    "strength": "strong",
                    "capability_tags": ["python"],
                },
                {
                    "id": "E2",
                    "strength": "strong",
                    "capability_tags": ["reporting"],
                },
                {
                    "id": "E3",
                    "strength": "medium",
                    "capability_tags": ["reporting"],
                },
            ],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E1"],
                },
                {
                    "id": "R2",
                    "importance": "preferred",
                    "status": "direct",
                    "evidence_ids": ["E2", "E3"],
                },
            ],
        }

        result = self.run_cli(payload, "--max-core", "1")

        self.assertEqual(result.returncode, 0, result.stderr)
        decisions = {
            item["evidence_id"]: item for item in json.loads(result.stdout)["decisions"]
        }
        self.assertEqual(decisions["E1"]["decision"], "core")
        self.assertEqual(decisions["E2"]["decision"], "support")
        self.assertEqual(decisions["E3"]["decision"], "compress")

    def test_unmatched_distinctive_evidence_is_compressed_not_deleted(self) -> None:
        payload = {
            "evidence": [
                {
                    "id": "E1",
                    "strength": "strong",
                    "defensibility": "ready",
                    "distinctive": False,
                    "capability_tags": ["python"],
                },
                {
                    "id": "E2",
                    "strength": "medium",
                    "defensibility": "ready",
                    "distinctive": True,
                    "capability_tags": ["community-trust"],
                },
            ],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "direct",
                    "evidence_ids": ["E1"],
                }
            ],
        }

        result = self.run_cli(payload, "--max-core", "1")

        self.assertEqual(result.returncode, 0, result.stderr)
        decisions = {
            item["evidence_id"]: item for item in json.loads(result.stdout)["decisions"]
        }
        self.assertEqual(decisions["E1"]["decision"], "core")
        self.assertEqual(decisions["E2"]["decision"], "compress")
        self.assertEqual(decisions["E2"]["placement"], "low-priority")

    def test_incomplete_evidence_is_held_for_confirmation(self) -> None:
        payload = {
            "evidence": [
                {
                    "id": "E1",
                    "strength": "strong",
                    "defensibility": "needs-detail",
                    "distinctive": False,
                    "capability_tags": ["reporting"],
                }
            ],
            "requirements": [
                {
                    "id": "R1",
                    "importance": "must",
                    "status": "partial",
                    "evidence_ids": ["E1"],
                }
            ],
        }

        result = self.run_cli(payload)

        self.assertEqual(result.returncode, 0, result.stderr)
        decision = json.loads(result.stdout)["decisions"][0]
        self.assertEqual(decision["decision"], "support")
        self.assertEqual(decision["placement"], "pending-confirmation")
        self.assertFalse(decision["finalizable"])
        self.assertIn("确认", decision["reason"])


if __name__ == "__main__":
    unittest.main()
