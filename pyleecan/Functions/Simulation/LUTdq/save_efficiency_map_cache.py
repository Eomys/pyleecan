import json
from datetime import datetime, timezone
from os.path import abspath, dirname, exists, splitext
from os import makedirs

import numpy as np

from ._utils import LOSS_SERIES_KEYS


def _resolve_cache_paths(save_path):
    """Return normalized npz/json paths for an efficiency-map cache."""

    base_path, extension = splitext(save_path)
    if extension.lower() == ".npz":
        npz_path = save_path
        base_path = base_path
    elif extension == "":
        npz_path = save_path + ".npz"
    else:
        npz_path = save_path + ".npz"
        base_path = save_path

    json_path = base_path + ".json"
    return abspath(npz_path), abspath(json_path)


def save_efficiency_map_cache(result, save_path):
    """Persist an efficiency-map result to a reusable local cache.

    Parameters
    ----------
    result : dict
        Result returned by ``run_efficiency_map_lut``.
    save_path : str
        Target cache path. ``.npz`` is appended if omitted.

    Returns
    -------
    paths : dict
        Absolute paths of the generated ``npz`` and ``json`` files.
    """

    npz_path, json_path = _resolve_cache_paths(save_path)
    cache_dir = dirname(npz_path)
    if cache_dir and not exists(cache_dir):
        makedirs(cache_dir)

    array_keys = [
        "speed",
        "load",
        "N0",
        "load_grid",
        "Tem_max",
        "Tem_av_ref",
        "Tem_av",
        "efficiency",
        "P_out",
        "P_in",
        "Id",
        "Iq",
        "Ud",
        "Uq",
        "I_rms",
        "U_rms",
        "Ld",
        "Lq",
        "control_region",
        "control_region_code",
        "voltage_limited_mask",
        "current_limited_mask",
        "full_load_control_region",
        "full_load_control_region_code",
        "full_load_voltage_limited_mask",
        "full_load_current_limited_mask",
    ]
    loss_keys = [key for key in LOSS_SERIES_KEYS if key in result]
    array_keys.extend(loss_keys)

    cache_arrays = dict()
    for key in array_keys:
        if key in result:
            cache_arrays[key] = np.asarray(result[key])

    full_load = result.get("full_load", {})
    full_load_keys = []
    if isinstance(full_load, dict):
        for key, values in full_load.items():
            if isinstance(values, np.ndarray):
                cache_key = "full_load__" + key
                cache_arrays[cache_key] = np.asarray(values)
                full_load_keys.append(key)

    np.savez_compressed(npz_path, **cache_arrays)

    metadata = {
        "cache_format": "pyleecan_efficiency_map_npz",
        "cache_version": 3,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "speed_count": int(np.asarray(result["speed"]).size),
        "load_count": int(np.asarray(result["load"]).size),
        "base_speed_rpm": (
            None
            if "base_speed_rpm" not in result
            or not np.isfinite(result["base_speed_rpm"])
            else float(result["base_speed_rpm"])
        ),
        "array_keys": array_keys,
        "full_load_keys": full_load_keys,
        "loss_keys": loss_keys,
    }

    with open(json_path, "w", encoding="utf-8") as metadata_file:
        json.dump(metadata, metadata_file, indent=2, sort_keys=True)

    return {"npz_path": npz_path, "json_path": json_path}
