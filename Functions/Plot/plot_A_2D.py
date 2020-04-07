# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import where


def plot_A_2D(
    Xdata,
    Ydatas,
    legend_list=[""],
    color_list=["b"],
    title="",
    xlabel="",
    ylabel="",
    is_newfig=True,
    is_autostack=True,
    fig=None,
    ax=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_disp_title=True,
    is_grid=True,
    type="curve",
    is_fund=False,
):
    """Plots a 2D graph (curve, bargraph or barchart), comparisons allowed with args list

    Parameters
    ----------
    Xdata : ndarray
        array of x-axis values
    Ydatas : list
        list of y-axes values
    legend_list : list
        list of legends
    color_list : list
        list of colors to use foe each curve
    title : str
        title of the graph
    xlabel : str
        label for the x-axis
    ylabel : str
        label for the y-axis
    is_newfig : bool
        boolean indicating if a new figure must be created
    is_autostack : bool
        boolean indicating if this new plot must be stacked underneath the former ones
    fig : figure object
        existing figure to use if is_newfig=False
    ax : figure object
        existing axes to use when is_autostack=False
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
    """

    if is_newfig:
        fig = plt.figure(tight_layout=True, figsize=(20, 10))
        ax = fig.add_subplot(111)
    elif is_autostack:
        n = len(fig.axes)
        for i in range(n):
            fig.axes[i].change_geometry(n + 1, 1, i + 1)
        ax = fig.add_subplot(n + 1, 1, n + 1)

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
                        color=color_list[i][0],
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
                        edgecolor=color_list[i][0],
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
                mag_max = max(Ydatas[i])
                imax = int(where(Ydatas[i] == mag_max)[0])
                barlist[imax].set_color("r")

    elif type == "barchart":
        for i in range(len(Ydatas)):
            if i == 0:
                if color_list[i] != "":
                    ax.bar(
                        range(len(Xdata)),
                        Ydatas[i],
                        color=color_list[i][0],
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
                        edgecolor=color_list[i][0],
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
