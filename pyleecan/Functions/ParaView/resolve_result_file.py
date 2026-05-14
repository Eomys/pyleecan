from glob import glob
from os.path import abspath, exists, isdir, isfile, join


def resolve_result_file(result_path, latest_only=True):
    """Resolve a VTK/VTU result path from a file or a result directory."""

    if result_path is None:
        raise ValueError("result_path cannot be None")

    path_value = abspath(str(result_path))
    if isfile(path_value):
        if path_value.lower().endswith((".vtu", ".vtk")):
            return path_value
        raise ValueError(f"Unsupported ParaView result file: {path_value}")

    if not isdir(path_value):
        raise FileNotFoundError(f"ParaView result path not found: {path_value}")

    candidate_list = []
    for pattern in ["step_t*.vtu", "step_t*.vtk", "*.vtu", "*.vtk"]:
        candidate_list.extend(sorted(glob(join(path_value, pattern))))

    candidate_list = sorted(set(candidate_list))
    if not candidate_list:
        raise FileNotFoundError(
            f"No VTU/VTK result file was found in directory: {path_value}"
        )

    if latest_only:
        return abspath(candidate_list[-1])

    return abspath(candidate_list[0])

