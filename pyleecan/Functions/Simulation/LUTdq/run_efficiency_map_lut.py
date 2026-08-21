import numpy as np

from ....Classes.OPMatrix import OPMatrix
from ._utils import (
    LOSS_SERIES_KEYS,
    as_float_array,
    classify_control_regions,
    compute_base_speed,
    compute_limit_masks,
    encode_control_regions,
    extract_output_series,
)
from .run_op_matrix_lut import run_op_matrix_lut


def _reshape_map(data_dict, shape):
    """Reshape every 1D series in a result dict into a 2D speed/load map."""

    reshaped = dict()
    for key, values in data_dict.items():
        reshaped[key] = values.reshape(shape)
    return reshaped


def _check_finite_series(series, keys, context, expected_size):
    """Validate that required result series are present, sized and finite."""

    for key in keys:
        if key not in series:
            raise KeyError(f"{context} result is missing '{key}'")

        values = np.asarray(series[key], dtype=float)
        if values.size != expected_size:
            raise ValueError(
                f"{context} result '{key}' has {values.size} values, "
                f"expected {expected_size}"
            )
        if not np.all(np.isfinite(values)):
            bad_idx = np.where(~np.isfinite(values.ravel()))[0][:5]
            raise ValueError(
                f"{context} result '{key}' contains non-finite values at "
                f"flattened indices {bad_idx.tolist()}"
            )


def run_efficiency_map_lut(
    simu,
    speed_vect,
    load_vect,
    max_load_rate=1.0,
    cache_path=None,
    plot_dir=None,
    file_prefix="efficiency_map",
    is_show_fig=False,
):
    """Run a reusable LUT-based efficiency-map workflow.

    The workflow is:
    1. Solve the full-load envelope versus speed with the existing MTPA logic.
    2. Convert each load ratio into a torque request per speed.
    3. Re-run the sweep using explicit torque targets through ``Tem_av_ref``.
    """

    speed = as_float_array(speed_vect, "speed_vect")
    load = as_float_array(load_vect, "load_vect")

    if np.any(load < 0) or np.any(load > 1):
        raise ValueError("load_vect values must stay within [0, 1]")
    if max_load_rate < 0 or max_load_rate > 1:
        raise ValueError("max_load_rate must stay within [0, 1]")

    full_load_simu = simu.copy()
    full_load_simu.elec.load_rate = float(max_load_rate)
    full_load_result = run_op_matrix_lut(
        full_load_simu, OPMatrix(N0=speed, col_names=["N0"])
    )
    full_load_series = extract_output_series(full_load_result["xoutput"])
    _check_finite_series(
        full_load_series,
        (
            "Tem_av",
            "P_out",
            "P_in",
            "efficiency",
            "Id",
            "Iq",
            "Ud",
            "Uq",
            "I_rms",
            "U_rms",
        ),
        "full-load envelope",
        speed.size,
    )
    tem_max = full_load_series["Tem_av"]
    if np.any(tem_max < 0):
        raise ValueError("full-load envelope Tem_av must be non-negative")

    full_load_control_region = classify_control_regions(
        full_load_series["I_rms"],
        full_load_series["U_rms"],
        Irms_max=full_load_simu.elec.Irms_max,
        Urms_max=full_load_simu.elec.Urms_max,
    )
    full_load_current_limited, full_load_voltage_limited = compute_limit_masks(
        full_load_series["I_rms"],
        full_load_series["U_rms"],
        Irms_max=full_load_simu.elec.Irms_max,
        Urms_max=full_load_simu.elec.Urms_max,
    )
    base_speed_rpm = compute_base_speed(speed, full_load_control_region)

    lut_cache = full_load_result["simu"].elec.LUT_enforced
    if lut_cache is None:
        raise ValueError("run_efficiency_map_lut requires a generated or enforced LUT")

    speed_grid = np.repeat(speed, load.size)
    load_grid = np.tile(load, speed.size)
    torque_ref = np.repeat(tem_max, load.size) * load_grid

    torque_result_simu = simu.copy()
    torque_result_simu.elec.LUT_enforced = lut_cache
    torque_result = run_op_matrix_lut(
        torque_result_simu,
        OPMatrix(
            N0=speed_grid,
            Tem_av_ref=torque_ref,
            col_names=["N0", "Tem_av"],
        ),
    )
    map_series = extract_output_series(torque_result["xoutput"])
    _check_finite_series(
        map_series,
        (
            "Tem_av",
            "P_out",
            "P_in",
            "efficiency",
            "Id",
            "Iq",
            "Ud",
            "Uq",
            "I_rms",
            "U_rms",
        ),
        "torque map",
        speed_grid.size,
    )
    control_region = classify_control_regions(
        map_series["I_rms"],
        map_series["U_rms"],
        Irms_max=torque_result_simu.elec.Irms_max,
        Urms_max=torque_result_simu.elec.Urms_max,
    )
    current_limited_mask, voltage_limited_mask = compute_limit_masks(
        map_series["I_rms"],
        map_series["U_rms"],
        Irms_max=torque_result_simu.elec.Irms_max,
        Urms_max=torque_result_simu.elec.Urms_max,
    )

    map_shape = (speed.size, load.size)
    map_data = _reshape_map(map_series, map_shape)

    loss_maps = {}
    for key in LOSS_SERIES_KEYS:
        values = map_series.get(key)
        if values is None:
            continue
        if np.any(np.isfinite(values)):
            loss_maps[key] = np.asarray(values, dtype=float).reshape(map_shape)

    result = {
        "speed": speed,
        "load": load,
        "N0": speed[:, None] * np.ones((1, load.size)),
        "load_grid": np.ones((speed.size, 1)) * load[None, :],
        "Tem_max": tem_max,
        "Tem_av_ref": torque_ref.reshape(map_shape),
        "Tem_av": map_data["Tem_av"],
        "efficiency": map_data["efficiency"],
        "P_out": map_data["P_out"],
        "P_in": map_data["P_in"],
        "Id": map_data["Id"],
        "Iq": map_data["Iq"],
        "Ud": map_data["Ud"],
        "Uq": map_data["Uq"],
        "I_rms": map_data["I_rms"],
        "U_rms": map_data["U_rms"],
        "Ld": map_data["Ld"],
        "Lq": map_data["Lq"],
        "control_region": control_region.reshape(map_shape),
        "control_region_code": encode_control_regions(control_region).reshape(
            map_shape
        ),
        "voltage_limited_mask": voltage_limited_mask.reshape(map_shape),
        "current_limited_mask": current_limited_mask.reshape(map_shape),
        "full_load_control_region": full_load_control_region,
        "full_load_control_region_code": encode_control_regions(
            full_load_control_region
        ),
        "full_load_voltage_limited_mask": full_load_voltage_limited,
        "full_load_current_limited_mask": full_load_current_limited,
        "base_speed_rpm": base_speed_rpm,
        "full_load": full_load_series,
        "LUT_enforced": lut_cache,
        "xoutput": torque_result["xoutput"],
        "OP_matrix": torque_result["OP_matrix"],
    }

    if loss_maps:
        result["loss_maps"] = loss_maps
        for key, values in loss_maps.items():
            result[key] = values

    if cache_path is not None:
        from .save_efficiency_map_cache import save_efficiency_map_cache

        result["cache_paths"] = save_efficiency_map_cache(result, cache_path)

    if plot_dir is not None:
        from .plot_efficiency_map import plot_efficiency_map

        result["plot_paths"] = plot_efficiency_map(
            result,
            plot_dir,
            file_prefix=file_prefix,
            is_show_fig=is_show_fig,
        )

    return result
