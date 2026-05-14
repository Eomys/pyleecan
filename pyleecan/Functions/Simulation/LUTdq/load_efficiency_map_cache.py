import json
from os.path import abspath, exists, splitext

import numpy as np

from .save_efficiency_map_cache import _resolve_cache_paths


def load_efficiency_map_cache(load_path):
    """Load an efficiency-map cache created by ``save_efficiency_map_cache``."""

    npz_path, json_path = _resolve_cache_paths(load_path)
    if not exists(npz_path):
        raise FileNotFoundError(npz_path)

    with np.load(npz_path) as cache_file:
        result = {key: cache_file[key] for key in cache_file.files}

    full_load = dict()
    for key in list(result.keys()):
        if key.startswith("full_load__"):
            full_load[key.split("__", 1)[1]] = result.pop(key)
    if full_load:
        result["full_load"] = full_load

    if exists(json_path):
        with open(json_path, "r", encoding="utf-8") as metadata_file:
            result["metadata"] = json.load(metadata_file)
    else:
        result["metadata"] = None

    result["cache_paths"] = {"npz_path": abspath(npz_path), "json_path": abspath(json_path)}
    return result
