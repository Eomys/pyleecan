import json
from os.path import abspath, exists

import numpy as np

from .save_efficiency_map_cache import _resolve_cache_paths


def load_inductance_map_cache(load_path):
    """Load a dq inductance-map cache created by ``save_inductance_map_cache``."""

    npz_path, json_path = _resolve_cache_paths(load_path)
    if not exists(npz_path):
        raise FileNotFoundError(npz_path)

    with np.load(npz_path) as cache_file:
        result = {key: cache_file[key] for key in cache_file.files}

    if exists(json_path):
        with open(json_path, "r", encoding="utf-8") as metadata_file:
            result["metadata"] = json.load(metadata_file)
    else:
        result["metadata"] = None

    result["cache_paths"] = {
        "npz_path": abspath(npz_path),
        "json_path": abspath(json_path),
    }
    return result
