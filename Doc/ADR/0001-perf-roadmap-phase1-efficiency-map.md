# ADR 0001: 性能优化路线图 Phase 1 — 效率图与工况能耗管线

- Status: Proposed
- Date: 2026-05-14
- Authors: pyleecan fork maintainers (magic-alt/pyleecan)
- Related issue: upstream Eomys/pyleecan#214 “Roadmap for the performance optimization of electrical motors”
- Branch: `feature/perf-roadmap-phase1-efficiency-map`

## Context

上游 issue Eomys/pyleecan#214 给出了电机性能优化的长期路线图，覆盖以下方向：

1. 电磁性能（功率、转矩、转矩脉动）
2. 损耗：Joule / 铁耗 / 磁体涡流损耗
3. 其他损耗：变流器、机械
4. 由损耗驱动的温升
5. 标准工况（NEDC / WLTP / HEV）下的效率/能耗
6. 最优控制策略（MTPA / MTPV / 弱磁切换等）

本仓库（magic-alt/pyleecan）已合并的相关基线（master @ 7a7a35f）：

- PR #3：`pyleecan/Functions/Simulation/LUTdq` 与 `DriveCycle`，`ElecLUTdq.solve_torque`，
  `VarSimu` 容错日志，并提供 LUT + drive-cycle 的 demo / 测试。
- PR #5：Elmer 验证资产（SimulationModels、Simu_ref/Femm、`Tests/Validation/Loss`、Prius/Nissan Leaf 文档）。
- PR #6：FEMM/MagFEMM/DXF/SymPy 稳定性回归补丁。

因此当前最具杠杆效应的入口是「LUTdq + DriveCycle」管线：上游 #214 中第 1、2、5、6 项都能在这里
落地，并与 PR #5 的 FEMM/Elmer 损耗验证形成闭环。本 ADR 仅规划 Phase 1，不锁死后续阶段。

## Decision

采用「以效率图 / 工况能耗为主线，分 4 个里程碑推进」的策略，在
`feature/perf-roadmap-phase1-efficiency-map` 上拆分为后续多个聚焦 PR：

### M1 — LUT 损耗聚合（对应 #214 第 1、2 项）

- 在 `pyleecan/Functions/Simulation/LUTdq` 中扩展输出结构：除已有 `Tem`、`Phi_dq` 外，
  补充 `P_jl`、`P_fe`、`P_mag`、`P_tot` 字段（dq 网格上的标量场）。
- 复用 PR #5 的损耗验证算例（Prius、Nissan Leaf）的 FEMM loss post-processing，
  在 LUT 求解阶段顺带写入铁耗 / 磁体损耗插值表，避免再次重算磁场。
- 输出对象规范：新增 `LUTdqLoss`（或在 `LUT_dq` 上扩展属性），保持向后兼容。

### M2 — 最优控制曲面提取（对应 #214 第 9 项）

- 基于 M1 的 `(Id, Iq) → (Tem, P_tot, |V|)` 网格，提取：
  - MTPA：在给定 |I| 等高线上 `argmax(Tem)`。
  - MTPV：在给定 |V|/ω 等高线上 `argmax(Tem)`。
  - 弱磁切换边界：电压裕量约束下的 `Id/Iq` 轨迹。
- 实现入口：`pyleecan/Functions/Simulation/LUTdq/extract_control_surface.py`。
- 与 `ElecLUTdq.solve_torque` 解耦，独立函数 + 单元测试（`Tests/Functions/Simulation/LUTdq/`）。

### M3 — 工况能耗与效率图（对应 #214 第 5 项）

- 复用 PR #3 的 `DriveCycle` 接口：在 `(speed, torque)` 序列上查 LUT，
  对每个时间步累加 `P_tot × dt` → 工况总能耗、平均效率、损耗分解。
- 提供 NEDC / WLTP 段标准数据（轻量 CSV，放入 `pyleecan/Data/DriveCycle/`），
  保持文件 < 50 KB，避免仓库膨胀。
- 输出：`OutDriveCycle` 增加 `energy_in_J`、`energy_loss_J`、`eta_cycle`。
- 文档：`Doc/Efficiency_Map_DriveCycle_CN.md` 串联 LUT → 控制面 → 工况。

### M4 — 温升钩子（对应 #214 第 7 项，最小占位）

- 不在 Phase 1 实现完整热模型。仅在 LUT 求解器中保留温度依赖入口：
  `Conductor.rho(T)`、`Magnet.Br(T)` 的回调钩子，便于后续接入
  `HeatTransferFEMM`（Phase 2）。
- 默认行为保持当前等温假设，避免回归。

## Alternatives Considered

1. **直接攻 3D Elmer（#202/#205 方向）**：技术价值高，但本仓库当前 Elmer 工具链
   仅完成验证资产，启动成本大，先做 Phase 1 风险更低。
2. **先做 HeatTransferFEMM 完整耦合**：依赖热边界条件建模，路径长；放到 Phase 2。
3. **重写 MagFEMM 并行**：PR #6 刚因并行触发 sliding-band bug 而禁用并行；先稳后快。

## Consequences

- 收益：把 PR #3 的 LUT 管线从「转矩查表」升级为「全损耗 + 控制 + 工况能耗」一体化，
  与上游 #214 第 1/2/5/9 项对齐，且能直接复用 PR #5 的验证基准。
- 成本：需要扩展若干 Output 类与 LUT 数据结构，可能涉及 `Class_Dict.json` 重生成。
- 风险：FEMM 损耗后处理在不同机型上数值稳定性需要回归测试，必须配套
  `Tests/Validation/Loss/` 中的算例（PR #5 已铺设）。

## Compatibility and Migration

- 新增字段以可选属性出现（默认 `None`），现有 LUT pickle / json 不受影响。
- `ElecLUTdq.solve_torque` 保持原签名；新接口走新方法 `solve_with_losses`。
- 旧的 `DriveCycle` demo 仍可运行，新指标作为附加输出。

## Rollout Plan

按里程碑拆分独立 PR，每个 PR 必须：

1. 在 `Tests/Validation/Loss/` 或 `Tests/Functions/Simulation/LUTdq/` 增加一个最小回归。
2. `pytest -m star Tests` 必须通过；涉及 FEMM 的标 `@pytest.mark.FEMM`。
3. 更新 `Doc/LUT_Execution_CN.md` 或新增对应中文文档。
4. 不修改 `.local/`、`Exe_gen/dist/` 等打包产物。

回滚策略：每个里程碑 PR 单独 revert 即可，不影响 master 的 FEMM/Elmer 验证基线。

## Next Action

- M1 先行：在本分支下创建子分支 `feature/perf-roadmap-m1-lut-losses`（或直接在本分支上分阶段提交），
  先补充 LUT 损耗字段与 Prius 算例的端到端回归。
