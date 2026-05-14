# Toyota Prius 2004 Elmer 显式电路对齐 FEMM 的仿真配置

## 1. 目的

这份文档只记录一件事：

- 哪一套 Prius 2004 Elmer 显式电路配置已经在本地验证能够对上直接 FEMM 静态 replay；
- 后续如果要复现实验或继续排查，哪些口径必须保持不变；
- 哪些旧配置或旧结果不能再当成当前正确基线使用。

本文档对应的机型文件为：

- `SimulationModels/Toyota_Prius_2004/IPMSM_Toyota_Prius_2004.json`

当前已验证对齐的是单点：

- `static_1200_full_load`
- `speed_rpm = 1200`
- `control_region = MTPA`

## 2. 当前权威结果

当前经过代码路径重新复验、且能与直接 FEMM replay 对齐的结果文件为：

- Elmer 复验结果：`.local/verification/prius_symfix_verify_nt48/summary.json`
- 旧验证工装中的直接 FEMM replay 基线：`.local/verification/elmer_prius2004/summary.json`

对应数值如下：

| 项目 | 数值 |
| --- | ---: |
| 直接 FEMM replay 扭矩 | `474.7511976029111 Nm` |
| 修正后 Elmer 扭矩 | `472.69344949105835 Nm` |
| 扭矩偏差 | `-2.0577481118527317 Nm` |
| 扭矩相对偏差 | `-0.43343716082078476 %` |

这组结果就是当前 Prius 显式电路“能对上 FEMM”的权威参考，不要再用旧文档中的 `601.55 Nm vs 490.36 Nm` 或其他过时数值作为结论。

## 3. 必须固定的比较口径

要得到上面的对齐结果，下面这些口径必须同时成立：

### 3.1 比较对象必须是“直接 FEMM 静态 replay”

允许使用的 FEMM 对照值是：

- `.local/verification/elmer_prius2004/summary.json` 中 `points[0].femm_baseline.Tem_av_Nm`

对 `static_1200_full_load`，它等于：

- `474.7511976029111 Nm`

不要把下面这个值拿来当 Elmer 对照基线：

- `.local/verification/prius2004_full_validation/summary.json` 或其派生点种子中的 `432.4144873777662 Nm`

原因是：

- `432.414... Nm` 是效率图 / 全图验证链路里的点种子口径；
- `474.751... Nm` 才是同分辨率、同工况下的直接 FEMM 静态 replay；
- Prius 这次 Elmer 显式电路对齐，比较口径必须是后者。

### 3.2 时间步与角度步必须固定

当前已验证可对齐 FEMM 的设置是：

- `Nt_tot = 48`
- `Na_tot = 720`
- `Kmesh_fineness = 1.0`

不要把 `nt_tot=12` 的快速试跑结果当成权威基线。该设置可用于快速排查，但不应用来判定 Prius 显式电路是否已经与 FEMM 对齐。

### 3.3 机型文件必须固定

当前对齐结论对应的机型文件是：

- `SimulationModels/Toyota_Prius_2004/IPMSM_Toyota_Prius_2004.json`

如果后续换成别的几何快照、临时导出的 json、或修改过的未提交机型文件，就不能直接沿用本文档中的扭矩基线。

## 4. Elmer 必须满足的配置

### 4.1 磁仿真入口配置

当前可对齐 FEMM 的 Elmer 入口配置为：

- `is_periodicity_a=True`
- `is_periodicity_t=False`
- `is_get_mesh=False`
- `is_save_FEA=True`
- `nb_worker=8`
- `Kmesh_fineness=1.0`

需要注意：

- 仓库默认会向 `ElmerSolver` 注入 `OMP_NUM_THREADS=8`；
- 但本机 `Elmer 26.1-Release` 仍可能在日志中显示 `Running with just one thread per task`；
- 因此“默认 8 线程”是代码执行准则，但本地 Elmer 是否真正并行仍取决于本机二进制构建。

### 4.2 显式电路必须跑在半机闭合扇区

Prius 这条显式 stranded circuit 不能继续沿用最小几何周期扇区。

当前正确规则是：

- 显式电路 FE 扇区会从原始 `1/8` 自动放宽到局部可闭合的 `1/2` 扇区；
- 这一步是 Prius 能稳定对上 FEMM 的前提之一。

如果又退回到过小扇区，局部绕组显式支路无法稳定闭合，结果会重新偏离 FEMM。

### 4.3 绕组连接矩阵必须使用 SWAT-EM 重新生成的符号图

Prius 路径中，显式电路不能直接信任机型 json 里缓存的旧 `wind_mat` 符号。

当前正确规则是：

- Elmer 显式电路使用 `comp_connection_mat()` 重新生成的绕组连接矩阵；
- 若缓存 `wind_mat` 与重建矩阵符号不一致，按重建矩阵为准；
- Rotor 初始角也要与这套重建后的 d 轴定义同步。

这一步如果回退，会直接把 Prius 扭矩拉偏。

### 4.4 半机单并路 Prius 的 `Symmetry Coefficient` 不能继续用 `1/2`

这是本次 Prius 剩余偏差的核心修复点。

对 Prius 当前这类拓扑：

- 半机显式电路
- `Npcp = 1`
- 单并路闭合显式支路

当前正确的分量耦合缩放是：

- `Symmetry Coefficient = 1/sqrt(2) = 0.7071067811865476`

在 `circuits.definitions` 中，这等价于：

- `Ns = sqrt(2) = 1.4142135623730951`

不要再把这类 Prius 半机单并路显式支路写成：

- `Symmetry Coefficient = 1/2`

因为这会把磁场耦合压得过低，直接导致扭矩明显偏小。

## 5. 已确认的错误配置

下面这些配置或口径已经被确认会误导 Prius Elmer 判断：

### 5.1 把半机单并路的 `Symmetry Coefficient` 固定写成 `0.5`

旧结果位于：

- `.local/verification/elmer_prius2004/summary.json`

对应数值：

- 直接 FEMM replay：`474.7511976029111 Nm`
- 旧 Elmer：`351.73503593388165 Nm`
- 扭矩偏差：`-25.911711711346115 %`

这就是当前必须避免的“错误 Prius 显式电路配置”。

### 5.2 用 `nt_tot=12` 的结果当成权威精度结论

`nt_tot=12` 可以用于快速排查，但不能直接替代 `nt_tot=48` 的权威对比结果。

原因是：

- 时间步过少时，Elmer 启动瞬态与后半段准稳态的口径更容易混杂；
- 对 Prius 这种显式电路问题排查，容易出现“看起来接近或过高，但并不是与权威基线同口径”的结果。

### 5.3 把效率图点种子扭矩当成 Elmer 对照基线

不要用：

- `point_seed["Tem_av_Nm"] = 432.4144873777662`

来判断 Prius Elmer 是否对上 FEMM。

正确的判断对象必须是：

- 同工况直接 FEMM replay 的 `474.7511976029111 Nm`

## 6. 推荐的复验流程

后续如果需要确认 Prius 显式电路没有再次跑偏，建议按下面顺序检查：

1. 机型文件仍然是 `SimulationModels/Toyota_Prius_2004/IPMSM_Toyota_Prius_2004.json`
2. 仿真分辨率仍然是 `Nt_tot=48`、`Na_tot=720`、`Kmesh_fineness=1.0`
3. Elmer 显式电路仍然自动放宽到 `1/2` FE 扇区
4. 绕组连接矩阵仍由 SWAT-EM 重建，而不是直接使用旧缓存符号
5. `circuits.definitions` 中 Prius 半机单并路分量的 `Ns` 仍为 `sqrt(2)` 量级，而不是 `2`
6. 对比对象仍然是直接 FEMM replay，而不是效率图点种子

如果以上任意一项被改掉，都不应该再直接引用本文档中的扭矩对齐结论。

## 7. 相关产物

与这次 Prius 修复直接相关的本地结果和文档如下：

- 正确代码路径复验：`.local/verification/prius_symfix_verify_nt48/summary.json`
- 直接修改 `circuits.definitions` 的诊断回放：`.local/verification/prius_symcoef_replay/sc_sqrt2/`
- 历史旧结果与直接 FEMM replay 基线：`.local/verification/elmer_prius2004/summary.json`
- 叶子机型阶段性总结：`Doc/Elmer_Simulation_Optimization_CN.md`

## 8. 当前结论

截至 `2026-04-19`，Toyota Prius 2004 这条“半机、单并路、显式 stranded circuit”路径已经有明确且可复现的正确配置：

- FE 扇区按显式支路闭合规则放宽到半机；
- 绕组符号图按 SWAT-EM 重建；
- Rotor 初始角与重建 d 轴对齐；
- `Symmetry Coefficient` 对这类 Prius 半机单并路支路采用 `1/sqrt(2)`；
- 比较口径固定为 `Nt_tot=48`、`Na_tot=720` 下的直接 FEMM 静态 replay。

在这组配置下，Prius `static_1200_full_load` 的 Elmer 扭矩已经收敛到：

- `472.69344949105835 Nm`

相对直接 FEMM replay：

- `474.7511976029111 Nm`

误差为：

- `-0.43%`

后续如果再出现 Prius Elmer 明显跑偏，优先检查的不是材料、网格或 ParaView，而是本文档第 3 节和第 4 节中的这些配置是否被改回了旧逻辑。
