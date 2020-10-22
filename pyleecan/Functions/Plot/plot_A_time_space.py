# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from .plot_2D import plot_2D
from .plot_3D import plot_3D
from ...definitions import config_dict
from numpy import meshgrid, max as np_max

FONT_NAME = config_dict["PLOT"]["FONT_NAME"]


def plot_A_time_space(
    data,
    is_deg=True,
    is_elecorder=False,
    is_spaceorder=False,
    freq_max=20000,
    r_max=100,
    z_max=None,
    is_norm=False,
    unit="SI",
    colormap=None,
    save_path=None,
    is_auto_ticks=True,
):
    """Plots a field as a function of time and space (angle)

    Parameters
    ----------
    data : Data
        a Data object
    is_deg : bool
        boolean indicating if the angle must be converted to degrees
    is_elecorder : bool
        boolean indicating if we want to use the electrical order for the fft axis
    is_spaceorder : bool
        boolean indicating if we want to use the spatial order for the fft axis
    freq_max : float
        maximum value of the frequency for the fft axis
    r_max : int
        maximum value of the wavenumber for the fft axis
    z_max : float
        maximum value for the field
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    colormap : colormap object
        colormap prescribed by user
    save_path : str
        path and name of the png file to save
    is_auto_ticks : bool
        in fft, adjust ticks to freqs and wavenumbers (deactivate if too close)
    """

    # Set plot
    fig, axs = plt.subplots(3, 2, tight_layout=True, figsize=(20, 10))
    title = data.name + " over time and space"
    if colormap is None:
        colormap = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
    color_list = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]

    # pcolorplot
    if is_deg:
        xlabel = "Angle [°]"
    else:
        xlabel = "Angle [rad]"
    ylabel = "Time [s]"
    if unit == "SI":
        unit = data.unit
    if is_norm:
        zlabel = r"$\frac{" + data.symbol + "}{" + data.symbol + "_0}\, [" + unit + "]$"
    else:
        zlabel = r"$" + data.symbol + "\, [" + unit + "]$"

    if is_deg:
        results = data.get_along("time", "angle{°}", unit=unit, is_norm=is_norm)
    else:
        results = data.get_along("time", "angle", unit=unit, is_norm=is_norm)
    angle = results["angle"]
    if is_deg and round(np_max(angle) / 6) % 5 == 0:
        xticks = [i * round(np_max(angle) / 6) for i in range(7)]
    else:
        xticks = None
    time = results["time"]
    A_t_s = results[data.symbol]
    angle_map, time_map = meshgrid(angle, time)
    if z_max is None:
        z_max = np_max(A_t_s)
    plot_3D(
        angle_map,
        time_map,
        A_t_s,
        z_max=z_max,
        z_min=-z_max,
        colormap=colormap,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
        xticks=xticks,
        fig=fig,
        subplot_index=0,
        type="pcolor",
    )

    # 2D plots

    # time
    xlabel = "Time [s]"
    if is_norm:
        ylabel = r"$\frac{" + data.symbol + "}{" + data.symbol + "_0}\, [" + unit + "]$"
    else:
        ylabel = r"$" + data.symbol + "\, [" + unit + "]$"
    results = data.compare_along("time", unit=unit, is_norm=is_norm)
    time = results["time"]
    Ydata = [results[data.symbol]]
    # Plot the original graph
    plot_2D(
        time,
        Ydata,
        fig=fig,
        subplot_index=2,
        xlabel=xlabel,
        ylabel=ylabel,
        color_list=color_list,
    )

    # angle
    if is_deg:
        xlabel = "Angle [°]"
    else:
        xlabel = "Angle [rad]"
    if is_deg:
        results = data.compare_along("angle{°}", unit=unit, is_norm=is_norm)
    else:
        results = data.compare_along("angle", unit=unit, is_norm=is_norm)
    angle = results["angle"]
    Ydata = [results[data.symbol]]
    # Plot the original graph
    plot_2D(
        angle,
        Ydata,
        fig=fig,
        subplot_index=4,
        xlabel=xlabel,
        ylabel=ylabel,
        xticks=xticks,
        color_list=color_list,
    )

    # fft time
    if "dB" in unit:
        unit_str = (
            "[" + unit + " re. " + str(data.normalizations["ref"]) + data.unit + "]"
        )
    else:
        unit_str = "[" + unit + "]"
    if data.symbol == "Magnitude":
        ylabel = "Magnitude [" + unit + "]"
    else:
        ylabel = r"$|\widehat{" + data.symbol + "}|$ " + unit_str
    if is_elecorder:
        elec_max = freq_max / data.normalizations.get("elec_order")
        xlabel = "Electrical order []"
        (freqs, Ydata) = data.compare_magnitude_along(
            "freqs=[0," + str(elec_max) + "]{elec_order}", unit=unit, is_norm=False
        )
    else:
        xlabel = "Frequency [Hz]"
        results = data.compare_magnitude_along(
            "freqs=[0," + str(freq_max) + "]", unit=unit, is_norm=False
        )
    freqs = results["freqs"]
    Ydata = [results[data.symbol]]

    if is_auto_ticks:
        indices = [ind for ind, y in enumerate(Ydata[0]) if abs(y) > 0.01]
        indices = [0] + list(set(indices))
        xticks = freqs[indices]
    else:
        xticks = None

    plot_2D(
        freqs,
        Ydata,
        fig=fig,
        subplot_index=3,
        xlabel=xlabel,
        ylabel=ylabel,
        type="bargraph",
        xticks=xticks,
        color_list=color_list,
    )

    # fft space
    if is_spaceorder:
        order_max = r_max / data.normalizations.get("space_order")
        xlabel = "Space order []"
        results = data.compare_magnitude_along(
            "wavenumber=[0," + str(order_max) + "]{space_order}",
            unit=unit,
            is_norm=False,
        )
    else:
        xlabel = "Wavenumber []"
        results = data.compare_magnitude_along(
            "wavenumber=[0," + str(r_max) + "]", unit=unit, is_norm=False
        )
    wavenumber = results["wavenumber"]
    Ydata = [results[data.symbol]]

    if is_auto_ticks:
        indices = [ind for ind, y in enumerate(Ydata[0]) if abs(y) > 0.01]
        indices = [0] + list(set(indices))
        xticks = wavenumber[indices]
    else:
        xticks = None

    plot_2D(
        wavenumber,
        Ydata,
        fig=fig,
        subplot_index=5,
        xlabel=xlabel,
        ylabel=ylabel,
        type="bargraph",
        xticks=xticks,
        color_list=color_list,
    )

    axs[0, 1].axis("off")

    fig.canvas.set_window_title(title)
    fig.suptitle(title, x=0.65, fontsize=24, fontname=FONT_NAME)
    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path)
        # plt.close()

    fig.show()
