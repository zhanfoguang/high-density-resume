# Test Prompts

Use these prompts to test whether the skill routes different user inputs into the right workflow.

## 1. From-Scratch Mining

Expected behavior: ask follow-up questions first. Do not invent a complete resume.

```text
Use $high-density-resume 帮我写一份实习简历。

我大二，智能制造工程技术专业，想找智能制造相关实习。参加过方程式赛车，会一点 PCB、UG/CAD，也经常用 AI 工具学习和整理资料。其他我不知道怎么写。
```

Check:

- Does the agent ask for target role, education details, projects, tools, deliverables, and interview-defensible facts?
- Does it avoid inventing rankings, awards, companies, or project outcomes?
- Does it output a missing-facts list before drafting?

## 2. Single Experience Extraction

Expected behavior: extract evidence units and ask about ownership, tools, results, and interview risk.

```text
Use $high-density-resume 帮我把这段经历写进简历。

我参加过方程式赛车队，做过电器相关工作，也用 AI 帮队里抢车号。PCB 是基于参考模板改的，抢车号一开始成绩不太好，后来我调整了一下整理规则的方法，结果排名变好了。
```

Check:

- Does the agent ask whether the user led, independently completed, or participated?
- Does it ask for exact ranking, tools, scope, and what was modified?
- Does it provide conservative, standard, and high-density bullet options?

## 3. Low-Material Student Mining

Expected behavior: do not conclude that the user has nothing to write. Mine small real actions, helping behavior, and unusual skills before drafting.

```text
Use $high-density-resume 帮我看看简历能写什么。

我大一，没实习没竞赛，也没什么项目。平时就参加社团活动，帮老师和同学处理过一些小事，会一点 Excel，也学过中医针灸基础，偶尔帮同学做基础放松。目标还不确定，可能想找办公室助理、运营助理或者普通实习。
```

Check:

- Does the agent route into low-material mining instead of saying there is not enough experience?
- Does it ask about course work, micro-tasks, tools, helping behavior, and target direction?
- Does it translate small actions into enterprise value such as execution, communication cost reduction, team trust, and service mindset?
- Does it keep health-related wording conservative and avoid treatment or cure claims?

## 4. Existing Resume Diagnosis

Expected behavior: diagnose before rewriting.

```text
Use $high-density-resume 审查下面这份简历。

请先不要直接重写。请按真实性、个人识别度、求职方向匹配、HR 搜索率、面试可追问性、结构扫读性打分，然后指出最该追问的 10 个问题，最后给出修改计划。

[Paste resume here]
```

Check:

- Does the agent score all six dimensions?
- Does it identify overclaiming risk and missing facts?
- Does it find target-role keyword gaps without keyword stuffing?
- Does it give a revision plan before rewriting?

## 5. Dual-AI Review

Expected behavior: review another AI's suggestions without blindly accepting them.

```text
Use $high-density-resume 做双 AI 交叉审稿。

这是另一个 AI 对我简历提出的修改建议。请你不要直接全盘采纳，而是按“采纳 / 驳回 / 部分采纳 / 需要补事实”分类，并说明理由。判断标准是：真实性、个人识别度、求职方向、HR 搜索率、面试追问风险。

[Paste another AI's critique here]
```

Check:

- Does the agent preserve truthful distinctive signals?
- Does it reject suggestions that make the resume generic?
- Does it identify suggestions that need more facts?
- Does it explain why a suggestion should be accepted or rejected?

## 6. Human Read-Through Risk Check

Expected behavior: act like a strict interviewer and find claims that may fail follow-up questions.

```text
Use $high-density-resume 帮我做面试追问风险检查。

请像严格 HR 一样逐条看我的简历，不要润色。只找这些问题：
1. 哪些词可能会被追问？
2. 哪些地方我如果答不上来就应该降级或删除？
3. 哪些工具、数字、项目名需要补证据？
4. 哪些表达可能写得比事实更大？

[Paste resume here]
```

Check:

- Does the agent focus on risk rather than style?
- Does it recommend downgrading unclear claims?
- Does it separate strong evidence from fragile wording?
