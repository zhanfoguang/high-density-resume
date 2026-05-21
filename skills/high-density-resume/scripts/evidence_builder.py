#!/usr/bin/env python3
"""Build resume evidence units from raw experience notes."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


TEXT = {
    "zh": {
        "title": "高密度简历证据单元生成器",
        "formula": "公式：动作 + 工具/方法 + 结果",
        "fact_note": "请按事实填写，不确定的数字先留空，后续核实。",
        "project": "经历/项目名称：",
        "level_title": "你在这段经历里的真实层级：",
        "level_1": "主导",
        "level_2": "独立完成",
        "level_3": "参与协助",
        "choose": "请选择 1/2/3：",
        "choose_error": "请输入 1、2 或 3。",
        "action": "具体动作：",
        "method": "工具/方法：",
        "result": "结果/交付物：",
        "details": "面试可追问细节：",
        "again": "继续添加下一段经历？输入 y 继续，其他键结束：",
        "bullets": "可放入简历的表达",
        "table": "证据单元表",
        "headers": "| 经历/项目 | 我的层级 | 动作 | 工具/方法 | 结果/交付物 | 可追问细节 |",
        "reminders": "压力测试提醒",
        "reminder_1": "如果某个工具、数字或结果讲不清楚，请先降级或删除。",
        "reminder_2": "如果只是参与，不要写成主导。",
        "reminder_3": "如果结果不能量化，就写交付物、影响对象、周期或前后变化。",
        "saved": "已写入：",
        "separator": "，",
        "period": "。",
    },
    "en": {
        "title": "High-density resume evidence-unit builder",
        "formula": "Formula: action + tool/method + result",
        "fact_note": "Fill with facts. Leave uncertain numbers blank until verified.",
        "project": "Experience/project name: ",
        "level_title": "Your real ownership level:",
        "level_1": "Led",
        "level_2": "Independently completed",
        "level_3": "Participated/assisted",
        "choose": "Choose 1/2/3: ",
        "choose_error": "Please enter 1, 2, or 3.",
        "action": "Specific action: ",
        "method": "Tool/method: ",
        "result": "Result/deliverable: ",
        "details": "Interview-defensible detail: ",
        "again": "Add another experience? Type y to continue: ",
        "bullets": "Resume Bullets",
        "table": "Evidence Unit Table",
        "headers": "| Experience | Level | Action | Tool/Method | Result/Deliverable | Interview Detail |",
        "reminders": "Pressure-Test Reminders",
        "reminder_1": "Downgrade or delete any tool, number, or result the user cannot explain.",
        "reminder_2": "Do not turn participation into ownership.",
        "reminder_3": "If the result is not numerical, use deliverable, audience, cycle time, or before/after change.",
        "saved": "Saved to: ",
        "separator": ", ",
        "period": ".",
    },
}


@dataclass
class EvidenceUnit:
    project: str
    level: str
    action: str
    method: str
    result: str
    details: str

    def resume_line(self, lang: str) -> str:
        text = TEXT[lang]
        parts = [self.action, self.method, self.result]
        line = text["separator"].join(part for part in parts if part)
        return line.rstrip("，。,. ") + text["period"]

    def markdown_row(self) -> str:
        return (
            f"| {escape_cell(self.project)} | {escape_cell(self.level)} | "
            f"{escape_cell(self.action)} | {escape_cell(self.method)} | "
            f"{escape_cell(self.result)} | {escape_cell(self.details)} |"
        )


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def ask(prompt: str) -> str:
    return input(prompt).strip()


def choose_level(lang: str) -> str:
    text = TEXT[lang]
    levels = {
        "1": text["level_1"],
        "2": text["level_2"],
        "3": text["level_3"],
    }

    print(f"\n{text['level_title']}")
    print(f"1. {text['level_1']}")
    print(f"2. {text['level_2']}")
    print(f"3. {text['level_3']}")

    while True:
        choice = ask(text["choose"])
        if choice in levels:
            return levels[choice]
        print(text["choose_error"])


def collect_unit(lang: str) -> EvidenceUnit:
    text = TEXT[lang]
    print(f"\n{text['fact_note']}")
    project = ask(text["project"])
    level = choose_level(lang)
    action = ask(text["action"])
    method = ask(text["method"])
    result = ask(text["result"])
    details = ask(text["details"])

    return EvidenceUnit(
        project=project,
        level=level,
        action=action,
        method=method,
        result=result,
        details=details,
    )


def render_markdown(units: list[EvidenceUnit], lang: str) -> str:
    text = TEXT[lang]
    lines = [
        f"## {text['bullets']}",
        "",
    ]

    for unit in units:
        lines.append(f"- {unit.resume_line(lang)}")

    lines.extend(
        [
            "",
            f"## {text['table']}",
            "",
            text["headers"],
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    for unit in units:
        lines.append(unit.markdown_row())

    lines.extend(
        [
            "",
            f"## {text['reminders']}",
            "",
            f"- {text['reminder_1']}",
            f"- {text['reminder_2']}",
            f"- {text['reminder_3']}",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build high-density resume evidence units."
    )
    parser.add_argument(
        "--lang",
        choices=("zh", "en"),
        default="en",
        help="Prompt/output language. Default: en.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional Markdown file path to write the generated evidence units.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    text = TEXT[args.lang]
    print(text["title"])
    print(text["formula"])

    units: list[EvidenceUnit] = []
    while True:
        units.append(collect_unit(args.lang))
        again = ask(f"\n{text['again']}").lower()
        if again != "y":
            break

    output = render_markdown(units, args.lang)
    print(f"\n{output}")

    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"{text['saved']}{args.output}")


if __name__ == "__main__":
    main()
