# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import where, argmin, abs

from ...Functions.init_fig import init_subplot


def plot_A_2D(
    Xdata,
    Ydatas,
    legend_list=[""],
    color_list=["b"],
    title="",
    xlabel="",
    ylabel="",
    fig=None,
    subplot_index=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_disp_title=True,
    is_grid=True,
    type="curve",
    is_fund=False,
    fund_harm=None,
):
    """Plots a 2D graph (curve, bargraph or barchart) comparing fields in Ydatas

    Parameters
    ----------
    Xdata : ndarray
        array of x-axis values
    Ydatas : list
        list of y-axes values
    legend_list : list
        list of legends
    color_list : list
        list of colors to use for each curve
    title : str
        title of the graph
    xlabel : str
        label for the x-axis
    ylabel : str
        label for the y-axis
    fig : Matplotlib.figure.Figure
        existing figure to use if is_newfig=False
    subplot_index : int
        index of subplot in which to plot
    is_logscale_x : bool
        boolean indicating if the x-axis must be set in logarithmic scale
    is_logscale_y : bool
        boolean indicating if the y-axis must be set in logarithmic scale
    is_disp_title : bool
        boolean indicating if the title must be displayed
    is_grid : bool
        boolean indicating if the grid must be displayed
    type : str
        type of 2D graph : "curve", "bargraph" or "barchart"
    is_fund : bool
        boolean indicating if the bar corresponding to the fundamental must be displayed in red
    fund_harm : float
        frequency of the fundamental harmonic    
    """

    # Set figure/subplot
    fig, ax = init_subplot(fig=fig, subplot_index=subplot_index)

    # Plot
    if type == "curve":
        for i in range(len(Ydatas)):
            ax.plot(Xdata, Ydatas[i], color_list[i], label=legend_list[i])
    elif type == "bargraph":
        for i in range(len(Ydatas)):
            width = Xdata[1] - Xdata[0]
            if i == 0:
                if color_list[i] != "":
                    barlist = ax.bar(
                        Xdata,
                        Ydatas[i],
                        color=color_list[i],
                        width=width,
                        label=legend_list[i],
                    )
                else:
                    barlist = ax.bar(
                        Xdata, Ydatas[i], width=width, label=legend_list[i]
                    )
            else:
                if color_list[i] != "":
                    barlist = ax.bar(
                        Xdata,
                        Ydatas[i],
                        edgecolor=color_list[i],
                        width=width,
                        fc="None",
                        lw=1,
                        label=legend_list[i],
                    )
                else:
                    barlist = ax.bar(
                        Xdata,
                        Ydatas[i],
                        width=width,
                        fc="None",
                        lw=1,
                        label=legend_list[i],
                    )
            if is_fund:  # Find fundamental
                if fund_harm is None:
                    mag_max = max(Ydatas[i])
                    imax = int(where(Ydatas[i] == mag_max)[0])
                else:
                    imax = argmin(abs(Xdata - fund_harm))
                barlist[imax].set_color("r")
    elif type == "barchart":
        for i in range(len(Ydatas)):
            if i == 0:
                if color_list[i] != "":
                    ax.bar(
                        range(len(Xdata)),
                        Ydatas[i],
                        color=color_list[i],
                        width=0.5,
                        label=legend_list[i],
                    )
                else:
                    ax.bar(
                        range(len(Xdata)), Ydatas[i], width=0.5, label=legend_list[i]
                    )
            else:
                if color_list[i] != "":
                    ax.bar(
                        range(len(Xdata)),
                        Ydatas[i],
                        edgecolor=color_list[i],
                        width=0.5,
                        fc="None",
                        lw=1,
                        label=legend_list[i],
                    )
                else:
                    ax.bar(
                        range(len(Xdata)),
                        Ydatas[i],
                        width=0.5,
                        fc="None",
                        lw=1,
                        label=legend_list[i],
                    )
        plt.xticks(range(len(Xdata)), [str(f) for f in Xdata], rotation=90)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if is_logscale_x:
        ax.xscale("log")

    if is_logscale_y:
        ax.yscale("log")

    if is_disp_title:
        ax.set_title(title)

    if is_grid:
        ax.grid()

    if len(Ydatas) > 1:
        ax.legend()

    plt.tight_layout()
