#!/usr/bin/env python3
"""Build resume evidence units from raw experience notes."""

from __future__ import annotations

from dataclasses import dataclass


LEVELS = {
    "1": "Led",
    "2": "Independently completed",
    "3": "Participated/assisted",
}


@dataclass
class EvidenceUnit:
    project: str
    level: str
    action: str
    method: str
    result: str
    details: str

    def resume_line(self) -> str:
        parts = [self.action, self.method, self.result]
        return ", ".join(part for part in parts if part).rstrip(",. ") + "."

    def markdown_row(self) -> str:
        return (
            f"| {self.project} | {self.level} | {self.action} | "
            f"{self.method} | {self.result} | {self.details} |"
        )


def ask(prompt: str) -> str:
    return input(prompt).strip()


def choose_level() -> str:
    print("\nYour real ownership level:")
    print("1. Led")
    print("2. Independently completed")
    print("3. Participated/assisted")

    while True:
        choice = ask("Choose 1/2/3: ")
        if choice in LEVELS:
            return LEVELS[choice]
        print("Please enter 1, 2, or 3.")


def collect_unit() -> EvidenceUnit:
    print("\nFill with facts. Leave uncertain numbers blank until verified.")
    project = ask("Experience/project name: ")
    level = choose_level()
    action = ask("Specific action: ")
    method = ask("Tool/method: ")
    result = ask("Result/deliverable: ")
    details = ask("Interview-defensible detail: ")

    return EvidenceUnit(
        project=project,
        level=level,
        action=action,
        method=method,
        result=result,
        details=details,
    )


def print_output(units: list[EvidenceUnit]) -> None:
    print("\n## Resume Bullets\n")
    for unit in units:
        print(f"- {unit.resume_line()}")

    print("\n## Evidence Unit Table\n")
    print("| Experience | Level | Action | Tool/Method | Result/Deliverable | Interview Detail |")
    print("| --- | --- | --- | --- | --- | --- |")
    for unit in units:
        print(unit.markdown_row())

    print("\n## Pressure-Test Reminders\n")
    print("- Downgrade or delete any tool, number, or result the user cannot explain.")
    print("- Do not turn participation into ownership.")
    print("- If the result is not numerical, use deliverable, audience, cycle time, or before/after change.")


def main() -> None:
    print("High-density resume evidence-unit builder")
    print("Formula: action + tool/method + result")

    units: list[EvidenceUnit] = []
    while True:
        units.append(collect_unit())
        again = ask("\nAdd another experience? Type y to continue: ").lower()
        if again != "y":
            break

    print_output(units)


if __name__ == "__main__":
    main()
