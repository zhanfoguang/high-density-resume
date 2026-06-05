# Launch Audit

这份审计用于判断项目是否已经接近“可公开展示 + 可承接咨询 + 可平台上架”的状态。它不等于收入承诺，只是把当前转化路径和缺口说清楚。

## 当前状态

| 模块 | 状态 | 证据 |
| --- | --- | --- |
| GitHub 开源入口 | 已准备 | `README.md` 包含方法论、模板、Skill 安装、案例、Support 和服务咨询入口 |
| 赞赏入口 | 已准备 | README 使用 `assets/support-wechat.png` |
| 脱敏咨询入口 | 已准备 | `.github/ISSUE_TEMPLATE/resume-diagnosis-request.md` |
| 服务菜单 | 已准备 | `docs/services.md` |
| 建议定价 | 已准备 | `docs/pricing.md` |
| 变现路径说明 | 已准备 | `docs/monetization.md` |
| Coze 上架材料 | 已准备 | `packaging/coze-store-listing.zh.md` |
| Coze 重新部署手册 | 已准备 | `docs/coze-redeploy-runbook.md` |
| 发行包 | 可生成 | `python3 tools/build_release.py --version 0.2.0` |
| 发布自检 | 可运行 | `python3 tools/check_launch_ready.py --release-dir dist/high-density-resume-v0.2.0` |

## 商业化路径

### 1. GitHub 轻转化

适合先建立可信度：

- README 展示完整方法论和可安装 Skill。
- Support 区放微信收款码。
- Issue 模板承接脱敏简历诊断和服务咨询。
- Services 页面说明什么免费、什么适合付费。
- Pricing 页面说明建议价格、交付物、修改边界和付款前确认。

上线前必须完成：

- [x] 替换真实微信收款码。
- [ ] 确认 README 不含个人隐私或错误收款信息。
- [ ] 确认 issue 模板提醒用户脱敏。

### 2. Coze 技能商店

适合产品化分发：

- 使用 `packaging/coze-store-listing.zh.md` 填写名称、分类、简介和案例。
- 使用 3 个案例验证技能能稳定完成低素材挖掘、单段经历改写、AI 建议审查。
- 部署成功后，再处理商店上架、商户/收款、付费模式和审核。

上线前必须完成：

- [ ] 技能部署成功。
- [ ] 3 个案例完整跑完，并能在商店展示。
- [ ] 商户/收款设置由本人确认。
- [ ] 描述中不承诺 offer、ATS 通过率、平台审核通过或固定收入。

### 3. 人工服务

适合从开源信任转成具体交付：

- 脱敏简历诊断。
- 单段经历高密度改写。
- 低素材学生挖掘。
- 完整简历带读。
- Coze / Skill 上架协助。

服务边界见 `docs/services.md`。核心原则是：只加工真实经历，不编经历、不包装虚假数据、不承诺求职结果。

## 当前阻塞项

| 阻塞项 | 为什么阻塞 | 解决方式 |
| --- | --- | --- |
| Coze 未完成公开上架 | 部署成功不等于商店可见，也不等于可收费 | 按 `docs/coze-redeploy-runbook.md` 重建或修复项目，再确认发布和商户设置 |
| 平台收益规则需实时确认 | 平台政策、审核和分成可能变化 | 上架当天阅读平台最新说明后再设置价格 |

## 最小上线定义

GitHub 最小上线：

```text
README 可读 + Skill 可安装 + 服务入口清楚 + 真实赞赏码可用 + 自检通过
```

Coze 最小上线：

```text
技能可用 + 3 个案例完整 + 商店描述合规 + 商户/收款已配置 + 审核通过
```

如果只完成 GitHub，不要宣称已经完成平台商业化。如果只完成 Coze 部署，不要宣称已经能赚钱。
