# Codeup 管理员操作清单

## 1. 目的

本文面向仓库管理员，用于把当前仓库从“本地约定”落地为“远端强制规则”。

适用仓库：

- `origin`: 阿里云 Codeup 主协作仓库
- 默认目标分支：`master`

本清单聚焦三类后台配置：

1. 分支保护
2. commit 规则
3. Merge Request 检查项

## 2. 执行前确认

在调整后台规则前，先确认以下前提已经成立：

- 仓库默认分支仍为 `master`
- 团队成员已经知道后续开发统一走 topic branch
- 当前仓库已有基本质量门禁思路
- 本仓库的治理文档已经合入：
  - `CONTRIBUTING.md`
  - `Doc/Open_Source_Project_Governance_CN.md`

## 3. 分支保护清单

### 3.1 保护 `master`

操作入口：

- Codeup 仓库
- `Settings > Branches`
- `Create Protected Branch Rule`

建议配置：

- Branch：`master`
- 禁止直接 push 到 `master`
- 禁止 force push
- 合并仅允许通过 Merge Request
- Minimum Number of Approvers Required：`1`
- Merge Request Allowed to Approve：至少包含 `Administrator` 和 `Developer`
- Default Reviewer：设置至少 1 名稳定 reviewer
- 开启 `Automated Status Check Passed Before Merge`

说明：

- 阿里云官方文档说明，受保护分支可以限制 push / merge 权限，并配置 reviewer 数量与自动化检查。
- `master` 是当前最关键的保护分支，必须先配置。

### 3.2 保护 `release/*`

如果后续要做正式版本发布，再追加一条保护规则：

- Branch：`release/*`
- 审批人数：`1`
- 禁止直接 push
- 禁止 force push
- 合并仅通过 Merge Request

说明：

- `release/*` 适合承载版本冻结、changelog 整理、发布前修正。

### 3.3 当前不建议保护 `feature/*`

当前阶段不建议把 `feature/*` 全部做成强保护分支，避免日常开发成本过高。

对 `feature/*` 的要求由流程约束承担：

- 必须从 `master` 切出
- 必须推送到远端
- 必须通过 Merge Request 合入 `master`

## 4. Commit 规则清单

操作入口：

- Codeup 仓库
- `Settings > Push Rules`
- `Create Push Rule`

### 4.1 提交标题正则

建议先采用过渡规则，兼容当前仓库已有历史前缀：

```regex
^\[(BF|FEAT|DOC|REF|TEST|CI|API|MOD|REL|CC|WP)\] .+
```

含义：

- 新标准前缀：`BF` `FEAT` `DOC` `REF` `TEST` `CI` `API` `MOD` `REL`
- 兼容历史前缀：`CC` `WP`

建议执行策略：

1. 先用过渡规则跑一段时间
2. 团队稳定后，再考虑去掉 `CC|WP`

### 4.2 强制禁止 force push

建议：

- 在 Push Rules 中关闭强推能力
- 在受保护分支规则中同步禁止 force push

原因：

- 避免覆盖 `master`
- 保证审查和问题追踪可回溯

### 4.3 可选项：提交邮箱规则

如果团队后续要统一身份，可以增加 commit email 规则。

当前不建议立即强制，因为容易阻断已有开发机配置。

## 5. Merge Request 检查项清单

### 5.1 必开检查项

操作入口：

- Codeup 仓库
- `Settings > Branches`
- 进入 `master` 对应的 Protected Branch Rule

建议开启：

- Reviewer checkpoint
- Automated Status Check Before Merge
- Pipeline check

说明：

- 阿里云官方文档说明，Merge Request 支持 reviewer 审批和自动化检查点。
- 当自动化检查未通过时，不应允许合并。

### 5.2 reviewer 规则

建议值：

- Minimum Number of Approvers Required：`1`
- Default Reviewer：至少 `1` 人
- 若后续启用 CodeOwner，再增加 CodeOwner 审批要求

对于核心目录，建议后续追加 CodeOwner：

- `pyleecan/Classes/`
- `pyleecan/Methods/`
- `pyleecan/GUI/`
- `pyleecan/Generator/`
- `Tests/`
- `Doc/`

### 5.3 MR 描述检查项

管理员应要求每个 MR 至少写清楚：

- Summary
- Linked Issue
- Scope
- Validation
- Backward Compatibility

当前仓库已经提供可复用模板：

- `.github/PULL_REQUEST_TEMPLATE.md`

即使 Codeup 不自动套用该模板，也应要求提交者按同样结构填写 MR 描述。

## 6. 流水线与自动检查清单

### 6.1 为 `master` 配置流水线检测

根据阿里云官方文档，建议按下面顺序配置：

1. 进入 MR 或仓库分支设置
2. 为 `master` 创建 Protected Branch Rule
3. 开启 `Automated Status Check Before Merge`
4. 在 `Pipeline Check` 中关联或创建流水线

### 6.2 流水线代码源触发建议

建议开启：

- `Submit Code`
- `Create/Update Merge Request`

建议分支过滤规则：

```regex
master|^feature/.*|^fix/.*|^docs/.*|^refactor/.*|^release/.*
```

说明：

- 阿里云文档说明代码源触发支持正则过滤。
- `Create/Update Merge Request` 适合在 MR 更新时触发验证。
- `Submit Code` 适合在分支推送时做预检查。

### 6.3 当前项目的最小质量门禁建议

管理员需要确保至少有一条等价于以下内容的校验流水线：

- `pre-commit` 或同等仓库策略检查
- `pytest -m star Tests`
- 必要时补充格式检查或关键 smoke test

如果 Codeup Flow 暂时未接管全部测试，也应先保证：

- Merge Request 上至少有一个自动化检查点
- 不允许在无检查情况下直接合并

## 7. 管理员上线顺序

推荐按以下顺序执行，避免一次性把团队卡死：

1. 先合并治理文档
2. 先保护 `master`
3. 再配置 reviewer 数量和默认 reviewer
4. 再加 commit message 正则
5. 再加 pipeline check
6. 最后评估是否启用 CodeOwner

## 8. 每周巡检清单

管理员每周至少检查一次：

- 是否仍有人直接在 `master` 上开发
- 是否存在未写清验证命令的 MR
- 是否有人绕过约定提交不合规 commit message
- `master` 的保护规则是否被改弱
- 自动化检查是否长期失败或失效

## 9. 当前仓库建议的首批配置值

### 9.1 分支保护

- `master`
- 可选：`release/*`

### 9.2 审批人数

- 最低 `1`

### 9.3 commit message 正则

```regex
^\[(BF|FEAT|DOC|REF|TEST|CI|API|MOD|REL|CC|WP)\] .+
```

### 9.4 流水线分支过滤

```regex
master|^feature/.*|^fix/.*|^docs/.*|^refactor/.*|^release/.*
```

## 10. 参考资料

以下内容基于阿里云官方文档整理，信息具有时间敏感性；如果 Codeup 控制台菜单后续调整，应以官方最新页面为准。

- Merge requests:
  https://www.alibabacloud.com/help/en/yunxiao/user-guide/using-merge-requests
- Branch security settings:
  https://www.alibabacloud.com/help/en/yunxiao/user-guide/branch-settings
- Push rule settings:
  https://www.alibabacloud.com/help/en/yunxiao/user-guide/push-rule-settings
- Extend code detection by pipelines:
  https://www.alibabacloud.com/help/en/yunxiao/user-guide/extending-code-detection-through-pipelining
- Code source trigger:
  https://www.alibabacloud.com/help/en/yunxiao/user-guide/code-source-trigger
- Manage branches:
  https://www.alibabacloud.com/help/en/yunxiao/user-guide/management-branch

本文整理日期：`2026-04-21`
