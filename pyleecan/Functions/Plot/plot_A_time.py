# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_A_2D import plot_A_2D
from ...definitions import config_dict
from numpy import squeeze, split


def plot_A_time(
    data,
    index_list=[0],
    alpha=None,
    alpha_index=0,
    is_fft=False,
    is_elecorder=False,
    freq_max=20000,
    is_norm=False,
    unit="SI",
    data_list=[],
    legend_list=[],
    color_list=[],
    save_path=None,
    y_min=None,
    y_max=None,
    mag_max=None,
    is_auto_ticks=True,
    fig=None,
    subplot_index=None,
):
    """Plots a field as a function of time

    Parameters
    ----------
    data : Data
        a Data object
    index_list : list
        list of indices to take from a components axis
    alpha : float
        angle value at which to slice
    alpha_index : int
        angle index at which to slice
    is_fft : bool
        boolean indicating if we want to plot the time-fft below the plot
    is_elecorder : bool
        boolean indicating if we want to use the electrical order for the fft axis
    freq_max : int
        maximum value of the frequency for the fft axis
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    data_list : list
        list of Data objects to compare
    legend_list : list
        list of legends to use for each Data object (including reference one) instead of data.name
    color_list : list
        list of colors to use for each Data object
    save_path : str
        path and name of the png file to save
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    mag_max : float
        maximum alue for the y-axis of the fft
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    """

    # Set plot
    (fig, axes, patch_leg, label_leg) = init_fig(fig, shape="rectangle")
    data_list2 = [data] + data_list
    if legend_list == []:
        legend_list = [d.name for d in data_list2]
    curve_colors = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]
    phase_colors = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
    legends = []
    colors = []
    n_phase = len(index_list)
    list_str = None
    for i, d in enumerate(data_list2):
        is_components = False
        for axis in d.axes:
            try:
                if axis.is_components:
                    is_components = True
                    legends += [
                        legend_list[i] + ": " + axis.values.tolist()[j]
                        for j in index_list
                    ]
                    colors += [phase_colors[i * n_phase + j] for j in range(n_phase)]
                    list_str = axis.name
            except:
                is_components = False
        if not is_components:
            legends += [legend_list[i]]
            colors += [curve_colors[i]]
    if color_list == []:
        color_list = colors

    xlabel = "Time [s]"
    if unit == "SI":
        unit = data.unit
    if is_norm:
        ylabel = r"$\frac{" + data.symbol + "}{" + data.symbol + "_0}\, [" + unit + "]$"
    else:
        ylabel = r"$" + data.symbol + "\, [" + unit + "]$"

    # Prepare the extractions
    if alpha != None:
        alpha_str = "angle=" + str(alpha)
    else:
        alpha_str = "angle[" + str(alpha_index) + "]"
    if data_list == []:
        title = data.name + " over time at " + alpha_str
    else:
        title = "Comparison of " + data.name + " over space at " + alpha_str

    # Extract the fields
    if list_str is not None:
        results = data.compare_along(
            "time",
            alpha_str,
            list_str + str(index_list),
            data_list=data_list,
            unit=unit,
            is_norm=is_norm,
        )
    else:
        results = data.compare_along(
            "time", alpha_str, data_list=data_list, unit=unit, is_norm=is_norm
        )
    time = results["time"]
    Ydatas = [results[data.symbol]] + [
        results[d.symbol + "_" + str(i)] for i, d in enumerate(data_list)
    ]
    Ydata = []
    for d in Ydatas:
        if d.ndim != 1:
            Ydata += split(d, len(index_list))
        else:
            Ydata += [d]
    Ydata = [squeeze(d) for d in Ydata]

    # Plot the original graph
    plot_A_2D(
        time,
        Ydata,
        legend_list=legends,
        color_list=color_list,
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        y_min=y_min,
        y_max=y_max,
        save_path=save_path,
        subplot_index=subplot_index,
    )

    if is_fft:
        if "dB" in unit:
            unit_str = "[" + unit + " re. " + str(data.normalizations["ref"]) + data.unit + "]"
        else:
            unit_str = "[" + unit + "]"
        if data_list == []:
            title = "FFT of " + data.name
        else:
            title = "Comparison of " + data.name + " FFT"
        if data.symbol == "Magnitude":
            ylabel = "Magnitude " + unit_str
        else:
            ylabel = r"$|\widehat{" + data.symbol + "}|$ " + unit_str
        legend_list = [legend_list[0]] + [legend_list[-1]]

        if is_elecorder:
            elec_max = freq_max / data.normalizations.get("elec_order")
            xlabel = "Electrical order []"
            results = data.compare_magnitude_along(
                "freqs=[0," + str(elec_max) + "]{elec_order}",
                alpha_str,
                data_list=data_list,
                unit=unit,
                is_norm=False,
            )

        else:
            xlabel = "Frequency [Hz]"
            results = data.compare_magnitude_along(
                "freqs=[0," + str(freq_max) + "]",
                alpha_str,
                data_list=data_list,
                unit=unit,
                is_norm=False,
            )

        freqs = results["freqs"]
        Ydata = [results[data.symbol]] + [
            results[d.symbol + "_" + str(i)] for i, d in enumerate(data_list)
        ]

        if is_auto_ticks:
            indices = [0]
            for i in range(len(Ydata)):
                indices += list(
                    set([ind for ind, y in enumerate(Ydata[i]) if abs(y) > 0.01])
                )
            xticks = freqs[indices]
        else:
            xticks = None

        plot_A_2D(
            freqs,
            Ydata,
            legend_list=legend_list,
            color_list=color_list,
            fig=fig,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            type="bargraph",
            y_max=mag_max,
            xticks=xticks,
            save_path=save_path,
        )
