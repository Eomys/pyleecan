# -*- coding: utf-8 -*-

from .plot_2D import plot_2D
from . import unit_dict, norm_dict, axes_dict
from ...definitions import config_dict
from numpy import squeeze, split, array, where, max as np_max


def plot_2D_Data(
    data,
    *arg_list,
    is_norm=False,
    unit="SI",
    data_list=[],
    legend_list=[],
    color_list=[],
    save_path=None,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_disp_title=True,
    is_grid=True,
    is_auto_ticks=True,
    fig=None,
    ax=None,
    barwidth=100,
    type_plot=None,
    fund_harm_dict=None,
    is_show_fig=None,
):
    """Plots a field as a function of time

    Parameters
    ----------
    data : Data
        a Data object
    *arg_list : list of str
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
        full path including folder, name and extension of the file to save if save_path is not None
    x_min : float
        minimum value for the x-axis
    x_max : float
        maximum value for the x-axis
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    is_logscale_x : bool
        boolean indicating if the x-axis must be set in logarithmic scale
    is_logscale_y : bool
        boolean indicating if the y-axis must be set in logarithmic scale
    is_disp_title : bool
        boolean indicating if the title must be displayed
    is_grid : bool
        boolean indicating if the grid must be displayed
    is_auto_ticks : bool
        in fft, adjust ticks to freqs (deactivate if too close)
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        ax on which to plot the data
    barwidth : float
        barwidth scaling factor, only if type_plot = "bargraph"
    type_plot : str
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    fund_harm_dict : dict
        Dict containing axis name as key and frequency/order/wavenumber of fundamental harmonic as value to display fundamental harmonic in red in the fft
    is_show_fig : bool
        True to show figure after plot

    """
    # Extract arg_list it the function called from another script with *arg_list
    if len(arg_list) == 1 and type(arg_list[0]) == tuple:
        arg_list = arg_list[0]

    # Get colors and line_styles from config_dict
    curve_colors = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]
    phase_colors = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
    line_styles = config_dict["PLOT"]["LINE_STYLE"]

    # Set unit
    if unit == "SI":
        unit = data.unit

    # Detect if is fft, build first title part and ylabel
    is_fft = False
    if any("wavenumber" in s for s in arg_list) or any("freqs" in s for s in arg_list):
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
            # title = data.name.capitalize() + " for " + ', '.join(arg_list_str)
            title1 = data.name.capitalize() + " "
        else:
            # title = data.name.capitalize() + " for " + ', '.join(arg_list_str)
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
            result = d.get_magnitude_along(arg_list, unit=unit, is_norm=is_norm)
            if i == 0:
                axes_list = result.pop("axes_list")
                axes_dict_other = result.pop("axes_dict_other")
                result_0 = result
            Ydatas.append(result.pop(d.symbol))
            Xdatas.append(result[list(result)[0]])
        else:
            result = d.get_along(arg_list, unit=unit, is_norm=is_norm)
            if i == 0:
                axes_list = result.pop("axes_list")
                axes_dict_other = result.pop("axes_dict_other")
                result_0 = result
            Ydatas.append(result.pop(d.symbol))
            Xdatas.append(result[list(result)[0]])

    # Find main axis as the axis with the most values
    # main_axis = axes_list[0]  # max(axes_list, key=lambda x: x.values.size)

    # Build xlabel and title parts 2 and 3
    title2 = ""
    title3 = " for "
    for axis in axes_list:
        # Title part 2
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
                main_axis_name = name
            elif axis.unit in norm_dict:
                xlabel = norm_dict[axis.unit]
                main_axis_name = axis.unit
            else:
                unit = axis.unit
                xlabel = name.capitalize() + " [" + unit + "]"
                main_axis_name = name
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

            # if result[axis.name].size >1:
            #     axis_str = result[axis.name].astype(
            #     str
            # )
            #     axis_str = "[" + ",".join(axis_str) +"]"
            # else:
            #     axis_str = str(result[axis.name][0])
            axis_str = str(
                result_0[axis.name]
            )  # TODO: smart conversion of float to str

            title3 += axis.name + "=" + axis_str + " " + unit + ", "

    # Title part 4 containing axes that are here but not involved in requested axes
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

    # Concatenate all title parts
    title = title1 + title2 + title3 + title4

    # Remove last coma due to title3 or title4
    title = title.rstrip(", ")

    # Detect how many curves are overlaid, build legend and color lists
    if legend_list == [] and data_list != []:
        legend_list = ["[" + d.name + "] " for d in data_list2]
    elif legend_list == []:
        legend_list = ["" for d in data_list2]
    else:
        legend_list = ["[" + leg + "] " for leg in legend_list]
    legends = []
    colors = []
    linestyle_list = []
    for i, d in enumerate(data_list2):
        is_overlay = False
        for axis in axes_list:
            if axis.extension == "list":
                is_overlay = True
                n_curves = len(axis.values)
                if axis.unit == "SI":
                    unit = unit_dict[axis.name]
                elif axis.unit in norm_dict:
                    unit = norm_dict[axis.unit]
                else:
                    unit = axis.unit
                legends += [
                    legend_list[i]
                    + axis.name
                    + "= "
                    + str(axis.values.tolist()[j])
                    + " "
                    + unit
                    for j in range(n_curves)
                ]
                colors += [
                    phase_colors[(i * n_curves + j) % len(phase_colors)]
                    for j in range(n_curves)
                ]
                linestyle_list += [line_styles[i] for j in range(n_curves)]

        if not is_overlay:
            legends += [legend_list[i]]
            colors += [curve_colors[i]]
            linestyle_list += [line_styles[i]]

    # Set colors_list to colors that has just been built
    if color_list == []:
        color_list = colors

    # Split Ydatas if the plot overlays several curves
    if is_overlay:
        Ydata = []
        for d in Ydatas:
            if d.ndim != 1:
                axis_index = where(array(d.shape) == n_curves)[0]
                if axis_index.size > 1:
                    print("WARNING, several axes with same dimensions")
                Ydata += split(d, n_curves, axis=axis_index[0])
            else:
                Ydata += [d]
        Ydatas = [squeeze(d) for d in Ydata]
        Xdata = []
        for i in range(len(data_list2)):
            Xdata += [Xdatas[i] for x in range(n_curves)]
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

        # Option to draw fundamental harmonic in red
        if fund_harm_dict is None:
            fund_harm = None
        else:
            # Activate the option only if main axis is in dict and only one Data is plotted
            if main_axis_name in fund_harm_dict and len(Ydatas) == 1:
                fund_harm = fund_harm_dict[main_axis_name]
            else:
                # Deactivate the option
                fund_harm = None

        plot_2D(
            Xdatas,
            Ydatas,
            legend_list=legends,
            color_list=color_list,
            fig=fig,
            ax=ax,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            type_plot=type_plot,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
            is_logscale_x=is_logscale_x,
            is_logscale_y=is_logscale_y,
            is_disp_title=is_disp_title,
            is_grid=is_grid,
            xticks=xticks,
            save_path=save_path,
            barwidth=barwidth,
            fund_harm=fund_harm,
            is_show_fig=is_show_fig,
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
            ax=ax,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            type_plot=type_plot,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
            is_logscale_x=is_logscale_x,
            is_logscale_y=is_logscale_y,
            is_disp_title=is_disp_title,
            is_grid=is_grid,
            xticks=xticks,
            linestyle_list=linestyle_list,
            save_path=save_path,
            is_show_fig=is_show_fig,
        )
