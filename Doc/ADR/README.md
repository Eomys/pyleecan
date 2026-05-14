# ADR 使用说明

ADR 是 Architecture Decision Record，用来记录影响仓库长期演进的重要决策。

以下场景必须新增 ADR：

- 公共 Python API 的破坏性调整
- 模块拆分、重命名、跨层重构
- 核心依赖替换或版本策略收紧
- 外部求解器耦合方式变化
- 序列化格式、配置结构、输出契约变化

使用要求：

1. 新文件命名为 `NNNN-short-title.md`
2. `NNNN` 使用四位序号，按创建顺序递增
3. 状态字段只使用 `Proposed`、`Accepted`、`Superseded`、`Deprecated`
4. 一个 ADR 只表达一个核心决策
5. ADR 合并后如果结论变化，应新增后续 ADR，而不是重写历史

起草模板见 [0000-template.md](0000-template.md)。
