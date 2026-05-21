# Eval: Single Experience Extraction

## Prompt

```text
Use $high-density-resume 帮我把这段经历写进简历。

我参加过方程式赛车队，做过电器相关工作，也用 AI 帮队里抢车号。PCB 是基于参考模板改的，抢车号一开始成绩不太好，后来我调整了一下整理规则的方法，结果排名变好了。
```

## Model Output

这是“单段经历拆解”场景。当前信息有价值，但还缺几个会影响简历真实性的细节。

必须追问：

1. 你在车队里的角色是什么？整车电器组成员、协助成员，还是具体模块负责人？
2. PCB 用的工具是什么？Altium Designer、立创 EDA，还是其他？
3. PCB 你修改了哪些部分？接口、布线、元件、封装、原理图，还是焊接调试？
4. 抢车号的原始排名和最终排名分别是多少？
5. 你调整的“整理规则方法”是什么？比如规则归档、限制条件拆分、答题策略对比？
6. 策略调整是你个人判断，还是团队共同决定？
7. 这段经历投什么岗位？智能制造、电气、自动化、制造工程，还是 AI 工具应用？

证据单元：

| 动作 | 工具/方法 | 结果/交付物 | 风险 |
| --- | --- | --- | --- |
| 参与方程式赛车电器相关工作 | 基于参考模板修改 PCB | 形成可用于调试的修改文件或实物板 | 不能写成主导整车电气系统 |
| 辅助抢车号规则整理 | AI 工具、规则拆解、策略调整 | 排名提升，但需要具体数字 | 没有数字前不要写“显著提升” |

保守版：

```text
参与方程式赛车队电器相关工作，基于参考模板修改 PCB，并配合完成后续焊接或调试；抢车号阶段使用 AI 工具整理赛事规则，辅助团队比较答题策略。
```

标准版：

```text
参与方程式赛车队电器组工作，基于参考模板完成 PCB 修改，并配合电器相关调试；抢车号阶段使用 AI 工具整理赛事规则、拆分限制条件，主动调整信息处理方式后帮助团队提升排名。
```

高密度版需要补数字后再定稿：

```text
参与方程式赛车队电器组工作，基于参考模板修改 PCB 并配合调试；抢车号阶段使用 AI 工具整理赛事规则、归档限制条件并比较答题策略，排名从第 X 名提升至第 Y 名。
```

## Score

```text
Workflow routing: 3
Truthfulness: 3
Evidence extraction: 3
Follow-up quality: 3
HR searchability: 2
Interview risk: 2
Total: 16
Pass/fail: Pass
```

## Notes

Good pass. HR keywords could be mapped more explicitly to target roles. Interview risk is identified, but severity labels would help.
