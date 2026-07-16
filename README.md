# High-Density Resume

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/Codex%20Skill-high--density--resume-blue.svg)](skills/high-density-resume/SKILL.md)

高密度个人识别型简历构建法：用证据链写简历，而不是用套话堆经历。仓库提供两个互补的跨 agent `SKILL.md` 包，可用于 Claude Code、Codex、OpenClaw 风格本地 agent，以及任何支持 `SKILL.md` 的工具。

> 简历不是经历列表，而是个人能力结构的压缩证据链。每一条内容都要回答三个问题：我是谁、我能做什么、我和别人有什么不同。

## What It Does

- 把零散经历拆成 `动作 + 工具/方法 + 结果` 的证据单元。
- 区分主导、独立完成、参与协助，避免把简历写虚。
- 同时照顾 HR 扫读、ATS/机器关键词、岗位价值和面试追问。
- 支持从零采矿、单段经历拆解、已有简历审查、双 AI 交叉审稿和面试风险检查。
- 对大一大二、项目少或觉得“没东西可写”的用户，从课程、社团微任务、帮助他人、AI 辅助学习和非典型技能里挖掘真实证据。
- 面向具体 JD 建立“岗位要求 → 经历证据 → 安全表述”链路，计算可复算的材料证据覆盖率，区分材料缺口与能力缺口。

## Choose A Skill

| 你的任务 | 使用的 Skill |
| --- | --- |
| 没有明确 JD，想从零挖经历、改写或审查简历 | [`high-density-resume`](skills/high-density-resume/SKILL.md) |
| 已有具体 JD，想做证据匹配、定制投递和面试风险检查 | [`resume-evidence-matcher`](skills/resume-evidence-matcher/SKILL.md) |

## Start Here

| 你现在有什么 | 先看这里 |
| --- | --- |
| 不知道怎么开始 | [用户入口分流工作流](docs/user-entry-workflows.md) |
| 想理解完整方法 | [方法论](docs/method.md) |
| 想直接填模板 | [简历模板](templates/resume-template.md) / [ATS 友好模板](templates/ats-friendly-resume-template.md) |
| 想融合 STAR/CAR/PAR/XYZ | [常见简历框架适配](docs/common-resume-frameworks.md) |
| 想看改写效果 | [完整改写示例](examples/full-walkthrough.md) / [Before & After](examples/before-after.md) |
| 想检查机器筛选和 HR 扫读 | [HR 与机器筛选友好规则](docs/hr-machine-screening.md) |
| 想评估当前简历 | [评分表](docs/rubric.md) / [压力测试清单](templates/review-checklist.md) |
| 已有具体 JD，想诊断证据覆盖 | [`resume-evidence-matcher`](skills/resume-evidence-matcher/SKILL.md) |

如果你有看似“不相关”但能体现个人特质的经历，参考 [Distinctive Signals](examples/distinctive-signals.md)，判断它是否能证明社交信任、助人倾向、团队融入或跨领域迁移。

## Use As An Agent Skill

User-level install for Claude-style skill directories:

```bash
python3 tools/install_skill.py --target claude
```

安装 JD 证据匹配 Skill：

```bash
python3 tools/install_skill.py --skill resume-evidence-matcher --target claude
```

Codex / Skills CLI 安装：

```bash
npx skills add zhanfoguang/high-density-resume@high-density-resume
```

```bash
npx skills add zhanfoguang/high-density-resume@resume-evidence-matcher
```

Project-level install for Claude-style skill directories:

```bash
python3 tools/install_skill.py --target claude-project --project /path/to/project
```

OpenClaw 风格本地目录安装：

```bash
python3 tools/install_skill.py --target openclaw
```

更多安装方式见 [Agent Compatibility](docs/agent-compatibility.md)。测试用例见 [Test Prompts](examples/test-prompts.md)，系统评测见 [evals](evals/README.md)。

## CLI Helper

把经历拆成“动作 + 工具/方法 + 结果”：

```bash
python3 tools/evidence_builder.py --output my-evidence.md
```

## Release Package

GitHub 仓库保持开源展示和社区协作属性；上传第三方 Skill 平台时，使用本地生成的干净发行包。

```bash
python3 tools/build_release.py --version 1.0.0
```

构建 JD 证据匹配 Skill：

```bash
python3 tools/build_release.py --skill resume-evidence-matcher --version 1.0.0
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

其中 zip 是可上传平台的 Skill 包，其他文件用于平台介绍页、审核材料和发布记录。

选择 `resume-evidence-matcher` 时，对应输出位于 `dist/resume-evidence-matcher-v1.0.0/`。

发布前可运行自检：

```bash
python3 tools/check_launch_ready.py
```

指定某个发行目录：

```bash
python3 tools/check_launch_ready.py --release-dir dist/high-density-resume-v0.2.0
```

CI 或尚未生成 `dist/` 时可运行：

```bash
python3 tools/check_launch_ready.py --skip-release
```

指定 Skill 自检：

```bash
python3 tools/check_launch_ready.py --skill resume-evidence-matcher --skip-release
```

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
├── assets/
│   ├── support-wechat.png
│   └── support-wechat-placeholder.svg
├── docs/
│   ├── faq.md
│   ├── agent-compatibility.md
│   ├── common-resume-frameworks.md
│   ├── dual-ai-review-workflow.md
│   ├── hr-machine-screening.md
│   ├── method.md
│   ├── rubric.md
│   └── user-entry-workflows.md
├── templates/
│   ├── ats-friendly-resume-template.md
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
│   ├── release-notes-template.md
│   └── resume-evidence-matcher/
├── skills/
│   ├── high-density-resume/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── assets/
│   │   ├── references/
│   │   ├── scripts/
│   │   └── test-prompts.json
│   └── resume-evidence-matcher/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/
│       ├── references/
│       ├── scripts/
│       └── test-prompts.json
├── tools/
│   ├── build_release.py
│   ├── check_launch_ready.py
│   ├── evidence_builder.py
│   └── install_skill.py
├── tests/
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

## Support

如果这个项目帮你把简历写得更真实、更能被 HR 看懂，可以请我喝杯茶。

<p>
  <img src="assets/support-wechat.png" width="180" alt="微信收款码" />
</p>

## License

MIT License. See [LICENSE](LICENSE).
