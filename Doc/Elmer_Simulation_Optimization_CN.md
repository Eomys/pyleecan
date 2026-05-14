# Elmer 仿真优化总结

## 1. 背景

本轮工作的目标是收敛 Pyleecan 中 Elmer 磁场仿真在 Nissan LEAF 2012 验证点上的扭矩偏差，尤其关注以下两类问题：

- 显式电路模型在周期扇区下的稳定性；
- 高速区 `FW / MTPV` 点与 FEMM 基线对比时的口径一致性。

工作目录内的最终验证结果生成于 `2026-04-17 UTC`，对应输出位于：

- `.local/verification/elmer_leaf2012/summary.json`
- `.local/verification/elmer_leaf2012/report.md`

## 1.1 当前仿真执行准则

自 `2026-04-18` 起，仓库内新建的默认磁仿真统一按以下准则执行：

- `MagElmer` 默认 `nb_worker=8`
- `MagFEMM` 默认 `nb_worker=8`
- `Tests/Validation/Loss/elmer_validation_common.py` 中的 Elmer/FEMM 验证入口统一使用 `8` 线程
- LUT 默认仿真入口 `pyleecan/Methods/Output/LUT/set_default_simulation.py` 统一使用 `8` 线程 FEMM

需要注意：

- FEMM 多进程并行会按该默认值实际展开；
- Elmer 路径已经显式向 `ElmerSolver` 注入 `OMP_NUM_THREADS=8`；
- 但当前本机 Windows 安装的 `Elmer 26.1-Release` 仍会在日志中打印 `Running with just one thread per task`，说明本地二进制暂时没有真正按 8 线程执行。

因此，当前“默认 8 线程”准则对仓库代码和 FEMM 路径已经生效；对本机 Elmer，则属于“默认请求 8 线程，但实际是否并行仍取决于本地 Elmer 构建”。

## 2. 本轮发现的核心问题

### 2.1 Elmer 显式电路在小周期扇区下不稳定

Leaf 48 槽 / 8 极机器在默认周期性设置下，空间周期扇区会缩到 `1/8`。对于 Elmer 的显式 stranded circuit，这种小扇区会导致相绕组在局部域内不能稳定闭合，表现为：

- 扭矩水平异常偏低；
- 同一 `Id/Iq` 点在不同速度区间下误差发散；
- 与 FEMM 的周期解相比，FW/MTPV 区间明显失配。

因此这轮修复把显式电路的有效 FE 扇区从“机器几何允许的最小周期扇区”调整为“至少半机、且绕组在局部域内显式闭合的扇区”。

### 2.2 直接 FEMM 静态 replay 一度只返回扇区扭矩

在排查 9000 rpm MTPV 点时，发现直接静态 `MagFEMM` replay 只得到约整机扭矩的 `1/8`。根因不是物理求解错误，而是 `Magnetics.run()` 在重建裁剪后的 `angle` 轴时丢失了原始 `symmetries`，导致：

- 角轴只覆盖了一个周期扇区；
- Maxwell stress 扭矩后处理无法恢复整机周期性；
- 验证工装中“直接 FEMM 基线”一度错误。

### 2.3 Elmer 高速点包含明显启动瞬态

对 `scalars.dat` 原始扭矩波形检查后发现：

- 3000 rpm 点全段均值与后半段均值差异较小；
- 7000 rpm / 9000 rpm 点全段均值明显低于后半段均值；
- 9000 rpm 点最后半段均值已经逼近直接 FEMM 静态基线，说明主要问题不再是周期缩放，而是启动瞬态污染了平均扭矩。

因此需要在 Elmer 扭矩后处理中增加“稳态窗口”选择，而不是始终对整段瞬态直接取平均。

### 2.4 旧验证工装在高速区口径不够严格

原先 `Tests/Validation/Loss/elmer_validation_common.py` 直接使用效率图 NPZ 中的：

- `full_load__Id`
- `full_load__Iq`
- `full_load__Tem_av`

其中 `full_load__Tem_av` 在高速区并不一定等同于“同分辨率、同静态求解设置下的直接 FEMM 扭矩”。这会把两类误差混在一起：

- LUT/效率图插值和约束求解误差；
- Elmer 与 FEMM 直接磁场求解差异。

因此本轮把验证口径调整为：

1. 用效率图只负责选 `Id/Iq` 种子；
2. 用同 `Nt_tot / Na_tot` 的直接 `MagFEMM` 静态 replay 生成基线；
3. 再用 Elmer 对比该直接 FEMM 基线。

## 3. 代码层面的主要优化

### 3.1 Elmer 显式电路扇区规则

涉及文件：

- `pyleecan/Methods/Simulation/MagElmer/solve_FEA.py`
- `pyleecan/Methods/Simulation/MagElmer/comp_flux_airgap.py`

本轮延续并固化了以下规则：

- 显式 stranded circuit 不再盲目使用最小空间周期扇区；
- FE 扇区会按绕组闭合需求自动放宽到半机或更大；
- 对于不适合该路径的反周期小扇区，明确拒绝继续沿用旧设置；
- 扭矩输出缩放按 Elmer `SaveScalars` 的实际行为处理，避免再次重复乘以整机周期因子。

这部分是本轮 Leaf `FW / MTPV` 稳定性的前提。

### 3.2 保留 angle 轴周期信息

涉及文件：

- `pyleecan/Methods/Simulation/Magnetics/run.py`

在 `angle` 轴长度因 FE 结果回写而被重建时，补回以下元数据：

- `symbol`
- `is_components`
- `is_overlay`
- `symmetries`
- `normalizations`

其中最关键的是 `symmetries`。修复后：

- 直接 FEMM 静态 replay 恢复到整机扭矩口径；
- Maxwell stress 路径不会再把整机扭矩误判为局部扇区扭矩。

### 3.3 Elmer 扭矩稳态窗口选择

涉及文件：

- `pyleecan/Methods/Simulation/MagElmer/solve_FEA.py`

新增了一个保守的后处理函数，用于在显著启动瞬态存在时切到准稳态波形：

- 若“后半段均值”与“全段均值”的相对漂移小于阈值，则保留原始整段波形；
- 若漂移显著，则认为前半段仍在启动过渡期，改用后半段波形平铺回原始长度；
- 这样可以保持 `OutMag` 下游的平均值、波动值、纹波计算逻辑不变，只修正输入波形的稳态代表性。

当前阈值是保守固定值，足以覆盖本轮 Leaf 高速点，不会影响 3000 rpm 点。

### 3.4 Leaf 验证工装改成“直接 FEMM replay 基线”

涉及文件：

- `Tests/Validation/Loss/elmer_validation_common.py`
- `Tests/Validation/Loss/run_elmer_validation_leaf.py`

新流程如下：

1. 从效率图 NPZ 中选取 full-load `Id/Iq` 种子；
2. 先运行一个同分辨率直接 FEMM 静态点；
3. 将该 FEMM 静态点作为真正基线；
4. 再运行 Elmer；
5. 报告中统一显示 `Elmer vs 直接 FEMM 基线`。

这样 FW/MTPV 的误差解释会更干净，不会被 LUT 结果掺杂。

## 4. 测试与验证

### 4.1 单元回归

本轮新增或增强了以下回归覆盖：

- `Tests/Methods/Simulation/test_MagElmer_postproc.py`
  - 显式电路 FE 扇区扩展逻辑；
  - Elmer 扭矩缩放逻辑；
  - Elmer 启动瞬态稳态窗口选择；
- `Tests/Methods/Simulation/test_VarSimu_run_regressions.py`
  - `Magnetics.run()` 在重建 `angle` 轴时保留周期信息。

已执行：

```powershell
pytest Tests\Methods\Simulation\test_VarSimu_run_regressions.py Tests\Methods\Simulation\test_MagElmer_postproc.py -q
```

结果：

- `36 passed`

### 4.2 Leaf 三点验证

已执行：

```powershell
python Tests\Validation\Loss\run_elmer_validation_leaf.py --nt-tot 48 --na-tot 720
```

最终对比口径为：`Elmer vs 同分辨率直接 FEMM 静态 replay`

结果如下：

| 点位 | 区间 | FEMM 扭矩 [Nm] | Elmer 扭矩 [Nm] | 扭矩偏差 |
| --- | --- | ---: | ---: | ---: |
| 3000 rpm | MTPA | 374.272 | 378.871 | +1.23% |
| 7000 rpm | FW | 373.724 | 360.401 | -3.56% |
| 9000 rpm | MTPV | 249.254 | 247.017 | -0.90% |

说明：

- 3000 rpm 点已经稳定在约 `1%` 量级；
- FW 点误差收敛到 `-3.56%`；
- MTPV 点误差收敛到 `-0.90%`；
- 7000 / 9000 点仍然复用了首点 `.msh`，说明“半机显式电路 + mesh reuse”路径在高速区已稳定。

## 5. 当前结论

截至 `2026-04-17 UTC` 的这轮优化，可以给出以下结论：

- Elmer 显式电路在 Leaf 案例中的有效 FE 扇区规则已经稳定；
- `半机显式电路` 规则在 `FW / MTPV` 区间能够保持可接受误差；
- 旧工装中由 `angle` 轴周期信息丢失导致的 FEMM 扇区扭矩问题已经修复；
- Elmer 高速点的主要后处理问题已从“缩放错误”转为“启动瞬态平均”，并已通过稳态窗口逻辑收敛；
- 当前 Leaf 三点验证结果已经可以作为后续 Elmer 回归基线继续使用。

## 6. 尚未处理的非阻塞项

当前还有一个非阻塞项没有纳入本轮提交范围的物理结论：

- Elmer 路径下 `U_rms` 仍可能显示为 `n/a`，因为 `scalars.dat / VTU` 的 winding-voltage 回收还不够稳定。

这不会影响本轮已经收敛的 torque / power 结论，但如果后续需要把电压误差也纳入 Leaf 验证，应继续完善该回收链路。
