# Nissan Leaf 2012 仿真验证总结

## 1. 输入与目标

本轮验证基于以下输入开展：

- 几何输入：`SimulationModels/Nissan_Leaf_2012/leaf.dxf`
- 当前机型 JSON：`SimulationModels/Nissan_Leaf_2012/Nissan_Leaf_2012_DXF.json`
- 模板机型：`SimulationModels/Toyota_Prius_2004/IPMSM_Toyota_Prius_2004.json`
- 公开参考：ORNL / DOE 关于 2012 Nissan Leaf 电机的拆解和性能公开数据

验证目标分三步推进：

1. 用 DXF 重建 Leaf 2012 电机几何，并验证几何尺寸是否与公开数据一致。
2. 在保持 8 线程 FEMM 流程的前提下，校准功率包络、转矩包络、效率图和动态负载结果。
3. 进一步调整 rotor pocket 中磁钢/空腔解释，优先同时逼近公开的 `443 Arms` 峰值电流点和 `4000 rpm` 左右弱磁起点。

## 2. 几何重建结论

DXF 重建后的几何与公开数据基本一致：

- 定子外径：`198.0 mm`，公开值 `198.12 mm`
- 定子内径：`131.0 mm`，公开值 `130.96 mm`
- 转子外径：`130.0 mm`，公开值 `129.97 mm`
- 轴径：`44.45 mm`，与公开值一致
- 叠长、槽极配比、匝数、并联支路、股数均与公开值一致或极接近

结论：几何本身不是主要误差来源。

## 3. 三轮验证结果

### Round 1：直接几何重建

建模假设：

- 两个 rotor pocket 闭环都按磁钢处理
- 直接使用模板机型的材料和电压电流边界

主要结果：

- 峰值转矩：`374.6 Nm`
- 峰值功率：`270.6 kW`
- `3000 rpm` 功率：`125.2 kW`
- 弱磁起点：`7000 rpm`

结论：

- 几何匹配很好
- 电磁性能明显高估
- 说明仅凭图纸直接套模板参数，不能复现公开 Leaf 包络

### Round 2：等效约束标定

标定目标：

- 优先逼近公开的 `280 Nm / 80 kW` 功率转矩包络

最佳候选：

- `Irms_max = 300 Arms`
- `Urms_max = 105 V`
- `Br_scale = 1.0`

主要结果：

- 峰值转矩：`277.3 Nm`
- 峰值功率：`85.65 kW`
- `3000 rpm` 功率：`83.08 kW`
- 高功率区峰值效率：`96.11%`
- 峰值转矩电流：`300 Arms`
- 弱磁起点：`3000 rpm`

结论：

- 功率与转矩包络已经接近公开数据
- 但 `443 Arms` 电流点没有复现
- 弱磁起点依旧提前到 `3000 rpm`

### Round 3：rotor pocket 重分配

重分配思路：

- 将外层 pocket 解释为磁钢
- 将内层 pocket 解释为空腔
- 再在此基础上重新标定 `Irms / Urms / Br`

最终最佳候选：

- `surface_roles = magnet, void`
- `Irms_max = 443 Arms`
- `Urms_max = 110 V`
- `Br_scale = 0.85`

主要结果：

- 峰值转矩：`332.2 Nm`
- 峰值功率：`91.41 kW`
- `3000 rpm` 功率：`91.41 kW`
- `3000 rpm` 静态点：`89.73 kW / 285.62 Nm / 92.62%`
- 峰值转矩电流：`442.999 Arms`
- 弱磁起点：`3000 rpm`
- 高功率区峰值效率：`95.08%`

结论：

- `443 Arms` 这个公开电流点已经可以被精确复现
- 但 `4000 rpm` 弱磁起点依旧没有拉回，仍然在 `3000 rpm`
- 同时峰值转矩和 `3000 rpm` 功率又再次偏大

## 4. 综合判断

当前验证已经把问题边界缩小得比较清楚：

- 几何尺寸重建是可信的
- 公开功率转矩包络可以通过等效约束标定逼近
- 公开 `443 Arms` 电流点也可以通过 rotor pocket 重解释逼近
- 但是在当前简化建模下，`443 Arms` 和 `4000 rpm` 弱磁起点还不能同时成立

这意味着误差更可能来自以下因素的组合，而不是单一参数偏差：

- rotor pocket 内部并非简单的“整块磁钢”或“整块空腔”
- 磁钢实际分布、磁桥、空腔以及局部材料区域需要更细粒度建模
- 公开电流口径与当前 `I_rms` 定义可能存在 RMS / peak / line-current 解释差异
- 真实逆变器电压边界和材料参数仍有不确定性

## 5. 后续建议

下一轮如果继续做，建议不再做粗粒度 `Irms / Urms / Br` 扫描，而是优先做以下工作：

1. 把外层 rotor pocket 进一步拆分成“局部磁钢 + 局部空腔 + 磁桥”结构。
2. 针对 `3000 rpm` 到 `4000 rpm` 的控制区切换单独做高分辨率扫描。
3. 明确 ORNL 公开 `443 Arms` 的定义口径，确认是否与当前模型输出完全同义。

## 6. 本地结果位置

本次验证的本地脚本、图表和汇总数据保存在：

- 当前提交到仓库的机型快照：`SimulationModels/Nissan_Leaf_2012/Nissan_Leaf_2012_DXF.json`
- `.local/verification/leaf_full_validation/`
- `.local/verification/leaf_full_validation/calibrated_8thread/`
- `.local/verification/leaf_full_validation/rotor_reallocated_8thread/`

这些结果用于本地复现和审查，没有作为仓库跟踪产物提交。
