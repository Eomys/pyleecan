# -*- coding: utf-8 -*-

from itertools import repeat

import matplotlib.pyplot as plt
from numpy import argmin, abs, squeeze, split, ndarray

from ...Functions.init_fig import init_subplot, init_fig
from ...definitions import config_dict

# Import values from config dict
FONT_NAME = config_dict["PLOT"]["FONT_NAME"]
FONT_SIZE_TITLE = config_dict["PLOT"]["FONT_SIZE_TITLE"]
FONT_SIZE_LABEL = config_dict["PLOT"]["FONT_SIZE_LABEL"]
FONT_SIZE_LEGEND = config_dict["PLOT"]["FONT_SIZE_LEGEND"]


def plot_A_2D(
    Xdatas,
    Ydatas,
    legend_list=[""],
    color_list=[(0, 0, 1, 0.5)],
    linestyle_list=["-"],
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
    type_plot="curve",
    fund_harm=None,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    xticks=None,
    save_path=None,
    barwidth=100,
):
    """Plots a 2D graph (curve, bargraph or barchart) comparing fields in Ydatas

    Parameters
    ----------
    Xdatas : ndarray
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
        existing figure to use if None create a new one
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
    type_plot : str
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    fund_harm : float
        frequency/order/wavenumber of the fundamental harmonic that must be displayed in red in the fft
    x_min : float
        minimum value for the x-axis
    x_max : float
        maximum value for the x-axis
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    xticks : list
        list of ticks to use for the x-axis
    save_path : str
        full path where the figure is saved if save_path is not None
    barwidth : float
        barwidth scaling factor, only if type_plot = "bargraph"
    """

    # Set figure/subplot
    is_show_fig = True if fig is None else False
    if fig is None:
        (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")

    fig, ax = init_subplot(fig=fig, subplot_index=subplot_index)

    # Number of curves on a axe
    ndatas = len(Ydatas)

    # Retrocompatibility
    if isinstance(Xdatas, ndarray):
        Xdatas = [Xdatas]

    if len(Xdatas) == 1:
        i_Xdatas = [0 for i in range(ndatas)]
    else:
        i_Xdatas = range(ndatas)

    # Expend default argument
    if 1 == len(color_list) < ndatas:
        # Set the same color for all curves
        color_list = list(repeat(color_list[0], ndatas))
    if 1 == len(linewidth_list) < ndatas:
        # Set the same color for all curves
        linewidth_list = list(repeat(linewidth_list[0], ndatas))
    if 1 == len(linestyle_list) < ndatas:
        # Set the same linestyles for all curves
        linestyle_list = list(repeat(linestyle_list[0], ndatas))
    if 1 == len(legend_list) < ndatas:
        # Set no legend for all curves
        legend_list = list(repeat("", ndatas))
        no_legend = True
    else:
        no_legend = False

    # Plot
    if type_plot == "curve":
        for i in range(ndatas):
            ax.plot(
                Xdatas[i_Xdatas[i]],
                Ydatas[i],
                color=color_list[i],
                label=legend_list[i],
                linewidth=linewidth_list[i],
                ls=linestyle_list[i],
            )
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
    elif type_plot == "bargraph":
        positions = range(-ndatas + 1, ndatas, 2)
        for i in range(ndatas):
            # width = (Xdatas[i_Xdatas[i]][1] - Xdatas[i_Xdatas[i]][0]) / ndatas
            width = Xdatas[i_Xdatas[i]][-1] / barwidth
            barlist = ax.bar(
                Xdatas[i_Xdatas[i]] + positions[i] * width / (2 * ndatas),
                Ydatas[i],
                color=color_list[i],
                width=width,
                label=legend_list[i],
            )
            if fund_harm is not None:  # Find fundamental
                imax = argmin(abs(Xdatas[i] - fund_harm))
                barlist[imax].set_edgecolor("k")
                barlist[imax].set_facecolor("k")

        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
    elif type_plot == "barchart":
        for i in range(ndatas):
            if i == 0:
                ax.bar(
                    range(len(Xdatas[i_Xdatas[i]])),
                    Ydatas[i],
                    color=color_list[i],
                    width=0.5,
                    label=legend_list[i],
                )
            else:
                ax.bar(
                    range(len(Xdatas[i_Xdatas[i]])),
                    Ydatas[i],
                    edgecolor=color_list[i],
                    width=0.5,
                    fc="None",
                    lw=1,
                    label=legend_list[i],
                )
        plt.xticks(
            range(len(Xdatas[i_Xdatas[i]])),
            [str(f) for f in Xdatas[i_Xdatas[i]]],
            rotation=90,
        )
    elif type_plot == "quiver":
        for i in range(ndatas):
            x = [e[0] for e in Xdatas[i_Xdatas[i]]]
            y = [e[1] for e in Xdatas[i_Xdatas[i]]]
            vect_list = split(Ydatas[i], 2)
            ax.quiver(x, y, squeeze(vect_list[0]), squeeze(vect_list[1]))
            ax.axis("equal")

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])

    if is_logscale_x:
        ax.set_xscale("log")

    if is_logscale_y:
        ax.set_yscale("log")

    if is_disp_title:
        ax.set_title(title)

    if is_grid:
        ax.grid()

    if ndatas > 1 and not no_legend:
        ax.legend(prop={"family": FONT_NAME, "size": FONT_SIZE_LEGEND})

    plt.tight_layout()
    for item in (
        [ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()
    ):
        item.set_fontname(FONT_NAME)
        item.set_fontsize(FONT_SIZE_LABEL)
    ax.title.set_fontname(FONT_NAME)
    ax.title.set_fontsize(FONT_SIZE_TITLE)

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()

    if is_show_fig:
        fig.show()

    return ax
