# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from .plot_A_2D import plot_A_2D
from .plot_A_3D import plot_A_3D
from numpy import meshgrid, max as np_max


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
    colormap="RdBu_r",
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
    """

    # Set plot
    fig, axs = plt.subplots(3, 2, tight_layout=True, figsize=(20, 10))
    title = data.name + " over time and space"

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
        (time, angle, A_t_s) = data.get_along(
            "time", "angle{°}", unit=unit, is_norm=is_norm
        )
    else:
        (time, angle, A_t_s) = data.get_along(
            "time", "angle", unit=unit, is_norm=is_norm
        )
    angle_map, time_map = meshgrid(angle, time)
    if z_max is None:
        z_max = np_max(A_t_s)
    plot_A_3D(
        angle_map,
        time_map,
        A_t_s,
        z_max=z_max,
        z_min=-z_max,
        colormap=colormap,
        xlabel=xlabel,
        ylabel=ylabel,
        zlabel=zlabel,
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
    (time, Ydata) = data.compare_along("time", unit=unit, is_norm=is_norm)
    # Plot the original graph
    plot_A_2D(
        time,
        Ydata,
        fig=fig,
        subplot_index=2,
        xlabel=xlabel,
        ylabel=ylabel,
    )

    # angle
    if is_deg:
        xlabel = "Angle [°]"
    else:
        xlabel = "Angle [rad]"
    if is_deg:
        (angle, Ydata) = data.compare_along("angle{°}", unit=unit, is_norm=is_norm)
    else:
        (angle, Ydata) = data.compare_along("angle", unit=unit, is_norm=is_norm)

    # Plot the original graph
    plot_A_2D(
        angle,
        Ydata,
        fig=fig,
        subplot_index=4,
        xlabel=xlabel,
        ylabel=ylabel,
    )

    # fft time
    if data.symbol == "Magnitude":
        ylabel = "Magnitude [" + unit + "]"
    else:
        ylabel = r"$|\widehat{" + data.symbol + "}|\, [" + unit + "]$"
    if is_elecorder:
        elec_max = freq_max / data.normalizations.get("elec_order")
        xlabel = "Electrical order []"
        (freqs, Ydata) = data.compare_magnitude_along(
            "freqs=[0," + str(elec_max) + "]{elec_order}", unit=unit, is_norm=False,
        )
    else:
        xlabel = "Frequency [Hz]"
        (freqs, Ydata) = data.compare_magnitude_along(
            "freqs=[0," + str(freq_max) + "]", unit=unit, is_norm=False,
        )
    plot_A_2D(
        freqs,
        Ydata,
        fig=fig,
        subplot_index=3,
        xlabel=xlabel,
        ylabel=ylabel,
        type="bargraph",
    )

    # fft space
    if is_spaceorder:
        order_max = r_max / data.normalizations.get("space_order")
        xlabel = "Space order []"
        (wavenumber, Ydata) = data.compare_magnitude_along(
            "wavenumber=[0," + str(order_max) + "]{space_order}",
            unit=unit,
            is_norm=False,
        )
    else:
        xlabel = "Wavenumber []"
        (wavenumber, Ydata) = data.compare_magnitude_along(
            "wavenumber=[0," + str(r_max) + "]", unit=unit, is_norm=False
        )
    plot_A_2D(
        wavenumber,
        Ydata,
        fig=fig,
        subplot_index=5,
        xlabel=xlabel,
        ylabel=ylabel,
        type="bargraph",
    )

    axs[0, 1].axis("off")

    fig.canvas.set_window_title(title)
    fig.suptitle(title, x=0.65, fontsize=16)
    fig.tight_layout()
