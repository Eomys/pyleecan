from os import makedirs
from os.path import abspath, exists, join

import matplotlib.pyplot as plt
import numpy as np


REGION_COLOR = {
    "MTPA": "red",
    "FW": "limegreen",
    "MTPV": "blue",
}


def _build_region_segments(speed, values, regions):
    """Split a full-load envelope into contiguous segments by control region."""

    speed = np.asarray(speed, dtype=float)
    values = np.asarray(values, dtype=float)
    regions = np.asarray(regions)

    if speed.ndim != 1 or values.ndim != 1 or regions.ndim != 1:
        raise ValueError("speed, values and regions must be 1D arrays")
    if not (speed.size == values.size == regions.size):
        raise ValueError("speed, values and regions must share the same length")

    segments = {region: [] for region in REGION_COLOR}
    valid_idx = np.where(np.isfinite(speed) & np.isfinite(values))[0]
    if valid_idx.size == 0:
        return segments

    split_idx = (
        np.where(
            (np.diff(valid_idx) > 1)
            | (regions[valid_idx[1:]] != regions[valid_idx[:-1]])
        )[0]
        + 1
    )

    for segment_idx in np.split(valid_idx, split_idx):
        region = str(regions[segment_idx[0]])
        if region in segments:
            segments[region].append((speed[segment_idx], values[segment_idx]))

    return segments


def _plot_segmented_envelope(
    speed, values, regions, ylabel, save_path, is_show_fig=False
):
    """Plot a continuous full-load envelope with region-colored overlays."""

    speed = np.asarray(speed, dtype=float)
    values = np.asarray(values, dtype=float)
    segments = _build_region_segments(speed, values, regions)

    fig, ax = plt.subplots()
    ax.plot(speed, values, color="black", linewidth=1.5, alpha=0.6)

    has_region_handle = False
    for region, color in REGION_COLOR.items():
        for idx, (x_data, y_data) in enumerate(segments[region]):
            ax.plot(
                x_data,
                y_data,
                color=color,
                linewidth=2.5,
                marker="o",
                markersize=4,
                label=region if idx == 0 else None,
            )
            has_region_handle = True

    ax.set_xlabel("Speed [rpm]")
    ax.set_ylabel(ylabel)
    ax.grid(True)
    if has_region_handle:
        ax.legend()
    fig.tight_layout()
    fig.savefig(save_path, dpi=150)

    if is_show_fig:
        plt.show()
    else:
        plt.close(fig)


def plot_efficiency_map(
    result, save_dir, file_prefix="efficiency_map", is_show_fig=False
):
    """Generate standard efficiency-map figures and save them to disk."""

    from ....Functions.Plot.plot_3D import plot_3D

    save_dir = abspath(save_dir)
    if not exists(save_dir):
        makedirs(save_dir)

    paths = {
        "torque_envelope": join(save_dir, file_prefix + "_torque_envelope.png"),
        "power_envelope": join(save_dir, file_prefix + "_power_envelope.png"),
        "efficiency_map": join(save_dir, file_prefix + "_efficiency_map.png"),
        "current_map": join(save_dir, file_prefix + "_current_map.png"),
        "voltage_map": join(save_dir, file_prefix + "_voltage_map.png"),
    }
    if "control_region_code" in result:
        paths["control_region_map"] = join(
            save_dir, file_prefix + "_control_region_map.png"
        )

    speed = np.asarray(result["speed"])
    tem_max = np.asarray(result["Tem_max"])
    full_load = result.get("full_load", {})
    full_load_power = np.asarray(full_load.get("P_out", np.full(speed.size, np.nan)))
    full_load_control_region = np.asarray(
        result.get(
            "full_load_control_region",
            np.full(speed.shape, "MTPA", dtype="<U7"),
        )
    )

    _plot_segmented_envelope(
        speed,
        tem_max,
        full_load_control_region,
        ylabel="Torque [N.m]",
        save_path=paths["torque_envelope"],
        is_show_fig=is_show_fig,
    )

    _plot_segmented_envelope(
        speed,
        full_load_power * 1e-3,
        full_load_control_region,
        ylabel="Power [kW]",
        save_path=paths["power_envelope"],
        is_show_fig=is_show_fig,
    )

    plot_3D(
        Xdata=result["N0"],
        Ydata=result["Tem_av"],
        Zdata=result["efficiency"],
        xlabel="Speed [rpm]",
        ylabel="Torque [N.m]",
        zlabel="Efficiency [-]",
        title="Efficiency Map",
        type_plot="pcolormesh",
        save_path=paths["efficiency_map"],
        is_show_fig=is_show_fig,
    )

    plot_3D(
        Xdata=result["N0"],
        Ydata=result["Tem_av"],
        Zdata=result["I_rms"],
        xlabel="Speed [rpm]",
        ylabel="Torque [N.m]",
        zlabel="Current [Arms]",
        title="Current Map",
        type_plot="pcolormesh",
        save_path=paths["current_map"],
        is_show_fig=is_show_fig,
    )

    plot_3D(
        Xdata=result["N0"],
        Ydata=result["Tem_av"],
        Zdata=result["U_rms"],
        xlabel="Speed [rpm]",
        ylabel="Torque [N.m]",
        zlabel="Voltage [Vrms]",
        title="Voltage Map",
        type_plot="pcolormesh",
        save_path=paths["voltage_map"],
        is_show_fig=is_show_fig,
    )

    if "control_region_map" in paths:
        plot_3D(
            Xdata=result["N0"],
            Ydata=result["Tem_av"],
            Zdata=result["control_region_code"],
            xlabel="Speed [rpm]",
            ylabel="Torque [N.m]",
            zlabel="Region code [-]",
            title="Control Region Map",
            type_plot="pcolormesh",
            save_path=paths["control_region_map"],
            is_show_fig=is_show_fig,
        )

    return paths
