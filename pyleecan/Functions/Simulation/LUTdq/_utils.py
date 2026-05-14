import numpy as np

from ....Classes.VarLoadCurrent import VarLoadCurrent


CONTROL_REGION_TO_CODE = {
    "UNKNOWN": -1,
    "MTPA": 0,
    "FW": 1,
    "MTPV": 2,
}


def as_float_array(values, name):
    """Convert a sequence to a 1D float ndarray."""

    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError(f"{name} must be a 1D sequence, got shape {array.shape}")
    if array.size == 0:
        raise ValueError(f"{name} cannot be empty")
    return array


def prepare_lut_varload_simu(simu, op_matrix):
    """Copy a simulation, attach a VarLoadCurrent and set its OP matrix."""

    simu_step = simu.copy()
    if simu_step.var_simu is None:
        simu_step.var_simu = VarLoadCurrent(is_keep_all_output=True)
    elif not hasattr(simu_step.var_simu, "set_OP_array"):
        raise TypeError("simu.var_simu must expose set_OP_array to run LUT sweeps")

    simu_step.var_simu.is_keep_all_output = True
    simu_step.var_simu.set_OP_array(op_matrix, is_update_input=True, input_index=0)

    return simu_step


def get_lut_axes(lut):
    """Return the speed and dq current axes embedded in a LUT."""

    op_array = lut.get_OP_array("N0", "Id", "Iq")
    speed_vect = np.unique(np.asarray(op_array[:, 0], dtype=float))
    id_vect = np.unique(np.asarray(op_array[:, 1], dtype=float))
    iq_vect = np.unique(np.asarray(op_array[:, 2], dtype=float))
    return speed_vect, id_vect, iq_vect


def get_or_build_lut(simu):
    """Return a reusable LUT, building it from the simulation when needed."""

    elec = getattr(simu, "elec", None)
    if elec is None:
        raise TypeError("simu must expose an elec object")

    if elec.LUT_enforced is not None:
        return elec.LUT_enforced, simu

    input_obj = getattr(simu, "input", None)
    op = getattr(input_obj, "OP", None) if input_obj is not None else None
    speed = getattr(op, "N0", None) if op is not None else None
    if speed is None:
        raise ValueError(
            "simu.input.OP.N0 must be defined to build a LUT when no LUT_enforced is available"
        )

    from ....Classes.OPMatrix import OPMatrix
    from .run_op_matrix_lut import run_op_matrix_lut

    warmup_result = run_op_matrix_lut(
        simu,
        OPMatrix(N0=np.array([float(speed)]), col_names=["N0"]),
    )
    return warmup_result["simu"].elec.LUT_enforced, warmup_result["simu"]


def compute_limit_masks(
    I_rms,
    U_rms,
    Irms_max=None,
    Urms_max=None,
    current_tol=0.02,
    voltage_tol=0.02,
):
    """Return current-limited and voltage-limited masks from rms quantities."""

    I_rms = np.asarray(I_rms, dtype=float)
    U_rms = np.asarray(U_rms, dtype=float)
    I_rms, U_rms = np.broadcast_arrays(I_rms, U_rms)

    current_limited = np.zeros(I_rms.shape, dtype=bool)
    voltage_limited = np.zeros(U_rms.shape, dtype=bool)

    if Irms_max is not None and np.isfinite(Irms_max) and Irms_max > 0:
        current_limited = np.isfinite(I_rms) & (
            I_rms >= (1.0 - current_tol) * float(Irms_max)
        )
    if Urms_max is not None and np.isfinite(Urms_max) and Urms_max > 0:
        voltage_limited = np.isfinite(U_rms) & (
            U_rms >= (1.0 - voltage_tol) * float(Urms_max)
        )

    return current_limited, voltage_limited


def classify_control_regions(
    I_rms,
    U_rms,
    Irms_max=None,
    Urms_max=None,
    current_tol=0.02,
    voltage_tol=0.02,
):
    """Classify operating points into MTPA, FW or MTPV regions."""

    I_rms = np.asarray(I_rms, dtype=float)
    U_rms = np.asarray(U_rms, dtype=float)
    I_rms, U_rms = np.broadcast_arrays(I_rms, U_rms)

    regions = np.full(I_rms.shape, "UNKNOWN", dtype="<U7")
    valid = np.isfinite(I_rms) | np.isfinite(U_rms)
    if not np.any(valid):
        return regions

    current_limited, voltage_limited = compute_limit_masks(
        I_rms,
        U_rms,
        Irms_max=Irms_max,
        Urms_max=Urms_max,
        current_tol=current_tol,
        voltage_tol=voltage_tol,
    )

    regions[valid] = "MTPA"
    regions[voltage_limited & current_limited] = "FW"
    regions[voltage_limited & ~current_limited] = "MTPV"
    return regions


def encode_control_regions(regions):
    """Encode region labels into integer map values."""

    regions = np.asarray(regions)
    codes = np.full(regions.shape, CONTROL_REGION_TO_CODE["UNKNOWN"], dtype=int)
    for region, code in CONTROL_REGION_TO_CODE.items():
        codes[regions == region] = code
    return codes


def compute_base_speed(speed, regions):
    """Return the first speed at which the full-load envelope leaves MTPA."""

    speed = np.asarray(speed, dtype=float)
    regions = np.asarray(regions)

    if speed.ndim != 1 or regions.ndim != 1 or speed.size != regions.size:
        raise ValueError("speed and regions must be 1D arrays with identical sizes")

    limited_index = np.where(regions != "MTPA")[0]
    if limited_index.size == 0:
        return np.nan
    return float(speed[limited_index[0]])


def extract_output_series(outputs):
    """Extract per-step electrical quantities from a XOutput or output list."""

    if hasattr(outputs, "output_list"):
        output_list = list(outputs.output_list)
    elif isinstance(outputs, (list, tuple)):
        output_list = list(outputs)
    else:
        raise TypeError("outputs must be a XOutput, list, or tuple of Output objects")

    step_count = len(output_list)
    data = {
        "N0": np.full(step_count, np.nan),
        "Tem_av_ref": np.full(step_count, np.nan),
        "Tem_av": np.full(step_count, np.nan),
        "P_out": np.full(step_count, np.nan),
        "P_in": np.full(step_count, np.nan),
        "efficiency": np.full(step_count, np.nan),
        "Id": np.full(step_count, np.nan),
        "Iq": np.full(step_count, np.nan),
        "Ud": np.full(step_count, np.nan),
        "Uq": np.full(step_count, np.nan),
        "I_rms": np.full(step_count, np.nan),
        "U_rms": np.full(step_count, np.nan),
        "Ld": np.full(step_count, np.nan),
        "Lq": np.full(step_count, np.nan),
    }

    for idx, output in enumerate(output_list):
        elec = getattr(output, "elec", None)
        op = getattr(elec, "OP", None) if elec is not None else None
        eec = getattr(elec, "eec", None) if elec is not None else None

        if op is not None:
            data["N0"][idx] = getattr(op, "N0", np.nan)
            data["Tem_av_ref"][idx] = getattr(op, "Tem_av_ref", np.nan)
            data["efficiency"][idx] = getattr(op, "efficiency", np.nan)
            data["Id"][idx] = getattr(op, "Id_ref", np.nan)
            data["Iq"][idx] = getattr(op, "Iq_ref", np.nan)
            data["Ud"][idx] = getattr(op, "Ud_ref", np.nan)
            data["Uq"][idx] = getattr(op, "Uq_ref", np.nan)

        if elec is not None:
            data["Tem_av"][idx] = getattr(elec, "Tem_av", np.nan)
            data["P_out"][idx] = getattr(elec, "P_out", np.nan)
            data["P_in"][idx] = getattr(elec, "P_in", np.nan)
        if eec is not None:
            data["Ld"][idx] = getattr(eec, "Ld", np.nan)
            data["Lq"][idx] = getattr(eec, "Lq", np.nan)

        if np.isfinite(data["Id"][idx]) and np.isfinite(data["Iq"][idx]):
            data["I_rms"][idx] = float(
                np.sqrt(data["Id"][idx] ** 2 + data["Iq"][idx] ** 2)
            )
        if np.isfinite(data["Ud"][idx]) and np.isfinite(data["Uq"][idx]):
            data["U_rms"][idx] = float(
                np.sqrt(data["Ud"][idx] ** 2 + data["Uq"][idx] ** 2)
            )
        if (
            not np.isfinite(data["efficiency"][idx])
            and np.isfinite(data["P_in"][idx])
            and data["P_in"][idx] != 0
        ):
            data["efficiency"][idx] = data["P_out"][idx] / data["P_in"][idx]

    return data
