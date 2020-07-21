# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_A_2D import plot_A_2D
from ...definitions import config_dict


def plot_A_space(
    data,
    t=None,
    t_index=0,
    is_spaceorder=False,
    r_max=100,
    fund_harm=None,
    unit="SI",
    data_list=[],
    legend_list=[],
    color_list=[],
    save_path=None,
    mag_max=None,
    is_auto_ticks=True,
    fig=None,
):
    """Plots a field as a function of space (angle)

    Parameters
    ----------
    data : Data
        a Data object
    index_list : list
        list of indices to take from a components axis
    t : float
        time value at which to slice
    t_index : int
        time index at which to slice
    is_spaceorder : bool
        boolean indicating if we want to use the spatial order for the fft axis
    r_max : int
        maximum value of the wavenumber for the fft axis
    fund_harm : float
        frequency of the fundamental harmonic
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
    mag_max : float
        maximum alue for the y-axis of the fft
    is_auto_ticks : bool
        in fft, adjust ticks to wavenumbers (deactivate if too close)
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    """

    # Set plot
    (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
    data_list2 = [data] + data_list
    if legend_list == []:
        legend_list = [d.name for d in data_list2]
    if color_list == []:
        curve_colors = config_dict["color_dict"]["CURVE_COLORS"]
        color_list = curve_colors

    if unit == "SI":
        unit = data.unit

    # Prepare the extractions
    if t != None:
        t_str = "time=" + str(t)
    else:
        t_str = "time[" + str(t_index) + "]"
    if data_list == []:
        title = "FFT of " + data.name
    else:
        title = "Comparison of FFT"
    if data.symbol == "Magnitude":
        ylabel = "Magnitude [" + unit + "]"
    else:
        ylabel = r"$|\widehat{" + data.symbol + "}|\, [" + unit + "]$"
    legend_list = [legend_list[0]] + [legend_list[-1]]
    
    if is_spaceorder:
        order_max = r_max / data.normalizations.get("space_order")
        xlabel = "Space order []"
        results = data.compare_magnitude_along(
            "wavenumber=[0," + str(order_max) + "]{space_order}",
            t_str,
            data_list=data_list,
            unit=unit,
            is_norm=False,
        )

    else:
        xlabel = "Wavenumber []"
        results = data.compare_magnitude_along(
            "wavenumber=[0," + str(r_max) + "]",
            t_str,
            data_list=data_list,
            unit=unit,
            is_norm=False,
        )
    wavenumber = results["wavenumber"]
    Ydata = [results[data.symbol]] + [
        results[d.symbol + "_" + str(i)] for i, d in enumerate(data_list)
    ]

    if is_auto_ticks:
        indices = [0]
        for i in range(len(Ydata)):
            indices += list(
                set([ind for ind, y in enumerate(Ydata[i]) if abs(y) > 0.01])
            )
        xticks = wavenumber[indices]
    else:
        xticks = None

    plot_A_2D(
        wavenumber,
        Ydata,
        legend_list=legend_list,
        color_list=color_list,
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        type="bargraph",
        is_fund=True,
        fund_harm=fund_harm,
        y_max=mag_max,
        xticks=xticks,
    )

    if save_path is not None:
        fig.savefig(save_path)

