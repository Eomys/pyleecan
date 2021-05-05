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
    ax=None,
    title=None,
    is_show_fig=True,
    save_path=None,
    win_title=None,
):
    """
    Plot data from a DataKeeper for a given parameter from a ParamExplorer

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
    ax: matplotlib.pyplot.Axe
        To put the plot in a specific ax
    title: str
        Figure or subfigure title according to ax
    is_show_fig : bool
        True to show figure after plot
    save_path : str
        full path of the png file where the figure is saved if save_path is not None

    Returns
    -------
    fig or ax

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
    plot_2D(
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
        font_name=FONT_NAME,
        font_size_title=FONT_SIZE_TITLE,
        font_size_label=FONT_SIZE_LABEL,
        font_size_legend=FONT_SIZE_LEGEND,
    )
    # RET_FIG = False
    # if ax is None:
    #     fig, ax = plt.subplots()
    #     fig.suptitle(title, fontname=FONT_NAME)
    #     RET_FIG = True
    # else:
    #     ax.set_title(title, fontname=FONT_NAME)

    # # plot
    # if plot_type == "scatter":
    #     plot = ax.scatter(x_values, y_values, c=colors)
    # elif plot_type == "curve":
    #     sort_index = np.argsort(x_values)
    #     plot = ax.plot(x_values[sort_index], y_values[sort_index], c=colors)

    # # add legend
    # if c_symbol is not None:
    #     legend1 = ax.legend(*plot.legend_elements(), loc="upper right", title=c_symbol)
    #     ax.add_artist(legend1)

    # ax.set_xlabel(x_label, fontname=FONT_NAME)
    # ax.set_ylabel(y_label, fontname=FONT_NAME)

    # if save_path is not None:
    #     fig.savefig(save_path)
    #     plt.close()

    # if is_show_fig:
    #     fig.show()

    # # return
    # if RET_FIG:
    #     return fig
    # else:
    #     return ax
