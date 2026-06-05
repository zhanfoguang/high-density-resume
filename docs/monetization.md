# Monetization Notes

这个项目的商业化原则：开源方法论免费，稳定交付能力可以收费；不夸大收益，不把用户引到不透明流程。

## 1. GitHub 转化入口

适合轻量转化：

- README 末尾放“请我喝茶”收款入口。
- 提供“简历案例改写 / Skill 定制 / 平台上架协助”的联系说明。
- 保持开源内容完整可用，不把核心方法藏起来。
- 用 GitHub issue 承接脱敏案例和服务咨询，避免用户在公开区上传完整隐私简历。

上线前把真实微信收款码保存为：

```text
assets/support-wechat.png
```

推荐用脚本安装，避免手工改错路径：

```bash
python3 tools/install_support_qr.py /path/to/wechat-qr.png
python3 tools/check_launch_ready.py
```

脚本会把图片复制到 `assets/support-wechat.png`，并把 README 的图片路径从占位图改成：

```markdown
<img src="assets/support-wechat.png" width="180" alt="微信收款码" />
```

## 2. 扣子技能商店路径

适合产品化转化：

1. 在扣子编程中部署技能。
2. 进入技能商店上架流程。
3. 填写技能名称、分类、简介、详细介绍和 3 个真实案例。
4. 开通商户或收款能力后，再选择免费、一次性付费或订阅等模式。
5. 用案例证明技能确实能稳定交付：低素材学生挖掘、单段经历改写、面试风险检查。

当前推荐分类：

```text
办公与效率
```

备选分类：

```text
专业咨询 / 教育科研 / 创作与写作
```

推荐定位：

```text
帮普通大学生把零散经历整理成真实、可追问的高密度简历。
```

注意：部署成功不等于自动产生收入。必须完成商店上架、商户/收款配置、付费模式设置和平台审核后，才可能进入付费转化。

可复制的扣子上架材料见：

```text
packaging/coze-store-listing.zh.md
```

如果扣子项目需要从头重做，按这份 runbook 操作：

```text
docs/coze-redeploy-runbook.md
```

## 3. 可收费服务包

可以把开源项目作为信任入口，把人工或半自动交付作为收费项：

| 服务 | 适合对象 | 交付物 |
| --- | --- | --- |
| 简历证据链诊断 | 已有简历但不知道问题在哪 | 评分表、风险清单、追问问题、修改计划 |
| 单段经历高密度改写 | 有项目/活动但写得很虚 | 保守版、标准版、高密度版、面试追问 |
| 低素材学生挖掘 | 没实习没竞赛的学生 | 可写素材表、企业价值翻译、简历骨架 |
| Skill / Coze 上架协助 | 想把方法论做成技能的人 | 技能描述、案例脚本、测试 prompts、上架清单 |

更完整的服务菜单和交付边界见：

```text
docs/services.md
```

建议价格、成交前确认和修改边界见：

```text
docs/pricing.md
```

## 3.1 GitHub 咨询入口设计

公开 issue 只适合接收脱敏问题：

- 某一段经历怎么改。
- 某个表达是否有面试风险。
- 某类普通经历能否写进简历。
- Skill / 扣子上架流程问题。

不适合公开提交：

- 完整未脱敏简历。
- 真实姓名、手机号、微信号、邮箱。
- 身份证、成绩单、合同、公司内部文件。

仓库已提供两个 issue 模板：

```text
.github/ISSUE_TEMPLATE/evidence-case.md
.github/ISSUE_TEMPLATE/resume-diagnosis-request.md
```

## 4. 付费边界

免费部分：

- 方法论、模板、测试 prompts、基础 Skill。
- GitHub issue 里的公开讨论。

适合收费的部分：

- 针对个人经历的深度追问和改写。
- 平台上架材料打磨。
- 一对一简历带读和面试追问模拟。
- 企业/社群内部模板定制。

不建议承诺：

- 保证拿 offer。
- 保证通过 ATS。
- 保证平台上架后一定赚钱。
- 替用户编造经历、奖项、数据或项目结果。

## 5. 发布前检查

- [ ] 已运行发布自检：

```bash
python3 tools/check_launch_ready.py
```

指定某个发行目录：

```bash
python3 tools/check_launch_ready.py --release-dir dist/high-density-resume-v0.2.0
```

如果还没有生成 `dist/` 发行包，可以先运行：

```bash
python3 tools/check_launch_ready.py --skip-release
```

- [ ] README 收款码已替换为真实图片，且不包含私人敏感信息。
- [ ] 扣子商店至少准备 3 个完整案例。
- [ ] 每个案例都能看到技能加载、追问过程和最终交付。
- [ ] 付费描述不夸大，不承诺求职结果。
- [ ] 隐私提醒清楚：用户不要上传未脱敏的身份证、住址、完整手机号等敏感信息。
