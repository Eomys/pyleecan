# LUT 执行器与效率 Map 工程化说明

本轮在现有 `VarLoadCurrent + ElecLUTdq + LUTdq` 主链路上补了两块工程化能力：

1. `Tem_av_ref` 目标转矩求解
2. 基于 LUT 的 drive cycle / efficiency map 执行器

这样前一轮新增的 `DriveCycle` 适配层不再只是“读 CSV + 拼 OPMatrix”，而是可以直接驱动主流程完成整段工况和效率 map 求解。

## 0. 默认线程准则

自 `2026-04-18` 起，`LUT.set_default_simulation()` 创建的默认磁仿真统一使用：

- `MagFEMM(nb_worker=8)`

这意味着：

- 没有显式覆写线程数时，LUT 相关默认效率图/工况矩阵仿真都会按 8 线程配置；
- 若测试或特定平台需要其他线程数，仍应在调用侧显式传入并覆写，不再依赖旧的 `4` 线程默认值。

## 1. 主流程补齐点

### 1.1 `ElecLUTdq` 新增 `solve_torque`

新增文件：

- `pyleecan/Methods/Simulation/ElecLUTdq/solve_torque.py`

`ElecLUTdq.run()` 现在的调度顺序是：

1. 若 `OP.Pem_av_ref` 或 `OP.Pem_av_in` 有值，走 `solve_power`
2. 否则若 `OP.Tem_av_ref` 有值，走 `solve_torque`
3. 否则走 `solve_MTPA`

这意味着：

- 以前 `OPMatrix` 中的 `Tem_av_ref` 对 `ElecLUTdq` 实际上不生效
- 现在转矩工况可以直接通过 `VarLoadCurrent` 主流程批量运行

### 1.2 `solve_torque` 的求解策略

`solve_torque` 与 `solve_power` 共用一套 dq 网格细化思想：

- 在当前 `Id/Iq` 边界内生成细化网格
- 由 LUT 插值得到 `Phid/Phiq`
- 计算 `Ud/Uq`、电流约束、电压约束
- 计算 `Tem`
- 在满足目标转矩的候选点里选“最小电流点”
- 若目标不可达，逐级回退到：
  - 仅满足电压
  - 仅满足电流
  - 同方向最接近目标转矩

支持：

- 正转矩
- 负转矩（再生区）
- `P_in / P_out / efficiency / Ud / Uq / Id / Iq / Ld / Lq / torque ripple` 输出

## 2. 新增执行器

新增目录：

- `pyleecan/Functions/Simulation/LUTdq/`

其中包含五个直接可用入口。

### 2.1 `run_op_matrix_lut`

最底层通用执行器。

功能：

- 复制输入 `simu`
- 若缺少 `var_simu`，自动补一个 `VarLoadCurrent`
- 打开 `is_keep_all_output`
- 将 `OPMatrix` 挂入现有 `VarLoadCurrent`
- 直接调用 `simu.run()`

适合：

- 任意离散工况批量计算
- 后续继续扩展参数扫描、标定点、热边界批处理

### 2.2 `run_drive_cycle_lut`

drive cycle 正式执行入口。

调用链：

1. `read_drive_cycle_csv`
2. `build_drive_cycle_op_matrix`
3. `run_op_matrix_lut`
4. `summarize_drive_cycle_outputs`

因此现在支持：

- `target="torque"`
- `target="power_out"`
- `target="power_in"`

并且输出中直接带：

- `xoutput`
- `OP_matrix`
- `metadata`
- `summary`

### 2.3 `run_efficiency_map_lut`

效率 map 工程化入口。

流程分两步：

1. 先对给定 `speed_vect` 做一次满载 MTPA 扫描，得到每个转速点的 `Tem_max`
2. 再将 `load_vect` 转换成每个转速点对应的目标转矩矩阵，批量走 `Tem_av_ref` 求解

这样得到的不是验证脚本里的临时数组，而是一套可复用结果结构：

- `speed`
- `load`
- `Tem_max`
- `Tem_av_ref`
- `Tem_av`
- `efficiency`
- `P_out / P_in`
- `Id / Iq / Ud / Uq`
- `I_rms / U_rms`
- `xoutput`
- `OP_matrix`

另外，这个执行器现在支持直接输出缓存文件和图表文件：

- `cache_path=...`
- `plot_dir=...`
- `file_prefix=...`
- `is_show_fig=False`

### 2.4 `save_efficiency_map_cache / load_efficiency_map_cache`

用于把效率 map 结果落成可重复加载的本地缓存。

当前缓存格式为两部分：

- `*.npz`
  保存所有数值矩阵与向量
- `*.json`
  保存缓存格式版本、生成时间、数组键名、维度信息

缓存里包含的核心数组有：

- `speed / load`
- `Tem_max`
- `Tem_av_ref / Tem_av`
- `efficiency`
- `P_out / P_in`
- `Id / Iq / Ud / Uq`
- `I_rms / U_rms`
- `full_load.*`

注意：

- 这里缓存的是工程结果数组，不是完整 `xoutput`
- 这样文件更轻，更适合后续反复读取、画图、做报表

### 2.5 `plot_efficiency_map`

用于把效率 map 结果输出成标准 PNG 图。

当前默认输出 5 张图：

- `*_torque_envelope.png`
- `*_power_envelope.png`
- `*_efficiency_map.png`
- `*_current_map.png`
- `*_voltage_map.png`

图表坐标基准为：

- 横轴：转速 `N0`
- 纵轴：输出转矩 `Tem_av`
- 色图：效率、电流、电压等目标量

## 3. 推荐调用方式

### 3.1 Drive cycle

```python
from pyleecan.Functions.Simulation.DriveCycle import read_drive_cycle_csv
from pyleecan.Functions.Simulation.LUTdq import run_drive_cycle_lut

trajectory = read_drive_cycle_csv(
    "drive_cycle.csv",
    column_map={
        "time": "time_s",
        "N0": "speed_rpm",
        "Tem_av": "torque_nm",
    },
)

result = run_drive_cycle_lut(simu, trajectory, target="torque")
summary = result["summary"]
```

### 3.2 Efficiency map

```python
import numpy as np

from pyleecan.Functions.Simulation.LUTdq import (
    load_efficiency_map_cache,
    run_efficiency_map_lut,
)

result = run_efficiency_map_lut(
    simu,
    speed_vect=np.linspace(500, 6000, 30),
    load_vect=np.linspace(0, 1, 7),
    cache_path="Output/efficiency_map/toyota_prius",
    plot_dir="Output/efficiency_map/plots",
    file_prefix="toyota_prius",
)

eta_map = result["efficiency"]
torque_map = result["Tem_av"]
cache_paths = result["cache_paths"]
plot_paths = result["plot_paths"]

loaded = load_efficiency_map_cache(cache_paths["npz_path"])
eta_map_cached = loaded["efficiency"]
```

### 3.3 无外部求解器 demo

仓库现在提供一个轻量展示脚本，使用解析型 `LUTdq`，不依赖 FEMM / Elmer：

```powershell
python Tutorials\run_lutdq_efficiency_map_demo.py
```

默认输出到：

- `.local/lutdq_demo/lutdq_demo.npz`
- `.local/lutdq_demo/lutdq_demo.json`
- `.local/lutdq_demo/summary.json`
- `.local/lutdq_demo/*_map.png`
- `.local/lutdq_demo/*_envelope.png`

可用参数包括：

- `--output-dir`
- `--speed-count`
- `--load-count`
- `--file-prefix`
- `--no-plot`
- `--show-fig`

## 4. 当前工程边界

这轮已经解决的是“主流程接通”，不是“全栈动态仿真完成”。

当前仍然保留的边界有：

- 还没有做标准 WLTP / CLTC / NEDC 工况模板库
- 还没有做长工况分箱、压缩和批量并发优化
- 还没有做 `Udc / 温度 / 冷却` 对每一步的闭环修正
- 还没有做基于热状态的在线 LUT 切换
- 还没有做效率 map 自动落图库、缓存和 GUI 入口

但从架构上讲，后续已经不需要再绕开主流程；只要继续围绕：

- `DriveCycle.read/build/summarize`
- `LUTdq.run_*`
- `ElecLUTdq.solve_*`

逐步扩展即可。
