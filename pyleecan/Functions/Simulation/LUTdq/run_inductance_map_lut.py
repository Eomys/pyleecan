import numpy as np

from ._utils import as_float_array, get_lut_axes, get_or_build_lut


def _resolve_axis(requested_axis, lut_axis, interp_count, name):
    """Return the axis used to sample the inductance map."""

    if requested_axis is not None:
        return as_float_array(requested_axis, name)

    lut_axis = np.asarray(lut_axis, dtype=float)
    if interp_count is None:
        return lut_axis

    interp_count = int(interp_count)
    if interp_count <= 0:
        raise ValueError(f"{name}_interp must be a positive integer")
    return np.linspace(float(lut_axis.min()), float(lut_axis.max()), interp_count)


def run_inductance_map_lut(
    simu,
    Id_vect=None,
    Iq_vect=None,
    n_Id_interp=None,
    n_Iq_interp=None,
    cache_path=None,
    plot_dir=None,
    file_prefix="inductance_map",
    is_show_fig=False,
):
    """Generate a reusable dq inductance map from an existing or freshly built LUT."""

    lut, simu_with_lut = get_or_build_lut(simu)
    speed_vect, lut_id_vect, lut_iq_vect = get_lut_axes(lut)
    if speed_vect.size != 1:
        raise ValueError(
            "run_inductance_map_lut expects a LUT built at a single speed, got "
            + str(speed_vect.size)
        )

    id_axis = _resolve_axis(Id_vect, lut_id_vect, n_Id_interp, "Id_vect")
    iq_axis = _resolve_axis(Iq_vect, lut_iq_vect, n_Iq_interp, "Iq_vect")

    Id_grid, Iq_grid = np.meshgrid(id_axis, iq_axis)
    Id_flat = Id_grid.ravel()
    Iq_flat = Iq_grid.ravel()

    Phi_dqh = lut.interp_Phi_dqh(Id_flat, Iq_flat)
    phi_mag = lut.get_Phi_dqh_mag_mean()
    if phi_mag is None:
        phi_mag = np.array([np.nan, np.nan, 0.0])
    else:
        phi_mag = np.asarray(phi_mag, dtype=float)

    Phid = np.asarray(Phi_dqh[0], dtype=float).reshape(Id_grid.shape)
    Phiq = np.asarray(Phi_dqh[1], dtype=float).reshape(Id_grid.shape)

    Ld = np.full(Id_grid.shape, np.nan)
    Lq = np.full(Iq_grid.shape, np.nan)
    id_mask = Id_grid != 0
    iq_mask = Iq_grid != 0
    if np.isfinite(phi_mag[0]):
        Ld[id_mask] = (Phid[id_mask] - phi_mag[0]) / Id_grid[id_mask]
    if np.isfinite(phi_mag[1]):
        Lq[iq_mask] = (Phiq[iq_mask] - phi_mag[1]) / Iq_grid[iq_mask]
    else:
        Lq[iq_mask] = Phiq[iq_mask] / Iq_grid[iq_mask]

    result = {
        "speed_rpm": float(speed_vect[0]),
        "Id_axis": id_axis,
        "Iq_axis": iq_axis,
        "Id_grid": Id_grid,
        "Iq_grid": Iq_grid,
        "Phid": Phid,
        "Phiq": Phiq,
        "Ld": Ld,
        "Lq": Lq,
        "Phi_dqh_mag": phi_mag,
        "LUT_enforced": lut,
        "simu": simu_with_lut,
    }

    if cache_path is not None:
        from .save_inductance_map_cache import save_inductance_map_cache

        result["cache_paths"] = save_inductance_map_cache(result, cache_path)

    if plot_dir is not None:
        from .plot_inductance_map import plot_inductance_map

        result["plot_paths"] = plot_inductance_map(
            result,
            plot_dir,
            file_prefix=file_prefix,
            is_show_fig=is_show_fig,
        )

    return result
