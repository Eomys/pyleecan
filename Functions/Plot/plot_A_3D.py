# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d

from ...Functions.init_fig import init_fig, init_subplot


def plot_A_3D(
    Xdata,
    Ydata,
    Zdata,
    colormap="RdBu",
    x_max=None,
    y_max=None,
    z_max=None,
    z_min=None,
    title="",
    xlabel="",
    ylabel="",
    zlabel="",
    fig=None,
    subplot_index=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_logscale_z=False,
    is_disp_title=True,
    type="stem",
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
    x_max : float
        maximum value for the x-axis (no automated scaling in 3D)
    y_max : float
        maximum value for the y-axis (no automated scaling in 3D)
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
        type of 3D graph : "stem", "surf" or "pcolor"
    """

    # Set figure/subplot
    is_3d = False
    if type != "pcolor":
        is_3d = True
    fig, ax = init_subplot(fig=fig, subplot_index=subplot_index, is_3d=is_3d)

    # Plot
    if type == "stem":
        for xi, yi, zi in zip(Xdata, Ydata, Zdata):
            line = art3d.Line3D(
                *zip((xi, yi, 0), (xi, yi, zi)),
                linewidth=1.0,
                marker="o",
                markersize=1.5,
                markevery=(1, 1)
            )
            ax.add_line(line)
        ax.set_xlim3d(x_max, -x_max)
        ax.set_ylim3d(y_max, -y_max)
        ax.set_zlim3d(0, z_max)
        # set correct angle
        ax.view_init(elev=20.0, azim=45)
        ax.zaxis.set_rotate_label(False)
        ax.set_zlabel(zlabel, rotation=0)
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
        ax.set_xlim3d(x_max, 0)
        ax.set_ylim3d(0, y_max)
        ax.set_zlim3d(-z_max, z_max)
        ax.zaxis.set_rotate_label(False)
        ax.set_zlabel(zlabel, rotation=0)
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
        clb.ax.set_title(zlabel)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if is_logscale_x:
        ax.xscale("log")

    if is_logscale_y:
        ax.yscale("log")

    if is_disp_title:
        ax.set_title(title)
