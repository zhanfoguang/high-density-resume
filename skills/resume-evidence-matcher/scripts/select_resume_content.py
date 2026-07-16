#!/usr/bin/env python3
"""Rank resume evidence for a specific JD and assign layout decisions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from calculate_coverage import (
    IMPORTANCE_WEIGHTS,
    STATUS_WEIGHTS,
    InputError,
    load_mapping,
    validate_evidence,
    validate_requirements,
)


STRENGTH_WEIGHTS = {"strong": 1.0, "medium": 0.75, "weak": 0.5}
DEFENSIBILITY_WEIGHTS = {"ready": 1.0, "needs-detail": 0.5, "conflict": 0.0}


def validate_evidence_metadata(data: dict[str, Any]) -> list[dict[str, Any]]:
    evidence = data["evidence"]
    validated: list[dict[str, Any]] = []
    for index, item in enumerate(evidence):
        label = f"evidence[{index}]"
        strength = item.get("strength", "medium")
        defensibility = item.get("defensibility", "ready")
        distinctive = item.get("distinctive", False)
        capability_tags = item.get("capability_tags", [])

        if strength not in STRENGTH_WEIGHTS:
            raise InputError(
                f"{label}.strength must be one of: strong, medium, weak"
            )
        if defensibility not in DEFENSIBILITY_WEIGHTS:
            raise InputError(
                f"{label}.defensibility must be one of: ready, needs-detail, conflict"
            )
        if not isinstance(distinctive, bool):
            raise InputError(f"{label}.distinctive must be a boolean")
        if not isinstance(capability_tags, list) or not all(
            isinstance(value, str) and value.strip() for value in capability_tags
        ):
            raise InputError(
                f"{label}.capability_tags must be a list of non-empty strings"
            )

        validated.append(
            {
                **item,
                "strength": strength,
                "defensibility": defensibility,
                "distinctive": distinctive,
                "capability_tags": capability_tags,
            }
        )
    return validated


def calculate_priority(
    evidence: list[dict[str, Any]], requirements: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    requirement_links: dict[str, list[dict[str, Any]]] = {
        item["id"]: [] for item in evidence
    }
    for requirement in requirements:
        for evidence_id in requirement.get("evidence_ids", []):
            requirement_links[evidence_id].append(requirement)

    ranked: list[dict[str, Any]] = []
    for item in evidence:
        links = requirement_links[item["id"]]
        base_score = sum(
            IMPORTANCE_WEIGHTS[requirement["importance"]]
            * STATUS_WEIGHTS[requirement["status"]]
            for requirement in links
        )
        score = (
            base_score
            * STRENGTH_WEIGHTS[item["strength"]]
            * DEFENSIBILITY_WEIGHTS[item["defensibility"]]
        )
        ranked.append(
            {
                "evidence_id": item["id"],
                "priority_score": round(score, 2),
                "requirement_ids": [requirement["id"] for requirement in links],
                "capability_tags": item["capability_tags"],
                "defensibility": item["defensibility"],
                "distinctive": item["distinctive"],
            }
        )

    return sorted(
        ranked,
        key=lambda item: (-item["priority_score"], item["evidence_id"]),
    )


def assign_decisions(
    ranked: list[dict[str, Any]], max_core: int
) -> list[dict[str, Any]]:
    eligible_core = [
        item
        for item in ranked
        if item["priority_score"] > 0 and item["defensibility"] == "ready"
    ]
    core_ids: set[str] = set()
    selected_tags: set[str] = set()
    selected_requirements: set[str] = set()
    redundant_ids: set[str] = set()
    for item in eligible_core:
        item_tags = set(item["capability_tags"])
        item_requirements = set(item["requirement_ids"])
        if (
            item_tags.issubset(selected_tags)
            and item_requirements.issubset(selected_requirements)
        ):
            redundant_ids.add(item["evidence_id"])
            continue
        if len(core_ids) >= max_core:
            continue
        core_ids.add(item["evidence_id"])
        selected_tags.update(item_tags)
        selected_requirements.update(item_requirements)

    retained_tags = set(selected_tags)
    retained_requirements = set(selected_requirements)
    decisions: list[dict[str, Any]] = []
    for item in ranked:
        if item["evidence_id"] in core_ids:
            decision = "core"
            placement = "first-third"
            reason = "岗位关联强且事实可确认，进入核心优势区。"
        elif item["evidence_id"] in redundant_ids:
            decision = "compress"
            placement = "condensed-support"
            reason = "能力标签与核心证据重复，压缩呈现以节省版面。"
        elif item["priority_score"] > 0:
            item_tags = set(item["capability_tags"])
            item_requirements = set(item["requirement_ids"])
            repeats_retained_evidence = (
                item["defensibility"] == "ready"
                and item_tags.issubset(retained_tags)
                and item_requirements.issubset(retained_requirements)
            )
            if repeats_retained_evidence:
                decision = "compress"
                placement = "condensed-support"
                reason = "能力标签和岗位要求与已保留证据重复，压缩呈现。"
            elif item["defensibility"] == "needs-detail":
                decision = "support"
                placement = "pending-confirmation"
                reason = "与岗位有关，但关键事实尚需确认，不进入正式简历。"
            else:
                decision = "support"
                placement = "supporting-section"
                reason = "与岗位有关，但未进入有限的核心优势位置。"
                retained_tags.update(item_tags)
                retained_requirements.update(item_requirements)
        elif item["distinctive"] and item["defensibility"] == "ready":
            decision = "compress"
            placement = "low-priority"
            reason = "与JD无直接映射，但有可解释的差异化价值，低优先保留。"
        else:
            decision = "hide"
            placement = "omit"
            if item["defensibility"] == "conflict":
                reason = "事实存在冲突，本次隐藏并要求核验。"
            else:
                reason = "当前无岗位映射或可解释差异化价值，本次隐藏。"
        decisions.append(
            {
                **item,
                "decision": decision,
                "placement": placement,
                "finalizable": item["defensibility"] == "ready",
                "reason": reason,
            }
        )
    return decisions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Select and place resume evidence for one JD."
    )
    parser.add_argument("mapping", type=Path, help="Path to the mapping JSON file.")
    parser.add_argument(
        "--max-core",
        type=int,
        default=3,
        help="Maximum number of evidence items placed in the first third. Default: 3.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_core < 1:
        print("error: --max-core must be at least 1", file=sys.stderr)
        return 2

    try:
        data = load_mapping(args.mapping)
        known_evidence_ids = validate_evidence(data)
        requirements = validate_requirements(data, known_evidence_ids)
        evidence = validate_evidence_metadata(data)
        ranked = calculate_priority(evidence, requirements)
        decisions = assign_decisions(ranked, args.max_core)
    except (InputError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    core_capability_tags: list[str] = []
    for item in decisions:
        if item["decision"] != "core":
            continue
        for tag in item["capability_tags"]:
            if tag not in core_capability_tags:
                core_capability_tags.append(tag)
    decision_counts = {
        decision: sum(item["decision"] == decision for item in decisions)
        for decision in ("core", "support", "compress", "hide")
    }
    result = {
        "metric": "resume_content_priority",
        "core_capability_tags": core_capability_tags,
        "decision_counts": decision_counts,
        "decisions": decisions,
        "disclaimer": (
            "Priority ranks supplied evidence for this JD; it is not a candidate score."
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
