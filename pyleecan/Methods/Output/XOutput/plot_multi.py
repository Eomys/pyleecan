import matplotlib.pyplot as plt
import numpy as np

from ....definitions import config_dict
from ....Methods.Output.XOutput import _get_symbol_data_

COLORS = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]
FONT_NAME = config_dict["PLOT"]["FONT_NAME"]


class PlotError(Exception):
    pass


def plot_multi(
    self, x_symbol, y_symbol, plot_type="scatter", idx=None, ax=None, title=None
):
    """
    Plot data from a DataKeeper for a given parameter from a ParamExplorer

    x_symbol: str
        ParamExplorer or DataKeeper symbol
    y_symbol: str
        ParamExplorer or DataKeeper symbol
    plot_type: str
        scatter or plot to chose plot type
    idx: slice
        To plot only some data
    ax: matplotlib.pyplot.Axe
        To put the plot in a specific ax
    title: str
        Figure or subfigure title according to ax

    Returns
    -------
    fig or ax

    Raises
    ------
    PlotError
    """

    if idx is None:
        idx = slice(None)

    if plot_type not in ["scatter", "plot"]:
        raise PlotError("Unknown plot_type {}.".format(plot_type))

    # get data and labels
    x_values, x_label = _get_symbol_data_(self, x_symbol, idx)
    y_values, y_label = _get_symbol_data_(self, y_symbol, idx)

    # Plot in new figure
    if ax is None:
        fig, ax = plt.subplots()
        if plot_type == "scatter":
            ax.scatter(x_values, y_values, c=COLORS[0])
        elif plot_type == "plot":
            sort_index = np.argsort(x_values)
            ax.plot(x_values[sort_index], y_values[sort_index])

        fig.suptitle(title, fontname=FONT_NAME)
        ax.set_xlabel(x_label, fontname=FONT_NAME)
        ax.set_ylabel(y_label, fontname=FONT_NAME)
        return fig

    # Plot in ax
    else:
        if plot_type == "scatter":
            ax.scatter(x_values, y_values)
        elif plot_type == "plot":
            sort_index = np.argsort(x_values)
            ax.plot(x_values[sort_index], y_values[sort_index])

        ax.set_title(title, fontname=FONT_NAME)
        ax.set_xlabel(x_label, fontname=FONT_NAME)
        ax.set_ylabel(y_label, fontname=FONT_NAME)
        return ax
