from os import remove
from os.path import abspath
from tempfile import NamedTemporaryFile
import subprocess

from ..get_path_binary import get_path_binary
from .build_paraview_render_script import build_paraview_render_script
from .resolve_result_file import resolve_result_file


def render_vtu_screenshot(
    result_path,
    array_name,
    output_path,
    component="Magnitude",
    time_index=-1,
    executable=None,
    image_size=(1600, 1200),
):
    """Render a ParaView screenshot from a VTU/VTK result file."""

    input_file = resolve_result_file(result_path, latest_only=True)
    output_file = abspath(str(output_path))

    if executable is not None:
        batch_binary = get_path_binary(executable)
    else:
        batch_binary = get_path_binary("pvpython")
        if batch_binary is None:
            batch_binary = get_path_binary("pvbatch")

    if batch_binary is None:
        raise FileNotFoundError(
            "pvpython/pvbatch executable not found. Set PARAVIEW_HOME, "
            "PYLEECAN_PVPYTHON or PYLEECAN_PVBATCH."
        )

    script_contents = build_paraview_render_script(
        input_path=input_file,
        array_name=array_name,
        output_path=output_file,
        component=component,
        time_index=time_index,
        image_size=image_size,
    )

    script_path = None
    try:
        with NamedTemporaryFile(
            mode="w",
            suffix=".py",
            encoding="utf-8",
            delete=False,
        ) as script_file:
            script_file.write(script_contents)
            script_path = script_file.name

        subprocess.run([batch_binary, script_path], check=True)
    finally:
        if script_path is not None:
            try:
                remove(script_path)
            except OSError:
                pass

    return output_file
