# 效率图与工况能耗管线

本文说明 Phase 1 M1-M3 的最小工作流：先生成 LUTdq 效率图，再提取控制曲面，最后在标准或自定义工况上积分能耗与损耗。

## 1. 生成效率图

入口：`pyleecan.Functions.Simulation.LUTdq.run_efficiency_map_lut`

典型输入：

- `simu`：包含 `ElecLUTdq` 的仿真对象。
- `speed_vect`：转速网格，单位 rpm。
- `load_vect`：负载比例网格，范围 `[0, 1]`。

典型输出：

- `Tem_av`、`P_out`、`P_in`、`efficiency`：效率图核心量。
- `Id`、`Iq`、`Ud`、`Uq`、`I_rms`、`U_rms`：控制与约束量。
- `loss_maps`：若每个工作点含 `OutLoss`，则包含 `P_jl`、`P_fe`、`P_mag`、`P_mech`、`P_loss_total` 等 M1 损耗图。

## 2. 提取控制面

入口：`pyleecan.Functions.Simulation.LUTdq.extract_control_surface`

该函数从效率图结果中提取三条曲线：

- `mtpa`：每个速度行中最大 `Tem_av / I_rms` 的 MTPA 工作点。
- `mtpv`：每个速度行中最大 `Tem_av / U_rms` 的 MTPV 工作点。
- `fw_boundary`：每个速度行第一次进入电压受限或非 MTPA 区域的弱磁边界。

如果 M1 损耗图存在，选中的曲线点会同时携带 `P_loss_total`、`P_jl`、`P_fe`、`P_mag` 等损耗值，并给出 `loss_per_torque`。

## 3. 读取工况

入口：

- 自定义 CSV：`pyleecan.Functions.Simulation.DriveCycle.read_drive_cycle_csv`
- 内置轻量片段：`pyleecan.Functions.Simulation.DriveCycle.read_standard_drive_cycle`

内置片段位于 `pyleecan/Data/DriveCycle/`：

- `NEDC_segment.csv`
- `WLTP_class3_segment.csv`

这些文件是用于流水线验证和示例的小型片段，不用于法规认证。若需要完整法规循环，应使用外部来源导入完整速度曲线，并根据车辆传动比、轮胎半径和负载模型转换成电机 `N0` 与 `Tem_av`。

CSV 至少需要：

```csv
time_s,N0,Tem_av
0,0,0
1,1200,20
2,1800,25
```

`read_drive_cycle_csv` 会识别常用别名，例如 `time_s`、`speed_rpm`、`torque_nm`。

## 4. 工况积分

入口：`pyleecan.Functions.Simulation.LUTdq.run_drive_cycle_lut`

该函数复用现有 `DriveCycle` OPMatrix 流程，将 `(time, N0, Tem_av)` 序列交给 `ElecLUTdq` / `VarLoadCurrent` 求解，并在 `result["summary"]` 中返回每步量和积分指标：

- 每步量：`N0`、`Tem_av`、`P_out`、`P_in`、`P_loss`、`efficiency`、`I_rms`、`U_rms`。
- 能量：`energy_out_J`、`energy_in_J`、`energy_loss_J`。
- 循环效率：`eta_cycle = energy_out_J / energy_in_J`。
- 损耗分解：`energy_loss_breakdown_J`，包含可用的 `P_jl`、`P_fe`、`P_mag`、`P_mech`、`P_loss_total` 等积分结果。

当前仓库尚未生成 `OutDriveCycle` 类，因此 M3 输出以 `result["summary"]` 字典形式提供；字段命名与计划中的 `OutDriveCycle` 保持一致，便于后续迁移到正式输出对象。

## 5. 最小示例

```python
import numpy as np

from pyleecan.Functions.Simulation.DriveCycle import read_standard_drive_cycle
from pyleecan.Functions.Simulation.LUTdq import (
    extract_control_surface,
    run_drive_cycle_lut,
    run_efficiency_map_lut,
)

# 1. 生成效率图
emap = run_efficiency_map_lut(
    simu,
    speed_vect=np.array([1000.0, 2000.0, 3000.0]),
    load_vect=np.array([0.25, 0.50, 1.00]),
)

# 2. 提取控制面
surface = extract_control_surface(
    emap,
    Irms_max=simu.elec.Irms_max,
    Urms_max=simu.elec.Urms_max,
)

# 3. 读取内置工况片段并积分能耗
trajectory = read_standard_drive_cycle("wltp_class3")
cycle = run_drive_cycle_lut(simu, trajectory, target="torque")
summary = cycle["summary"]

print(summary["energy_in_J"], summary["energy_loss_J"], summary["eta_cycle"])
print(summary.get("energy_loss_breakdown_J", {}))
```

## 6. 验证建议

- 纯 Python 回归：`pytest Tests/Functions/Simulation/test_drive_cycle.py Tests/Functions/Simulation/test_lutdq_executors.py -q`
- PR 烟测：`pytest -m star Tests -q --no-header`

涉及 FEMM 或真实损耗模型时，应在 `Tests/Validation/Loss/` 中增加机型级回归，并按需要打 `@pytest.mark.FEMM`。
