import numpy as np


DEFAULT_COLUMN_ALIASES = {
    "time": ("time", "time_s", "t"),
    "N0": ("N0", "speed", "speed_rpm", "rpm"),
    "Tem_av": ("Tem_av", "Tem_av_ref", "torque", "torque_nm"),
    "Pem_av": ("Pem_av", "Pem_av_ref", "power", "power_w"),
    "Udc": ("Udc", "udc", "udc_v", "voltage_dc"),
    "T_amb": ("T_amb", "Tamb", "t_amb", "ambient_temp"),
    "T_coolant": ("T_coolant", "Tcoolant", "t_coolant", "coolant_temp"),
}


def as_float_array(values, name):
    """Convert a sequence to a 1D float ndarray."""

    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError(f"{name} must be a 1D sequence, got shape {array.shape}")
    return array


def validate_trajectory_dict(trajectory, require_target=False):
    """Validate a drive-cycle trajectory dictionary and return numpy arrays."""

    if trajectory is None:
        raise ValueError("trajectory cannot be None")

    data = dict()
    for key, values in trajectory.items():
        data[key] = as_float_array(values, key)

    required = ["time", "N0"]
    if require_target and "Tem_av" not in data and "Pem_av" not in data:
        raise ValueError("trajectory must contain either Tem_av or Pem_av")

    missing = [key for key in required if key not in data]
    if missing:
        raise ValueError(
            "trajectory is missing required columns: " + ", ".join(missing)
        )

    lengths = {values.size for values in data.values()}
    if len(lengths) != 1:
        raise ValueError("All trajectory vectors must have the same length")

    if data["time"].size == 0:
        raise ValueError("trajectory cannot be empty")

    if data["time"].size > 1 and np.any(np.diff(data["time"]) <= 0):
        raise ValueError("trajectory time vector must be strictly increasing")

    return data


def integrate_series(time, values):
    """Integrate a sampled series while ignoring non-finite points."""

    mask = np.isfinite(time) & np.isfinite(values)
    if np.count_nonzero(mask) < 2:
        if np.count_nonzero(mask) == 1:
            return 0.0
        return np.nan

    if hasattr(np, "trapezoid"):
        return float(np.trapezoid(values[mask], time[mask]))
    return float(np.trapz(values[mask], time[mask]))
