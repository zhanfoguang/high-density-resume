# Eval: From-Scratch Mining

## Prompt

```text
Use $high-density-resume 帮我写一份实习简历。

我大二，智能制造工程技术专业，想找智能制造相关实习。参加过方程式赛车，会一点 PCB、UG/CAD，也经常用 AI 工具学习和整理资料。其他我不知道怎么写。
```

## Model Output

这是“从零开始采矿”场景。你现在给的信息还不够直接生成完整简历，我先不编内容。我们先把经历拆成可写进简历的证据单元。

请先回答这些问题：

1. 目标岗位更偏哪一类：智能制造工程、设备/电气、工艺、自动化、生产技术，还是不限方向？
2. 学校、年级、主修课程、绩点或排名有没有可以写的信息？
3. 方程式赛车里你具体做了什么？是主导、独立完成，还是参与协助？
4. PCB 是从零设计、基于模板修改、焊接调试，还是只学习过？
5. UG/CAD 用在什么场景？做过建模、装配、工程图，还是只上过课？
6. AI 工具具体用过哪些？GPT、Codex、Claude、DeepSeek？用于规则整理、代码、资料归纳，还是项目交付？
7. 有没有交付物：图纸、PCB 文件、调试记录、排名、比赛结果、作品链接、报告？
8. 哪些经历面试时你能讲清楚？哪些只是接触过，不能写太满？
9. 你是否有证书、比赛、开源项目、实习、课程项目或公开分享？
10. 你希望简历突出“工程硬件”“AI 工具”“跨领域学习”里的哪一个主线？

目前可以先形成一个待补证据表：

| 经历 | 当前信息 | 缺失事实 | 可能写法 |
| --- | --- | --- | --- |
| 方程式赛车 | 参加过 | 角色、动作、工具、结果 | 参与 FSC 车队，完成某类电器/建模/调试工作 |
| PCB | 会一点 | 工具、是否实际修改/焊接/调试 | 使用某工具完成某模块 PCB 修改或调试 |
| UG/CAD | 会一点 | 使用场景、交付物 | 使用 UG/CAD 完成零部件建模或工程图 |
| AI 工具 | 经常使用 | 工具名、任务、结果 | 使用 AI 工具整理规则、生成清单或辅助学习 |

下一步你先回答第 1、3、4、5、6、7 题，我再帮你生成第一版简历骨架。

## Score

```text
Workflow routing: 3
Truthfulness: 3
Evidence extraction: 2
Follow-up quality: 3
HR searchability: 3
Interview risk: 3
Total: 17
Pass/fail: Pass
```

## Notes

Correctly avoided drafting a full resume. Evidence extraction is only partial because the input is sparse, which is appropriate.
