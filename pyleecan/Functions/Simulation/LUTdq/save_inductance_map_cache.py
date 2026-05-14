import json
from datetime import datetime, timezone
from os import makedirs
from os.path import abspath, dirname, exists

import numpy as np

from .save_efficiency_map_cache import _resolve_cache_paths


def save_inductance_map_cache(result, save_path):
    """Persist a dq inductance-map result to a local cache."""

    npz_path, json_path = _resolve_cache_paths(save_path)
    cache_dir = dirname(npz_path)
    if cache_dir and not exists(cache_dir):
        makedirs(cache_dir)

    array_keys = [
        "speed_rpm",
        "Id_axis",
        "Iq_axis",
        "Id_grid",
        "Iq_grid",
        "Phid",
        "Phiq",
        "Ld",
        "Lq",
        "Phi_dqh_mag",
    ]
    cache_arrays = {key: np.asarray(result[key]) for key in array_keys if key in result}
    np.savez_compressed(npz_path, **cache_arrays)

    metadata = {
        "cache_format": "pyleecan_inductance_map_npz",
        "cache_version": 1,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "speed_rpm": float(np.asarray(result["speed_rpm"]).reshape(())),
        "id_count": int(np.asarray(result["Id_axis"]).size),
        "iq_count": int(np.asarray(result["Iq_axis"]).size),
        "array_keys": array_keys,
    }

    with open(json_path, "w", encoding="utf-8") as metadata_file:
        json.dump(metadata, metadata_file, indent=2, sort_keys=True)

    return {"npz_path": abspath(npz_path), "json_path": abspath(json_path)}
