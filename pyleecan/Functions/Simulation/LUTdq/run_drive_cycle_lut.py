from ..DriveCycle.build_drive_cycle_op_matrix import build_drive_cycle_op_matrix
from ..DriveCycle.summarize_drive_cycle_outputs import summarize_drive_cycle_outputs
from .run_op_matrix_lut import run_op_matrix_lut


def run_drive_cycle_lut(simu, trajectory, target="torque"):
    """Run a drive cycle through the existing LUT + VarLoadCurrent main flow."""

    op_matrix, metadata = build_drive_cycle_op_matrix(trajectory, target=target)
    result = run_op_matrix_lut(simu, op_matrix)

    summary = summarize_drive_cycle_outputs(result["xoutput"], metadata["time"])
    summary.update(metadata)
    result["metadata"] = metadata
    result["summary"] = summary

    return result
