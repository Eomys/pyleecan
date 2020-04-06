# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pyleecan.Functions.Plot.plot_A_2D import plot_A_2D


def plot_A_time(
    self,
    Data_str,
    alpha=None,
    alpha_index=0,
    is_fft=False,
    is_elecorder=False,
    freq_max=20000,
    is_norm=False,
    unit="SI",
    out_list=[],
):
    """Plots a field as a function of time

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
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
    out_list : list
        list of Output objects to compare
    """

    # Get Data object names
    Phys = getattr(self, Data_str.split(".")[0])
    A = getattr(Phys, Data_str.split(".")[1])
    B_list = []
    for out in out_list:
        Phys = getattr(out, Data_str.split(".")[0])
        B_list.append(getattr(Phys, Data_str.split(".")[1]))

    # Set plot
    fig = plt.figure(constrained_layout=True, figsize=(20, 10))
    legend_list = [self.post.legend_name]
    for out in out_list:
        legend_list.append(out.post.legend_name)
    color_list = [self.post.line_color]
    for out in out_list:
        color_list.append(out.post.line_color)
    xlabel = "Time [s]"
    if unit == "SI":
        unit = A.unit
    if is_norm:
        ylabel = r"$\frac{" + A.symbol + "}{" + A.symbol + "_0}\, [" + unit + "]$"
    else:
        ylabel = r"$" + A.symbol + "\, [" + unit + "]$"

    # Extract the fields
    if alpha != None:
        alpha_str = "angle=" + str(alpha)
    else:
        alpha_str = "angle[" + str(alpha_index) + "]"

    (time, Ydata) = A.compare_along(
        "time", alpha_str, data_list=B_list, unit=unit, is_norm=is_norm
    )

    title = A.name + " over time at " + alpha_str

    # Plot the original graph
    plot_A_2D(
        time,
        Ydata,
        legend_list=legend_list,
        color_list=color_list,
        is_newfig=False,
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
    )

    if is_fft:
        title = "FFT of " + A.name
        ylabel = r"$\widehat{" + A.symbol + "}\, [" + unit + "]$"

        if is_elecorder:
            elec_max = freq_max / A.normalizations.get("elec_order")
            xlabel = "Electrical order []"
            (freqs, Ydata) = A.compare_magnitude_along(
                "freqs=[0," + str(elec_max) + "]{elec_order}",
                alpha_str,
                data_list=B_list,
                unit=unit,
                is_norm=False,
            )

        else:
            xlabel = "Frequency [Hz]"
            (freqs, Ydata) = A.compare_magnitude_along(
                "freqs=[0," + str(freq_max) + "]",
                alpha_str,
                data_list=B_list,
                unit=unit,
                is_norm=False,
            )

        plot_A_2D(
            freqs,
            Ydata,
            legend_list=legend_list,
            color_list=color_list,
            is_newfig=False,
            fig=fig,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            type="bargraph",
        )
