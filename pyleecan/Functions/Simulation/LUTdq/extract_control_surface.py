import numpy as np

from ._utils import (
    LOSS_SERIES_KEYS,
    classify_control_regions,
    compute_limit_masks,
    encode_control_regions,
)


_CURVE_KEYS = (
    "N0",
    "load",
    "Tem_av",
    "Id",
    "Iq",
    "I_rms",
    "U_rms",
    "efficiency",
    "P_out",
    "P_in",
    "voltage_margin",
    "current_margin",
    "loss_per_torque",
)


def _as_2d(result, key, shape=None, is_required=True):
    if key not in result:
        if is_required:
            raise KeyError(f"control-surface extraction requires '{key}'")
        return None

    values = np.asarray(result[key])
    if values.ndim != 2:
        raise ValueError(f"'{key}' must be a 2D map, got shape {values.shape}")
    if shape is not None and values.shape != shape:
        raise ValueError(f"'{key}' has shape {values.shape}, expected {shape}")
    return values


def _optional_2d(result, key, shape):
    values = _as_2d(result, key, shape=shape, is_required=False)
    if values is not None:
        return values

    loss_maps = result.get("loss_maps", {})
    if isinstance(loss_maps, dict) and key in loss_maps:
        values = np.asarray(loss_maps[key], dtype=float)
        if values.ndim != 2 or values.shape != shape:
            raise ValueError(
                f"loss_maps['{key}'] has shape {values.shape}, expected {shape}"
            )
        return values
    return None


def _speed_vector(result, n_speed):
    if "speed" in result:
        speed = np.asarray(result["speed"], dtype=float)
        if speed.ndim != 1 or speed.size != n_speed:
            raise ValueError(f"'speed' must be a 1D array of size {n_speed}")
        return speed

    n0_map = _as_2d(result, "N0", is_required=True)
    if n0_map.shape[0] != n_speed:
        raise ValueError("'N0' has an inconsistent speed axis")
    return np.asarray(n0_map[:, 0], dtype=float)


def _load_map(result, shape):
    if "load_grid" in result:
        return np.asarray(_as_2d(result, "load_grid", shape=shape), dtype=float)
    if "load" in result:
        load = np.asarray(result["load"], dtype=float)
        if load.ndim != 1 or load.size != shape[1]:
            raise ValueError(f"'load' must be a 1D array of size {shape[1]}")
        return np.ones((shape[0], 1)) * load[None, :]
    return np.full(shape, np.nan)


def _resolve_rms_map(result, direct_key, comp_keys, shape):
    values = _optional_2d(result, direct_key, shape)
    if values is not None:
        return np.asarray(values, dtype=float)

    first = _optional_2d(result, comp_keys[0], shape)
    second = _optional_2d(result, comp_keys[1], shape)
    if first is None or second is None:
        raise KeyError(
            f"control-surface extraction requires '{direct_key}' or "
            f"both '{comp_keys[0]}' and '{comp_keys[1]}'"
        )
    return np.sqrt(
        np.asarray(first, dtype=float) ** 2 + np.asarray(second, dtype=float) ** 2
    )


def _resolve_regions(
    result, I_rms, U_rms, Irms_max, Urms_max, current_tol, voltage_tol
):
    existing = result.get("control_region")
    if existing is not None:
        regions = np.asarray(existing)
        if regions.shape != I_rms.shape:
            raise ValueError(
                f"'control_region' has shape {regions.shape}, expected {I_rms.shape}"
            )
        return regions

    return classify_control_regions(
        I_rms,
        U_rms,
        Irms_max=Irms_max,
        Urms_max=Urms_max,
        current_tol=current_tol,
        voltage_tol=voltage_tol,
    )


def _resolve_masks(result, I_rms, U_rms, Irms_max, Urms_max, current_tol, voltage_tol):
    current_mask = result.get("current_limited_mask")
    voltage_mask = result.get("voltage_limited_mask")
    if current_mask is None or voltage_mask is None:
        return compute_limit_masks(
            I_rms,
            U_rms,
            Irms_max=Irms_max,
            Urms_max=Urms_max,
            current_tol=current_tol,
            voltage_tol=voltage_tol,
        )

    current_mask = np.asarray(current_mask, dtype=bool)
    voltage_mask = np.asarray(voltage_mask, dtype=bool)
    if current_mask.shape != I_rms.shape:
        raise ValueError(
            f"'current_limited_mask' has shape {current_mask.shape}, expected {I_rms.shape}"
        )
    if voltage_mask.shape != I_rms.shape:
        raise ValueError(
            f"'voltage_limited_mask' has shape {voltage_mask.shape}, expected {I_rms.shape}"
        )
    return current_mask, voltage_mask


def _select_argmax(score, mask):
    indices = np.full(score.shape[0], -1, dtype=int)
    for row in range(score.shape[0]):
        row_mask = mask[row] & np.isfinite(score[row])
        if np.any(row_mask):
            row_candidates = np.where(row_mask)[0]
            indices[row] = row_candidates[int(np.nanargmax(score[row, row_candidates]))]
    return indices


def _select_first(mask):
    indices = np.full(mask.shape[0], -1, dtype=int)
    for row in range(mask.shape[0]):
        row_candidates = np.where(mask[row])[0]
        if row_candidates.size:
            indices[row] = int(row_candidates[0])
    return indices


def _curve_from_indices(maps, regions, indices):
    n_speed = indices.size
    curve = {
        "index": indices.copy(),
        "control_region": np.full(n_speed, "UNKNOWN", dtype="<U7"),
    }

    for key, values in maps.items():
        if key not in LOSS_SERIES_KEYS and key not in _CURVE_KEYS:
            continue
        curve[key] = np.full(n_speed, np.nan)

    for row, col in enumerate(indices):
        if col < 0:
            continue
        curve["control_region"][row] = str(regions[row, col])
        for key, values in maps.items():
            if key in LOSS_SERIES_KEYS:
                curve[key][row] = values[row, col]
            elif key in _CURVE_KEYS:
                curve[key][row] = values[row, col]

    return curve


def extract_control_surface(
    result,
    Irms_max=None,
    Urms_max=None,
    current_tol=0.02,
    voltage_tol=0.02,
    loss_key="P_loss_total",
):
    """Extract MTPA, MTPV and field-weakening boundary curves from a LUT map.

    Parameters
    ----------
    result : dict
        Result returned by ``run_efficiency_map_lut`` or an equivalent dict of
        2D maps. Required keys are ``Tem_av``, ``Id``, ``Iq`` and either
        ``I_rms``/``U_rms`` or ``Id``/``Iq`` plus ``Ud``/``Uq``.
    Irms_max, Urms_max : float, optional
        Current and voltage limits used when ``result`` does not already carry
        ``current_limited_mask`` / ``voltage_limited_mask``.
    current_tol, voltage_tol : float
        Relative tolerances used to classify current and voltage limited cells.
    loss_key : str or None
        Loss map to carry into the selected curves. By default the M1 aggregate
        ``P_loss_total`` is used when available.

    Returns
    -------
    control_surface : dict
        Dict with ``mtpa``, ``mtpv`` and ``fw_boundary`` curve dictionaries.
        Each curve has one selected point per speed row; missing points have
        ``index == -1`` and NaN scalar values.
    """

    Tem_av = np.asarray(_as_2d(result, "Tem_av"), dtype=float)
    shape = Tem_av.shape
    if shape[0] == 0 or shape[1] == 0:
        raise ValueError("'Tem_av' cannot be empty")

    Id = np.asarray(_as_2d(result, "Id", shape=shape), dtype=float)
    Iq = np.asarray(_as_2d(result, "Iq", shape=shape), dtype=float)
    I_rms = _resolve_rms_map(result, "I_rms", ("Id", "Iq"), shape)
    U_rms = _resolve_rms_map(result, "U_rms", ("Ud", "Uq"), shape)

    speed = _speed_vector(result, shape[0])
    n0_map = _optional_2d(result, "N0", shape)
    if n0_map is None:
        n0_map = speed[:, None] * np.ones((1, shape[1]))
    load_map = _load_map(result, shape)

    regions = _resolve_regions(
        result,
        I_rms,
        U_rms,
        Irms_max,
        Urms_max,
        current_tol,
        voltage_tol,
    )
    current_limited, voltage_limited = _resolve_masks(
        result,
        I_rms,
        U_rms,
        Irms_max,
        Urms_max,
        current_tol,
        voltage_tol,
    )
    region_code = encode_control_regions(regions)

    valid = np.isfinite(Tem_av) & np.isfinite(I_rms) & np.isfinite(U_rms)
    positive_current = I_rms > np.finfo(float).eps
    positive_voltage = U_rms > np.finfo(float).eps

    mtpa_score = np.full(shape, np.nan)
    mtpa_score[positive_current] = Tem_av[positive_current] / I_rms[positive_current]
    mtpa_mask = valid & (regions == "MTPA") & positive_current
    if not np.any(mtpa_mask):
        mtpa_mask = valid & ~voltage_limited & positive_current
    mtpa_idx = _select_argmax(mtpa_score, mtpa_mask)

    mtpv_score = np.full(shape, np.nan)
    mtpv_score[positive_voltage] = Tem_av[positive_voltage] / U_rms[positive_voltage]
    mtpv_mask = valid & (regions == "MTPV") & positive_voltage
    mtpv_idx = _select_argmax(mtpv_score, mtpv_mask)

    fw_mask = valid & (voltage_limited | ((regions != "MTPA") & (regions != "UNKNOWN")))
    fw_idx = _select_first(fw_mask)

    maps = {
        "N0": np.asarray(n0_map, dtype=float),
        "load": load_map,
        "Tem_av": Tem_av,
        "Id": Id,
        "Iq": Iq,
        "I_rms": I_rms,
        "U_rms": U_rms,
        "efficiency": _optional_2d(result, "efficiency", shape),
        "P_out": _optional_2d(result, "P_out", shape),
        "P_in": _optional_2d(result, "P_in", shape),
        "voltage_margin": np.full(shape, np.nan),
        "current_margin": np.full(shape, np.nan),
    }

    if Urms_max is not None and np.isfinite(Urms_max) and Urms_max > 0:
        maps["voltage_margin"] = (float(Urms_max) - U_rms) / float(Urms_max)
    if Irms_max is not None and np.isfinite(Irms_max) and Irms_max > 0:
        maps["current_margin"] = (float(Irms_max) - I_rms) / float(Irms_max)

    if loss_key is not None:
        loss_map = _optional_2d(result, loss_key, shape)
        if loss_map is not None:
            loss_map = np.asarray(loss_map, dtype=float)
            maps[loss_key] = loss_map
            loss_per_torque = np.full(shape, np.nan)
            nonzero_torque = np.abs(Tem_av) > np.finfo(float).eps
            loss_per_torque[nonzero_torque] = loss_map[nonzero_torque] / np.abs(
                Tem_av[nonzero_torque]
            )
            maps["loss_per_torque"] = loss_per_torque

    for key in LOSS_SERIES_KEYS:
        if key == loss_key:
            continue
        values = _optional_2d(result, key, shape)
        if values is not None:
            maps[key] = np.asarray(values, dtype=float)

    maps = {key: values for key, values in maps.items() if values is not None}

    return {
        "speed": speed,
        "control_region": regions,
        "control_region_code": region_code,
        "current_limited_mask": current_limited,
        "voltage_limited_mask": voltage_limited,
        "base_speed_rpm": result.get("base_speed_rpm", np.nan),
        "loss_key": loss_key,
        "mtpa": _curve_from_indices(maps, regions, mtpa_idx),
        "mtpv": _curve_from_indices(maps, regions, mtpv_idx),
        "fw_boundary": _curve_from_indices(maps, regions, fw_idx),
    }
