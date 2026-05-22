# High-Density Resume

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/Codex%20Skill-high--density--resume-blue.svg)](skills/high-density-resume/SKILL.md)

高密度个人识别型简历构建法：用证据链写简历，而不是用套话堆经历。

同时也是一个跨 agent 的 `SKILL.md` 包，可用于 Claude Code、Codex、OpenClaw 风格本地 agent，以及任何支持 `SKILL.md` 的工具。

> 简历不是经历列表，而是个人能力结构的压缩证据链。每一条内容都要回答三个问题：我是谁、我能做什么、我和别人有什么不同。

这个项目适合：

- 学生、转专业求职者、实习求职者，希望把零散经历写得更像“能干活的人”。
- 工程、技术、产品、运营、商业实践类经历较多，但不知道怎么挖亮点的人。
- 想摆脱 AI 套话简历，写出真实、可追问、可验证表达的人。
- 想用 Markdown、Word、LaTeX 或其他模板重构简历的人。

## 快速开始

1. 先阅读 [方法论](docs/method.md)。
2. 用 [证据单元表](templates/evidence-units.md) 拆解自己的经历。
3. 把最硬、最能讲清楚的经历放进 [简历模板](templates/resume-template.md)。
4. 对照 [完整改写示例](examples/full-walkthrough.md) 和 [Before / After 案例](examples/before-after.md) 删除套话、补足事实。
5. 用 [评分表](docs/rubric.md) 和 [压力测试清单](templates/review-checklist.md) 做最后一轮删改。

如果你有看似“不相关”但能体现个人特质的经历，可以参考 [Distinctive Signals](examples/distinctive-signals.md)，判断它是否能证明社交信任、助人倾向、团队融入或跨领域迁移。

如果你不知道从哪里开始，先看 [用户入口分流工作流](docs/user-entry-workflows.md)：没简历的人走“从零采矿”，有简历的人走“诊断与重构”，只有一段经历的人走“证据单元拆解”。

进阶用法：如果你会同时使用 GPT、DeepSeek、Claude 等多个模型，可以参考 [双 AI 交叉审稿流程](docs/dual-ai-review-workflow.md)，让一个模型写、另一个模型审，再由你把关真实性、个人识别度、求职方向、HR 搜索率和面试追问风险。

测试用例见 [Test Prompts](examples/test-prompts.md)，可以用来检查 Skill 是否正确处理从零采矿、单段经历拆解、已有简历审查和双 AI 审稿。

更系统的人工评测见 [evals](evals/README.md)，用于记录不同 agent/model 的实际输出、评分和需要回流到 Skill 的问题。

也可以直接运行小工具，把经历拆成“动作 + 工具/方法 + 结果”：

```bash
python3 tools/evidence_builder.py
```

输出到 Markdown 文件：

```bash
python3 tools/evidence_builder.py --output my-evidence.md
```

## Agent Skill

仓库内置了一个可复用的跨 agent skill：

```text
skills/high-density-resume/
```

它采用渐进加载结构：

- `SKILL.md`：短入口，只保留触发条件、工作流和输出规则。
- `references/`：完整方法论和 Before / After 改写模式。
- `assets/`：可复制的简历模板和证据单元表。
- `scripts/`：交互式证据单元生成工具。

Claude Code 用户级安装：

```bash
python3 tools/install_skill.py --target claude
```

Claude Code 项目级安装：

```bash
python3 tools/install_skill.py --target claude-project --project /path/to/project
```

Codex / Skills CLI 安装：

```bash
npx skills add zhanfoguang/high-density-resume@high-density-resume
```

OpenClaw 风格本地目录安装：

```bash
python3 tools/install_skill.py --target openclaw
```

更多安装方式见 [Agent Compatibility](docs/agent-compatibility.md)。

## Release Package

这个 GitHub 仓库保持开源展示和社区协作属性。若需要上传到第三方 Skill 平台，可以在本地生成一个干净的发行包，而不是让平台依赖 GitHub 仓库本身。

```bash
python3 tools/build_release.py --version 1.0.0
```

生成内容默认位于：

```text
dist/high-density-resume-v1.0.0/
├── high-density-resume-skill-v1.0.0.zip
├── listing.zh.md
├── listing.en.md
├── package-checklist.md
├── test-report.md
└── release-notes.md
```

其中 zip 是可上传平台的 Skill 包，其他文件用于平台介绍页、审核材料和发布记录。平台私有字段、定价、截图、结算信息需要在上传前按目标平台后台要求手动补充。

## 五步法

| 步骤 | 目标 | 关键动作 | 输出物 |
| --- | --- | --- | --- |
| 1. 挖料 | 把经历拆成事实 | 区分主导、独立完成、参与协助；记录工具、动作、结果 | 证据单元 |
| 2. 搭骨架 | 让 HR 快速归类你 | 提炼“专业底盘 + 工具能力 + 独特习惯/背景” | 个人识别标签 |
| 3. 写血肉 | 用可追问语言呈现能力 | 删除“锻炼了”“学习了”；写真实工具和真实数字 | 高密度项目描述 |
| 4. 排兵布阵 | 优化扫读路径 | 黄金三分之一放最硬证据；经历分类；每条 2-3 行 | 简历结构 |
| 5. 修门面 | 删除噪音 | 答不上来的降级或删除；无关信息删除；保留记忆点 | 最终简历 |

## 证据单元公式

```text
动作 + 工具/方法 + 结果
```

示例：

| 普通写法 | 高密度写法 |
| --- | --- |
| 参与方程式赛车，负责电器相关工作 | 基于参考模板修改并绘制 PCB，使用 Altium Designer 完成关键模块布线，配合完成硬连线调试 |
| 参与抢车号规则分析 | 抢车号阶段使用 Codex 整理规则，上午第 31 名，主动调整策略后提升至第 19 名 |
| 负责活动现场支持 | 在公开分享活动中承担现场设备调试与流程支持，保障讲者切换、投屏和演示环节稳定进行 |

## 仓库结构

```text
.
├── README.md
├── docs/
│   ├── faq.md
│   ├── agent-compatibility.md
│   ├── dual-ai-review-workflow.md
│   ├── method.md
│   ├── rubric.md
│   └── user-entry-workflows.md
├── templates/
│   ├── evidence-units.md
│   ├── resume-template.md
│   └── review-checklist.md
├── examples/
│   ├── before-after.md
│   ├── distinctive-signals.md
│   ├── full-walkthrough.md
│   └── test-prompts.md
├── evals/
│   ├── README.md
│   ├── scorecard.md
│   └── cases/
├── prompts/
│   └── resume-coach.md
├── packaging/
│   ├── manifest.yaml
│   ├── listing.zh.md
│   ├── listing.en.md
│   ├── package-checklist.md
│   ├── test-report-template.md
│   └── release-notes-template.md
├── skills/
│   └── high-density-resume/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/
│       ├── references/
│       └── scripts/
├── tools/
│   ├── build_release.py
│   ├── evidence_builder.py
│   └── install_skill.py
├── CONTRIBUTING.md
└── LICENSE
```

## 核心原则

- 简历上的每一个词，都应该经得起面试追问。
- 宁可写窄写准，不写宽写虚。
- 不要让 HR 猜你是谁，要主动给出清晰的个人识别标签。
- 量化不是编数字，而是把真实结果说清楚。
- 如果一句话既没有回答问题，也没有提供证据，就删掉。

## 常见问题

常见问题已整理到 [FAQ](docs/faq.md)，包括“没有量化结果怎么办”“经历普通怎么写”“AI 能不能帮忙写”等场景。

## 贡献方式

欢迎提交：

- Before / After 改写案例。
- 不同行业的证据单元示例。
- Markdown、Word、LaTeX 简历模板。
- 针对学生、转专业、工程、产品、运营等场景的扩展指南。

提交前请阅读 [贡献指南](CONTRIBUTING.md)。

## License

MIT License. See [LICENSE](LICENSE).
