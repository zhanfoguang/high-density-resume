#!/usr/bin/env python3
"""Build resume evidence units from raw experience notes."""

from __future__ import annotations

from dataclasses import dataclass


LEVELS = {
    "1": "主导",
    "2": "独立完成",
    "3": "参与协助",
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
        return "，".join(part for part in parts if part).rstrip("，。") + "。"

    def markdown_row(self) -> str:
        return (
            f"| {self.project} | {self.level} | {self.action} | "
            f"{self.method} | {self.result} | {self.details} |"
        )


def ask(prompt: str) -> str:
    return input(prompt).strip()


def choose_level() -> str:
    print("\n你在这段经历里的真实层级：")
    print("1. 主导")
    print("2. 独立完成")
    print("3. 参与协助")

    while True:
        choice = ask("请选择 1/2/3：")
        if choice in LEVELS:
            return LEVELS[choice]
        print("请输入 1、2 或 3。")


def collect_unit() -> EvidenceUnit:
    print("\n请按事实填写，不确定的数字先留空，后续核实。")
    project = ask("经历/项目名称：")
    level = choose_level()
    action = ask("具体动作：")
    method = ask("工具/方法：")
    result = ask("结果/交付物：")
    details = ask("面试可追问细节：")

    return EvidenceUnit(
        project=project,
        level=level,
        action=action,
        method=method,
        result=result,
        details=details,
    )


def print_output(units: list[EvidenceUnit]) -> None:
    print("\n## 可放入简历的表达\n")
    for unit in units:
        print(f"- {unit.resume_line()}")

    print("\n## 证据单元表\n")
    print("| 经历/项目 | 我的层级 | 动作 | 工具/方法 | 结果/交付物 | 可追问细节 |")
    print("| --- | --- | --- | --- | --- | --- |")
    for unit in units:
        print(unit.markdown_row())

    print("\n## 压力测试提醒\n")
    print("- 如果某个工具、数字或结果讲不清楚，请先降级或删除。")
    print("- 如果只是参与，不要写成主导。")
    print("- 如果结果不能量化，就写交付物、影响对象、周期或前后变化。")


def main() -> None:
    print("高密度简历证据单元生成器")
    print("公式：动作 + 工具/方法 + 结果")

    units: list[EvidenceUnit] = []
    while True:
        units.append(collect_unit())
        again = ask("\n继续添加下一段经历？输入 y 继续，其他键结束：").lower()
        if again != "y":
            break

    print_output(units)


if __name__ == "__main__":
    main()
