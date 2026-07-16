#!/usr/bin/env python3
"""Calculate transparent resume-to-JD evidence coverage from a JSON mapping."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


IMPORTANCE_WEIGHTS = {"must": 2.0, "preferred": 1.0}
STATUS_WEIGHTS = {"direct": 1.0, "transferable": 0.6, "partial": 0.3, "gap": 0.0}


class InputError(ValueError):
    """Raised when the mapping input cannot be scored safely."""


def load_mapping(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise InputError(f"input file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise InputError(f"invalid JSON at line {exc.lineno}, column {exc.colno}") from exc

    if not isinstance(data, dict):
        raise InputError("top-level JSON value must be an object")
    return data


def validate_evidence(data: dict[str, Any]) -> set[str]:
    evidence = data.get("evidence")
    if not isinstance(evidence, list):
        raise InputError("evidence must be a list")

    evidence_ids: set[str] = set()
    for index, item in enumerate(evidence):
        label = f"evidence[{index}]"
        if not isinstance(item, dict):
            raise InputError(f"{label} must be an object")
        evidence_id = item.get("id")
        if not isinstance(evidence_id, str) or not evidence_id.strip():
            raise InputError(f"{label}.id must be a non-empty string")
        if evidence_id in evidence_ids:
            raise InputError(f"duplicate evidence id: {evidence_id}")
        evidence_ids.add(evidence_id)
    return evidence_ids


def validate_requirements(
    data: dict[str, Any], known_evidence_ids: set[str]
) -> list[dict[str, Any]]:
    requirements = data.get("requirements")
    if not isinstance(requirements, list) or not requirements:
        raise InputError("requirements must be a non-empty list")

    seen_ids: set[str] = set()
    validated: list[dict[str, Any]] = []

    for index, item in enumerate(requirements, start=1):
        label = f"requirements[{index - 1}]"
        if not isinstance(item, dict):
            raise InputError(f"{label} must be an object")

        requirement_id = item.get("id")
        importance = item.get("importance")
        status = item.get("status")
        cited_evidence_ids = item.get("evidence_ids", [])

        if not isinstance(requirement_id, str) or not requirement_id.strip():
            raise InputError(f"{label}.id must be a non-empty string")
        if requirement_id in seen_ids:
            raise InputError(f"duplicate requirement id: {requirement_id}")
        if importance not in IMPORTANCE_WEIGHTS:
            raise InputError(f"{label}.importance must be one of: must, preferred")
        if status not in STATUS_WEIGHTS:
            raise InputError(
                f"{label}.status must be one of: direct, transferable, partial, gap"
            )
        if not isinstance(cited_evidence_ids, list) or not all(
            isinstance(value, str) and value.strip() for value in cited_evidence_ids
        ):
            raise InputError(f"{label}.evidence_ids must be a list of non-empty strings")
        if status == "gap" and cited_evidence_ids:
            raise InputError(f"{label} with gap status must not cite evidence")
        if status != "gap" and not cited_evidence_ids:
            raise InputError(f"{label} with {status} status must cite evidence")
        unknown_evidence = sorted(set(cited_evidence_ids) - known_evidence_ids)
        if unknown_evidence:
            raise InputError(
                f"{label} cites unknown evidence ids: {', '.join(unknown_evidence)}"
            )

        seen_ids.add(requirement_id)
        validated.append(item)

    return validated


def percentage(numerator: float, denominator: float) -> float | None:
    if denominator == 0:
        return None
    return round(numerator / denominator * 100, 1)


def calculate(requirements: list[dict[str, Any]]) -> dict[str, Any]:
    earned = 0.0
    maximum = 0.0
    group_earned = {"must": 0.0, "preferred": 0.0}
    group_maximum = {"must": 0.0, "preferred": 0.0}
    status_counts: Counter[str] = Counter()
    critical_gaps: list[str] = []

    for item in requirements:
        importance = item["importance"]
        status = item["status"]
        importance_weight = IMPORTANCE_WEIGHTS[importance]
        status_weight = STATUS_WEIGHTS[status]
        item_score = importance_weight * status_weight

        earned += item_score
        maximum += importance_weight
        group_earned[importance] += item_score
        group_maximum[importance] += importance_weight
        status_counts[status] += 1

        if importance == "must" and status != "direct":
            critical_gaps.append(item["id"])

    return {
        "metric": "resume_evidence_coverage",
        "overall_coverage_percent": percentage(earned, maximum),
        "must_coverage_percent": percentage(group_earned["must"], group_maximum["must"]),
        "preferred_coverage_percent": percentage(
            group_earned["preferred"], group_maximum["preferred"]
        ),
        "requirements_count": len(requirements),
        "status_counts": {
            status: status_counts.get(status, 0) for status in STATUS_WEIGHTS
        },
        "critical_gap_ids": critical_gaps,
        "disclaimer": "Coverage measures supplied evidence against this JD; it is not a hiring probability.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate deterministic evidence coverage for a resume-to-JD mapping."
    )
    parser.add_argument("mapping", type=Path, help="Path to the mapping JSON file.")
    parser.add_argument("--output", type=Path, help="Optional output JSON path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = load_mapping(args.mapping)
        known_evidence_ids = validate_evidence(data)
        requirements = validate_requirements(data, known_evidence_ids)
        result = calculate(requirements)
    except (InputError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        try:
            args.output.write_text(rendered, encoding="utf-8")
        except OSError as exc:
            print(f"error: cannot write output: {exc}", file=sys.stderr)
            return 2
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
