# Eval Case: Dual-AI Review

## Purpose

Test whether the skill reviews another AI's suggestions without blindly accepting them.

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

## Expected Behavior

- Accept preserving exact ranking and before/after change.
- Reject turning participation into ownership.
- Reject or downgrade broad AI mastery claims.
- Partially accept shortening only if it preserves core positioning.
- Discuss whether the distinctive acupuncture signal should be kept, moved, or removed based on target role and interview risk.

## Model Output

Paste output here.

## Score

```text
Workflow routing:
Truthfulness:
Evidence extraction:
Follow-up quality:
HR searchability:
Interview risk:
Total:
Pass/fail:
```

## Skill Improvements

Record anything that should be changed in the skill.
