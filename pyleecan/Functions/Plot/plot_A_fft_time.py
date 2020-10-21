# -*- coding: utf-8 -*-

from ..init_fig import init_fig
from .plot_A_2D import plot_A_2D
from ...definitions import config_dict

from numpy import max as np_max


def plot_A_fft_time(
    data,
    alpha=None,
    alpha_index=0,
    is_elecorder=False,
    freq_max=20000,
    unit="SI",
    data_list=[],
    legend_list=[],
    color_list=[],
    save_path=None,
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
    is_elecorder : bool
        boolean indicating if we want to use the electrical order for the fft axis
    freq_max : int
        maximum value of the frequency for the fft axis
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
    if color_list == []:
        color_list = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]

    if unit == "SI":
        unit = data.unit
        unit_str = "[" + unit + "]"
    elif "dB" in unit:
        unit_str = (
            "[" + unit + " re. " + str(data.normalizations["ref"]) + data.unit + "]"
        )
    else:
        unit_str = "[" + unit + "]"

    # Prepare the extractions
    if alpha != None:
        alpha_str = "angle=" + str(alpha)
    else:
        alpha_str = "angle[" + str(alpha_index) + "]"

    if data_list == []:
        title = "FFT of " + data.name
    else:
        title = "Comparison of " + data.name + " FFT"
    if data.symbol == "Magnitude":
        ylabel = "Magnitude " + unit_str
    else:
        ylabel = r"$|\widehat{" + data.symbol + "}|$ " + unit_str
        
    Xdatas = []
    Ydatas = []
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
        indices = [ind for ind, y in enumerate(Ydatas[0]) if abs(y) > abs(0.01 * np_max(y))]
        xticks = freqs[indices]
    else:
        xticks = None

    plot_A_2D(
        Xdatas,
        Ydatas,
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
        subplot_index=subplot_index,
    )

    if is_show_fig:
        fig.show()
