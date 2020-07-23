# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d

from ...Functions.init_fig import init_subplot
from ...definitions import config_dict

COLORS = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]
FONT_NAME = config_dict["PLOT"]["FONT_NAME"]


def plot_A_3D(
    Xdata,
    Ydata,
    Zdata,
    colormap="RdBu",
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    z_min=None,
    z_max=None,
    title="",
    xlabel="",
    ylabel="",
    zlabel="",
    xticks=None,
    yticks=None,
    fig=None,
    subplot_index=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_logscale_z=False,
    is_disp_title=True,
    type="stem",
    save_path=None,
):
    """Plots a 3D graph ("stem", "surf" or "pcolor")

    Parameters
    ----------
    Xdata : ndarray
        array of x-axis values
    Ydata : ndarray
        array of y-axis values
    Zdata : ndarray
        array of z-axis values
    colormap : colormap object
        colormap prescribed by user
    x_min : float
        minimum value for the x-axis (no automated scaling in 3D)
    x_max : float
        maximum value for the x-axis (no automated scaling in 3D)
    y_min : float
        minimum value for the y-axis (no automated scaling in 3D)
    y_max : float
        maximum value for the y-axis (no automated scaling in 3D)
    z_min : float
        minimum value for the z-axis (no automated scaling in 3D)
    z_max : float
        maximum value for the z-axis (no automated scaling in 3D)
    title : str
        title of the graph
    xlabel : str
        label for the x-axis
    ylabel : str
        label for the y-axis
    zlabel : str
        label for the z-axis
    xticks : list
        list of ticks to use for the x-axis
    fig : Matplotlib.figure.Figure
        existing figure to use if is_newfig=False
    subplot_index : int
        index of subplot in which to plot
    is_logscale_x : bool
        boolean indicating if the x-axis must be set in logarithmic scale
    is_logscale_y : bool
        boolean indicating if the y-axis must be set in logarithmic scale
    is_logscale_z : bool
        boolean indicating if the z-axis must be set in logarithmic scale
    is_disp_title : bool
        boolean indicating if the title must be displayed
    type : str
        type of 3D graph : "stem", "surf", "pcolor" or "scatter"
    """

    # Set figure/subplot
    is_3d = False
    if type != "pcolor" and type != "scatter":
        is_3d = True
    fig, ax = init_subplot(fig=fig, subplot_index=subplot_index, is_3d=is_3d)

    # Plot
    if type == "stem":
        for xi, yi, zi in zip(Xdata, Ydata, Zdata):
            line = art3d.Line3D(
                *zip((xi, yi, 0), (xi, yi, zi)),
                linewidth=3.0,
                marker="o",
                markersize=5.0,
                markevery=(1, 1),
                color=COLORS[0]
            )
            ax.add_line(line)
        ax.set_xlim3d(x_max, x_min)
        ax.set_ylim3d(y_min, y_max)
        ax.set_zlim3d(z_min, z_max)
        # set correct angle
        ax.view_init(elev=20.0, azim=45)
        ax.zaxis.set_rotate_label(False)
        ax.set_zlabel(zlabel, rotation=0)
        ax.xaxis.labelpad = 30
        ax.yaxis.labelpad = 30
        ax.zaxis.labelpad = 30
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
        if yticks is not None:
            ax.yaxis.set_ticks(yticks)
        # white background
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor("w")
        ax.yaxis.pane.set_edgecolor("w")
        ax.zaxis.pane.set_edgecolor("w")
        if is_logscale_z:
            ax.zscale("log")
    elif type == "surf":
        ax.plot_surface(Xdata, Ydata, Zdata, cmap=colormap)
        ax.set_xlim3d(x_max, x_min)
        ax.set_ylim3d(y_min, y_max)
        ax.set_zlim3d(z_min, z_max)
        ax.zaxis.set_rotate_label(False)
        ax.set_zlabel(zlabel, rotation=0)
        ax.xaxis.labelpad = 30
        ax.yaxis.labelpad = 30
        ax.zaxis.labelpad = 30
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
        if yticks is not None:
            ax.yaxis.set_ticks(yticks)
        # white background
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor("w")
        ax.yaxis.pane.set_edgecolor("w")
        ax.zaxis.pane.set_edgecolor("w")
        if is_logscale_z:
            ax.zscale("log")
    elif type == "pcolor":
        c = ax.pcolormesh(Xdata, Ydata, Zdata, cmap=colormap, vmin=z_min, vmax=z_max)
        clb = fig.colorbar(c, ax=ax)
        clb.ax.set_title(zlabel, fontsize=18)
        clb.ax.tick_params(labelsize=18)
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
        if yticks is not None:
            ax.yaxis.set_ticks(yticks)
    elif type == "scatter":
        c = ax.scatter(
            Xdata, Ydata, c=Zdata, marker="s", cmap=colormap, vmin=z_min, vmax=z_max
        )
        clb = fig.colorbar(c, ax=ax)
        clb.ax.set_title(zlabel, fontsize=18)
        clb.ax.tick_params(labelsize=18)
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
        if yticks is not None:
            ax.yaxis.set_ticks(yticks)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if is_logscale_x:
        ax.xscale("log")

    if is_logscale_y:
        ax.yscale("log")

    if is_disp_title:
        ax.set_title(title)

    if is_3d:
        for item in (
            [ax.xaxis.label, ax.yaxis.label, ax.zaxis.label]
            + ax.get_xticklabels()
            + ax.get_yticklabels()
            + ax.get_zticklabels()
        ):
            item.set_fontsize(22)
    else:
        for item in (
            [ax.xaxis.label, ax.yaxis.label]
            + ax.get_xticklabels()
            + ax.get_yticklabels()
        ):
            item.set_fontsize(22)
            item.set_fontname(FONT_NAME)
    ax.title.set_fontsize(24)
    ax.title.set_fontname(FONT_NAME)

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()
