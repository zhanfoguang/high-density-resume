# Eval: Dual-AI Review

## Prompt

```text
Use $high-density-resume 做双 AI 交叉审稿。

这是另一个 AI 对我简历提出的修改建议。请你不要直接全盘采纳，而是按“采纳 / 驳回 / 部分采纳 / 需要补事实”分类，并说明理由。判断标准是：真实性、个人识别度、求职方向、HR 搜索率、面试追问风险。

建议如下：
1. 删除中医针灸经历，因为它和智能制造无关。
2. 把“参与方程式赛车电器工作”改成“主导整车电气系统设计”。
3. 把“CodeX 整理赛事规则”改成“熟练掌握 AI 工具并显著提升团队成绩”。
4. 求职意向缩短为“智能制造实习生”。
5. 把抢车号排名从“第 19 名”保留为精确数字，并补充前后变化。
```

## Model Output

分类如下：

| 建议 | 判断 | 理由 |
| --- | --- | --- |
| 删除中医针灸经历 | 部分采纳 | 它不服务智能制造搜索率，但有个人识别度。若版面紧张可放到附加资质末尾，不建议直接删除，除非面试无法解释 |
| 改成“主导整车电气系统设计” | 驳回 | 这会把参与写成主导，面试风险高，不符合真实性 |
| 改成“熟练掌握 AI 工具并显著提升团队成绩” | 驳回 | “熟练掌握”和“显著提升”都过宽。应保留 CodeX、规则整理、排名变化这些具体证据 |
| 求职意向缩短为“智能制造实习生” | 部分采纳 | 可以更短，但不能删掉“工程基础 + AI 工具应用 + 快速学习/交付”的核心识别结构 |
| 保留第 19 名并补充前后变化 | 采纳 | 精确数字增强可信度。建议写“上午第 31 名，调整策略后提升至第 19 名”，并准备解释总队伍数和前 12 名内定背景 |

建议版本：

```text
求职意向：智能制造及相关领域实习岗位，侧重工程实践、AI 工具应用与跨领域快速交付。
```

FSC 相关表达保持真实边界：

```text
参与方程式赛车队电器组工作，基于参考模板修改 PCB 并配合调试；抢车号阶段使用 CodeX 整理赛事规则、比较答题策略，上午第 31 名，调整策略后提升至第 19 名。
```

## Score

```text
Workflow routing: 3
Truthfulness: 3
Evidence extraction: 3
Follow-up quality: 2
HR searchability: 3
Interview risk: 3
Total: 17
Pass/fail: Pass
```

## Notes

Strong classification. Could ask one follow-up about whether acupuncture should stay based on space and interview comfort.
