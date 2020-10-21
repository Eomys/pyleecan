# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_A_2D import plot_A_2D
from ...definitions import config_dict
from numpy import squeeze, split, where, array, max as np_max
from itertools import repeat


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
    linestyle_list=[],
    save_path=None,
    y_min=None,
    y_max=None,
    mag_max=None,
    is_auto_ticks=True,
    fig=None,
    subplot_index=None,
):
    """Plots a field as a function of time

    /!\ If relevant /!\ :
        - any change in Function.Plot.plot_A_time should be added in Method.Output.Output.plot.plot_A_time
        - any change in plot_A_time that is applicable to plot_A_space should be implemented in both

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
    linestyle_list : list
        list of linestyle to use for each Data object (ex: "-", "dotted")
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
    is_show_fig = True if fig is None else False
    (fig, axes, patch_leg, label_leg) = init_fig(fig, shape="rectangle")
    data_list2 = [data] + data_list
    if legend_list == []:
        legend_list = [d.name for d in data_list2]
    curve_colors = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]
    phase_colors = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
    legends = []
    colors = []
    linestyles = []
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
                    linestyles += list(repeat("-", n_phase))
                    list_str = axis.name
            except:
                is_components = False
        if not is_components:
            legends += [legend_list[i]]
            colors += [curve_colors[i]]
            linestyles.append("-")
    if color_list == []:
        color_list = colors
    if linestyle_list == []:
        linestyle_list = linestyles

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

    # Title string
    if list_str is not None:
        title = data.name + " over time for " + list_str + str(index_list)
    else:
        title = data.name + " over time for " + alpha_str

    if data_list != []:
        title = "Comparison of " + title

    # Extract the fields
    Xdatas = []
    Ydatas = []
    if list_str is not None:
        for d in data_list2:
            results = data.get_along(
                alpha_str,
                "time",
                list_str + str(index_list),
                unit=unit,
                is_norm=is_norm,
            )
            Xdatas.append(results["time"])
            Ydatas.append(results[data.symbol])
    else:
        for d in data_list2:
            results = data.compare_along(
                alpha_str, "time", data_list=data_list, unit=unit, is_norm=is_norm
            )
            Xdatas.append(results["time"])
            Ydatas.append(results[data.symbol])

    Ydata = []
    for d in Ydatas:
        if d.ndim != 1:
            axis_index = where(array(d.shape) == len(index_list))[0]
            if axis_index.size > 1:
                print("WARNING, several axes with same dimensions")
            Ydata += split(d, len(index_list), axis=axis_index[0])
        else:
            Ydata += [d]
    Ydata = [squeeze(d) for d in Ydata]

    # Plot the original graph
    plot_A_2D(
        Xdatas,
        Ydata,
        legend_list=legends,
        color_list=color_list,
        linestyle_list=linestyle_list,
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
        # Extract the fields
        Xdatas = []
        Ydatas = []
        if "dB" in unit:
            unit_str = (
                "[" + unit + " re. " + str(data.normalizations["ref"]) + data.unit + "]"
            )
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
            for d in data_list2:
                results = d.get_magnitude_along(
                    "freqs=[0," + str(elec_max) + "]{elec_order}",
                    alpha_str,
                    unit=unit,
                    is_norm=False,
                )
                Xdatas.append(results["freqs"])
                Ydatas.append(results[data.symbol])

        else:
            xlabel = "Frequency [Hz]"
            for d in data_list2:
                results = d.get_magnitude_along(
                    "freqs=[0," + str(freq_max) + "]",
                    alpha_str,
                    unit=unit,
                    is_norm=False,
                )
                Xdatas.append(results["freqs"])
                Ydatas.append(results[data.symbol])

        freqs = Xdatas[0]

        if is_auto_ticks:
            indices = [
                ind for ind, y in enumerate(Ydatas[0]) if abs(y) > abs(0.01 * np_max(y))
            ]
            xticks = freqs[indices]
        else:
            xticks = None

        plot_A_2D(
            Xdatas,
            Ydatas,
            legend_list=legend_list,
            color_list=color_list,
            linestyle_list=linestyle_list,
            fig=fig,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            type="bargraph",
            y_max=mag_max,
            xticks=xticks,
            save_path=save_path,
        )

    if is_show_fig:
        fig.show()
