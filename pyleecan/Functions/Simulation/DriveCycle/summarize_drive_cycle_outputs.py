import numpy as np

from ._utils import integrate_series, validate_trajectory_dict


def _coerce_output_list(outputs):
    """Return a flat list of Output objects."""

    if hasattr(outputs, "output_list"):
        return outputs.output_list
    if isinstance(outputs, (list, tuple)):
        return list(outputs)
    raise TypeError("outputs must be a XOutput, list, or tuple of Output objects")


def _get_rms_amplitude(op, current=True):
    """Extract an rms magnitude from an OP object."""

    if op is None:
        return np.nan

    if current:
        if hasattr(op, "get_I0_Phi0"):
            try:
                return float(op.get_I0_Phi0()["I0"])
            except Exception:
                pass
        d_value = getattr(op, "Id_ref", None)
        q_value = getattr(op, "Iq_ref", None)
    else:
        if hasattr(op, "get_U0_UPhi0"):
            try:
                return float(op.get_U0_UPhi0()["U0"])
            except Exception:
                pass
        d_value = getattr(op, "Ud_ref", None)
        q_value = getattr(op, "Uq_ref", None)

    if d_value is None or q_value is None:
        return np.nan
    return float(np.sqrt(d_value**2 + q_value**2))


def summarize_drive_cycle_outputs(outputs, time):
    """Summarize a list of operating-point outputs over a drive cycle.

    Parameters
    ----------
    outputs : XOutput | list[Output]
        Per-step outputs obtained from a variable-load workflow.
    time : array_like
        Time vector associated with the outputs.

    Returns
    -------
    summary : dict
        Arrays per operating point plus integrated cycle metrics.
    """

    output_list = _coerce_output_list(outputs)
    data = validate_trajectory_dict({"time": time, "N0": np.arange(len(output_list))})
    time_vect = data["time"]

    if len(output_list) != time_vect.size:
        raise ValueError("time and outputs must have the same number of samples")

    step_count = len(output_list)
    speed = np.full(step_count, np.nan)
    torque = np.full(step_count, np.nan)
    p_out = np.full(step_count, np.nan)
    p_in = np.full(step_count, np.nan)
    p_loss = np.full(step_count, np.nan)
    efficiency = np.full(step_count, np.nan)
    i_rms = np.full(step_count, np.nan)
    u_rms = np.full(step_count, np.nan)

    for idx, output in enumerate(output_list):
        elec = getattr(output, "elec", None)
        op = getattr(elec, "OP", None) if elec is not None else None

        if op is not None:
            speed[idx] = getattr(op, "N0", np.nan)

        if elec is not None:
            torque[idx] = getattr(elec, "Tem_av", np.nan)
            if not np.isfinite(torque[idx]) and op is not None:
                torque[idx] = getattr(op, "Tem_av_ref", np.nan)

            p_out[idx] = getattr(elec, "P_out", np.nan)
            if not np.isfinite(p_out[idx]) and np.isfinite(torque[idx]) and np.isfinite(
                speed[idx]
            ):
                p_out[idx] = torque[idx] * 2 * np.pi * speed[idx] / 60

            p_in[idx] = getattr(elec, "P_in", np.nan)
            efficiency[idx] = (
                getattr(op, "efficiency", np.nan) if op is not None else np.nan
            )
            i_rms[idx] = _get_rms_amplitude(op, current=True)
            u_rms[idx] = _get_rms_amplitude(op, current=False)

        if np.isfinite(p_in[idx]) and np.isfinite(p_out[idx]):
            p_loss[idx] = p_in[idx] - p_out[idx]
        else:
            loss = getattr(output, "loss", None)
            if loss is not None and hasattr(loss, "get_loss_overall"):
                try:
                    p_loss[idx] = float(loss.get_loss_overall())
                except Exception:
                    p_loss[idx] = np.nan
            if not np.isfinite(p_in[idx]) and np.isfinite(p_out[idx]) and np.isfinite(
                p_loss[idx]
            ):
                p_in[idx] = p_out[idx] + p_loss[idx]

        if not np.isfinite(efficiency[idx]) and np.isfinite(p_in[idx]) and p_in[idx] != 0:
            efficiency[idx] = p_out[idx] / p_in[idx]

    energy_out = integrate_series(time_vect, p_out)
    energy_in = integrate_series(time_vect, p_in)
    energy_loss = integrate_series(time_vect, p_loss)

    return {
        "time": time_vect,
        "N0": speed,
        "Tem_av": torque,
        "P_out": p_out,
        "P_in": p_in,
        "P_loss": p_loss,
        "efficiency": efficiency,
        "I_rms": i_rms,
        "U_rms": u_rms,
        "duration": float(time_vect[-1] - time_vect[0]) if step_count > 1 else 0.0,
        "step_count": step_count,
        "invalid_step_count": int(np.count_nonzero(~np.isfinite(p_out) | ~np.isfinite(p_in))),
        "energy_out_J": energy_out,
        "energy_in_J": energy_in,
        "energy_loss_J": energy_loss,
        "eta_cycle": energy_out / energy_in
        if np.isfinite(energy_in) and energy_in != 0
        else np.nan,
        "max_speed_rpm": float(np.nanmax(speed)),
        "max_torque_Nm": float(np.nanmax(np.abs(torque))),
        "max_I_rms_A": float(np.nanmax(i_rms)),
        "max_U_rms_V": float(np.nanmax(u_rms)),
    }
