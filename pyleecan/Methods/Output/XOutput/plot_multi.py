import matplotlib.pyplot as plt
import numpy as np

from SciDataTool.Functions.Plot.plot_2D import plot_2D

from ....definitions import config_dict
from ....Methods.Output.XOutput import _get_symbol_data_
from ....Functions.Plot import dict_2D, dict_3D

COLORS = config_dict["PLOT"]["COLOR_DICT"]["COLOR_LIST"]
COLORMAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
FONT_NAME = config_dict["PLOT"]["FONT_NAME"]
FONT_SIZE_TITLE = config_dict["PLOT"]["FONT_SIZE_TITLE"]
FONT_SIZE_LABEL = config_dict["PLOT"]["FONT_SIZE_LABEL"]
FONT_SIZE_LEGEND = config_dict["PLOT"]["FONT_SIZE_LEGEND"]


class PlotError(Exception):
    pass


def plot_multi(
    self,
    x_symbol,
    y_symbol,
    c_symbol=None,
    cmap=None,
    plot_type="point",
    idx=None,
    fig=None,
    ax=None,
    title=None,
    is_show_fig=True,
    save_path=None,
    win_title=None,
):
    """2D Plot from a DataKeeper / OptiObjective / ParamExplorer as a function of another
    DataKeeper / OptiObjective / ParamExplorer

    Parameters
    ----------
    self : XOutput
        XOutput object
    x_symbol: str
        ParamExplorer or DataKeeper symbol
    y_symbol: str
        ParamExplorer or DataKeeper symbol
    c_symbol: str
        optional symbol to set the plot colors
    cmap: colormap
        optional colormap
    plot_type: str
        scatter or plot to chose plot type
    idx: slice
        To plot only some data
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        ax on which to plot the data
    title: str
        Figure or subfigure title according to ax
    is_show_fig : bool
        True to show figure after plot
    save_path : str
        full path of the png file where the figure is saved if save_path is not None
    win_title : str
        Title of the plot window

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot

    Raises
    ------
    PlotError
    """

    if idx is None:
        idx = slice(None)

    if plot_type not in ["point", "curve"]:
        raise PlotError("Unknown plot_type {}.".format(plot_type))

    # get data and labels
    x_values, x_label = _get_symbol_data_(self, x_symbol, idx)
    y_values, y_label = _get_symbol_data_(self, y_symbol, idx)

    if c_symbol is None:
        colors = COLORS[0]
    else:
        # get the color data
        c_values, _ = _get_symbol_data_(self, c_symbol, idx)
        colors = c_values[:, np.newaxis]

    # add legend
    if c_symbol is not None:
        legends = [c_symbol]
    else:
        legends = []

    if cmap is None:
        cmap = COLORMAP

    # call plot_2D function
    fig, ax = plot_2D(
        Xdatas=[x_values],
        Ydatas=[y_values],
        xlabel=x_label,
        ylabel=y_label,
        color_list=[colors],
        legend_list=legends,
        title=title,
        type_plot=plot_type,
        save_path=save_path,
        is_show_fig=is_show_fig,
        win_title=win_title,
        fig=fig,
        ax=ax,
        font_name=FONT_NAME,
        font_size_title=FONT_SIZE_TITLE,
        font_size_label=FONT_SIZE_LABEL,
        font_size_legend=FONT_SIZE_LEGEND,
    )
    return fig, ax
