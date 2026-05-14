import subprocess

from ..get_path_binary import get_path_binary
from .resolve_result_file import resolve_result_file


def launch_paraview(result_path, executable=None, latest_only=True):
    """Launch the ParaView GUI on a result file."""

    resolved_file = resolve_result_file(result_path, latest_only=latest_only)
    executable_name = executable if executable is not None else "paraview"
    paraview_binary = get_path_binary(executable_name)
    if paraview_binary is None:
        raise FileNotFoundError(
            "ParaView executable not found. Set PARAVIEW_HOME/PYLEECAN_PARAVIEW "
            "or install ParaView in a standard Windows location."
        )

    return subprocess.Popen([paraview_binary, resolved_file])

