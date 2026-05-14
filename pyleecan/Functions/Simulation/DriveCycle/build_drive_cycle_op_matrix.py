from ....Classes.OPMatrix import OPMatrix
from ._utils import validate_trajectory_dict


def build_drive_cycle_op_matrix(trajectory, target="torque"):
    """Build an OPMatrix from a drive-cycle trajectory.

    Parameters
    ----------
    trajectory : dict
        Dictionary containing at least ``time`` and ``N0`` and either ``Tem_av``
        or ``Pem_av``.
    target : str
        ``torque`` to use ``Tem_av`` as the reference,
        ``power_out`` to use ``Pem_av`` as output power,
        ``power_in`` to use ``Pem_av`` as input power.

    Returns
    -------
    OP_matrix : OPMatrix
        Operating-point matrix ready to be consumed by existing VarLoad flows.
    metadata : dict
        Auxiliary trajectory metadata required by higher-level drive-cycle tools.
    """

    data = validate_trajectory_dict(trajectory, require_target=True)

    if target not in ("torque", "power_out", "power_in"):
        raise ValueError(
            "target must be one of 'torque', 'power_out', or 'power_in'"
        )

    op_matrix = OPMatrix(N0=data["N0"], is_output_power=(target != "power_in"))

    if target == "torque":
        if "Tem_av" not in data:
            raise ValueError("trajectory must contain Tem_av for torque targets")
        op_matrix.Tem_av_ref = data["Tem_av"]
        op_matrix.col_names = ["N0", "Tem_av"]
    else:
        if "Pem_av" not in data:
            raise ValueError("trajectory must contain Pem_av for power targets")
        op_matrix.Pem_av_ref = data["Pem_av"]
        op_matrix.col_names = ["N0", "Pem_av"]

    metadata = {
        "time": data["time"],
        "duration": float(data["time"][-1] - data["time"][0])
        if data["time"].size > 1
        else 0.0,
        "step_count": int(data["time"].size),
        "target": target,
    }

    if data["time"].size > 1:
        metadata["dt_mean"] = float((data["time"][1:] - data["time"][:-1]).mean())
    else:
        metadata["dt_mean"] = 0.0

    for key in ("Udc", "T_amb", "T_coolant"):
        if key in data:
            metadata[key] = data[key]

    return op_matrix, metadata
