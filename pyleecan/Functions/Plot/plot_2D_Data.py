# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_2D import plot_2D
from . import unit_dict, norm_dict, axes_dict
from ...definitions import config_dict
from numpy import squeeze, split, array, where, max as np_max


def plot_2D_Data(
    data,
    *args,
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
    barwidth=100,
    type_plot=None,
    is_fund=False,
    fund_harm=None,
):
    """Plots a field as a function of time

    Parameters
    ----------
    data : Data
        a Data object
    *args : list of str
        arguments to specify which axes to plot
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
        full path of the png file where the figure is saved if save_path is not None
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
    barwidth : float
        barwidth scaling factor, only if type_plot = "bargraph"
    type_plot : str
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    fund_harm : float
        frequency/order/wavenumber of the fundamental harmonic that must be displayed in red in the fft

    """

    if len(args) == 1 and type(args[0]) == tuple:
        args = args[0]  # if called from another script with *args

    # Set plot
    is_show_fig = True if fig is None else False
    (fig, axes, patch_leg, label_leg) = init_fig(fig, shape="rectangle")
    curve_colors = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]
    phase_colors = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
    line_styles = config_dict["PLOT"]["LINE_STYLE"]

    # Set unit
    if unit == "SI":
        unit = data.unit

    # Detect fft
    is_fft = False
    if any("wavenumber" in s for s in args) or any("freqs" in s for s in args):
        is_fft = True
        if "dB" in unit:
            unit_str = (
                "[" + unit + " re. " + str(data.normalizations["ref"]) + data.unit + "]"
            )
        else:
            unit_str = "[" + unit + "]"
        if data.symbol == "Magnitude":
            ylabel = "Magnitude " + unit_str
        else:
            ylabel = r"$|\widehat{" + data.symbol + "}|$ " + unit_str
        if data_list == []:
            title1 = "FFT of " + data.name.lower() + " "
        else:
            title1 = "Comparison of " + data.name.lower() + " FFT "
    else:
        if data_list == []:
            # title = data.name.capitalize() + " for " + ', '.join(args_str)
            title1 = data.name.capitalize() + " "
        else:
            # title = data.name.capitalize() + " for " + ', '.join(args_str)
            title1 = "Comparison of " + data.name.lower() + " "
        if is_norm:
            ylabel = (
                r"$\frac{" + data.symbol + "}{" + data.symbol + "_0}\, [" + unit + "]$"
            )
        else:
            ylabel = r"$" + data.symbol + "\, [" + unit + "]$"

    # Extract field and axes
    Xdatas = []
    Ydatas = []
    data_list2 = [data] + data_list
    for i, d in enumerate(data_list2):
        if is_fft:
            result = d.get_magnitude_along(args, unit=unit, is_norm=is_norm)
            if i == 0:
                axes_list = result.pop("axes_list")
                axes_dict_other = result.pop("axes_dict_other")
            Ydatas.append(result.pop(d.symbol))
            Xdatas.append(result[list(result)[0]])
        else:
            result = d.get_along(args, unit=unit, is_norm=is_norm)
            if i == 0:
                axes_list = result.pop("axes_list")
                axes_dict_other = result.pop("axes_dict_other")
            Ydatas.append(result.pop(d.symbol))
            Xdatas.append(result[list(result)[0]])

    # Build labels and titles
    title2 = ""
    title3 = " for "
    for axis in axes_list:
        if axis.extension in [
            "whole",
            "interval",
            "oneperiod",
            "antiperiod",
            "smallestperiod",
        ]:
            if axis.name in axes_dict:
                name = axes_dict[axis.name]
            else:
                name = axis.name
            title2 = "over " + axis.name.lower()
            if axis.unit == "SI":
                unit = unit_dict[axis.name]
                xlabel = name.capitalize() + " [" + unit + "]"
            elif axis.unit in norm_dict:
                xlabel = norm_dict[axis.unit]
            else:
                unit = axis.unit
                xlabel = name.capitalize() + " [" + unit + "]"
            if (
                axis.name == "angle"
                and axis.unit == "°"
                and round(np_max(axis.values) / 6) % 5 == 0
            ):
                xticks = [i * round(np_max(axis.values) / 6) for i in range(7)]
            else:
                xticks = None
        else:
            if axis.unit == "SI":
                unit = unit_dict[axis.name]
            elif axis.unit in norm_dict:
                unit = norm_dict[axis.unit]
            else:
                unit = axis.unit
            title3 += axis.name + "=" + str(result[axis.name]) + " " + unit + ", "
    title4 = ""
    for axis_name in axes_dict_other:
        title4 += (
            axis_name
            + "="
            + str(axes_dict_other[axis_name][0])
            + " "
            + axes_dict_other[axis_name][1]
            + ", "
        )

    if title3 == " for " and title4 == "":
        title3 = ""

    title = title1 + title2 + title3 + title4
    title = title.rstrip(", ")

    # Build legends and colors
    if legend_list == [] and data_list != []:
        legend_list = [d.name for d in data_list2]
    elif legend_list == []:
        legend_list = ["" for d in data_list2]
    legends = []
    colors = []
    linestyle_list = []
    for i, d in enumerate(data_list2):
        is_overlay = False
        for axis in axes_list:
            if axis.extension == "list":
                is_overlay = True
                n_phase = len(axis.values)
                if axis.unit == "SI":
                    unit = unit_dict[axis.name]
                elif axis.unit in norm_dict:
                    unit = norm_dict[axis.unit]
                else:
                    unit = axis.unit
                legends += [
                    "["
                    + legend_list[i]
                    + "] "
                    + axis.name
                    + "= "
                    + str(axis.values.tolist()[j])
                    + " "
                    + unit
                    for j in range(n_phase)
                ]
                colors += [phase_colors[i * n_phase + j] for j in range(n_phase)]
                linestyle_list += [line_styles[i] for j in range(n_phase)]

        if not is_overlay:
            legends += [legend_list[i]]
            colors += [curve_colors[i]]
            linestyle_list += [line_styles[i]]

    if color_list == []:
        color_list = colors

    # Split phases
    if is_overlay:
        Ydata = []
        for d in Ydatas:
            if d.ndim != 1:
                axis_index = where(array(d.shape) == n_phase)[0]
                if axis_index.size > 1:
                    print("WARNING, several axes with same dimensions")
                Ydata += split(d, n_phase, axis=axis_index[0])
            else:
                Ydata += [d]
        Ydatas = [squeeze(d) for d in Ydata]
        Xdata = []
        for i in range(len(data_list2)):
            Xdata += [Xdatas[i] for x in range(n_phase)]
        Xdatas = Xdata

    # Call generic plot function
    if is_fft:
        freqs = Xdatas[0]
        if is_auto_ticks:
            indices = [
                ind for ind, y in enumerate(Ydatas[0]) if abs(y) > abs(0.01 * np_max(y))
            ]
            xticks = freqs[indices]
        else:
            xticks = None

        # Force bargraph for fft if type_graph not specified
        if type_plot is None:
            type_plot = "bargraph"

        plot_2D(
            Xdatas,
            Ydatas,
            legend_list=legend_list,
            color_list=color_list,
            fig=fig,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            type_plot=type_plot,
            y_max=mag_max,
            xticks=xticks,
            save_path=save_path,
            barwidth=barwidth,
            fund_harm=fund_harm,
        )

    else:

        # Force curve plot if type_plot not specified
        if type_plot is None:
            type_plot = "curve"

        plot_2D(
            Xdatas,
            Ydatas,
            legend_list=legends,
            color_list=color_list,
            fig=fig,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            type_plot=type_plot,
            y_min=y_min,
            y_max=y_max,
            xticks=xticks,
            linestyle_list=linestyle_list,
            save_path=save_path,
        )

    if is_show_fig:
        fig.show()
