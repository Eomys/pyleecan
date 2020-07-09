# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import where, argmin, abs, squeeze, split

from ...Functions.init_fig import init_subplot, init_fig


def plot_A_2D(
    Xdata,
    Ydatas,
    legend_list=[""],
    color_list=[(0, 0, 1, 0.5)],
    linewidth_list=[3],
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
    y_min=None,
    y_max=None,
    xticks=None,
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
    linewidth_list : list
        list of line width to use for each curve
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
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    is_fund : bool
        boolean indicating if the bar corresponding to the fundamental must be displayed in red
    fund_harm : float
        frequency of the fundamental harmonic
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    xticks : list
        list of ticks to use for the x-axis
    """

    # Set figure/subplot
    if fig is None:
        (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")
    fig, ax = init_subplot(fig=fig, subplot_index=subplot_index)

    # Expend default argument
    if len(color_list) < len(Ydatas) and len(color_list) == 1:
        # Set the same color for all curves
        color_list = [color_list[0] for Y in Ydatas]
    if len(linewidth_list) < len(Ydatas) and len(linewidth_list) == 1:
        # Set the same color for all curves
        linewidth_list = [linewidth_list[0] for Y in Ydatas]
    if len(legend_list) < len(Ydatas) and len(legend_list) == 1:
        # Set no legend for all curves
        legend_list = ["" for Y in Ydatas]
        no_legend = True
    else:
        no_legend = False

    # Plot
    if type == "curve":
        for i in range(len(Ydatas)):
            ax.plot(
                Xdata,
                Ydatas[i],
                color=color_list[i],
                label=legend_list[i],
                linewidth=linewidth_list[i],
            )
    elif type == "bargraph":
        for i in range(len(Ydatas)):
            width = Xdata[1] - Xdata[0]
            if i == 0:
                barlist = ax.bar(
                    Xdata,
                    Ydatas[i],
                    color=color_list[i],
                    width=width,
                    label=legend_list[i],
                )
            else:
                barlist = ax.bar(
                    Xdata,
                    Ydatas[i],
                    edgecolor=color_list[i],
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
                barlist[imax].set_color("k")
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
    elif type == "barchart":
        for i in range(len(Ydatas)):
            if i == 0:
                ax.bar(
                    range(len(Xdata)),
                    Ydatas[i],
                    color=color_list[i],
                    width=0.5,
                    label=legend_list[i],
                )
            else:
                ax.bar(
                    range(len(Xdata)),
                    Ydatas[i],
                    edgecolor=color_list[i],
                    width=0.5,
                    fc="None",
                    lw=1,
                    label=legend_list[i],
                )
        plt.xticks(range(len(Xdata)), [str(f) for f in Xdata], rotation=90)
    elif type == "quiver":
        for i in range(len(Ydatas)):
            x = [e[0] for e in Xdata]
            y = [e[1] for e in Xdata]
            vect_list = split(Ydatas[i], 2)
            ax.quiver(x, y, squeeze(vect_list[0]), squeeze(vect_list[1]))
            ax.axis("equal")

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim([y_min, y_max])

    if is_logscale_x:
        ax.xscale("log")

    if is_logscale_y:
        ax.yscale("log")

    if is_disp_title:
        ax.set_title(title)

    if is_grid:
        ax.grid()

    if len(Ydatas) > 1 and not no_legend:
        ax.legend()

    plt.tight_layout()
    for item in (
        [ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()
    ):
        item.set_fontsize(22)
    ax.title.set_fontsize(24)
    return ax
