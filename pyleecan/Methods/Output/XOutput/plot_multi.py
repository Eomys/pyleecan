import matplotlib.pyplot as plt
import numpy as np

from ....definitions import config_dict

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

    # Get x_data
    if x_symbol in self.keys():  # DataKeeper
        x_data = self[x_symbol]
        x_values = np.array(x_data.result)[idx]
    else:  # ParamSetter
        x_data = self.get_paramexplorer(x_symbol)
        x_values = np.array(x_data.value)[idx]

    # x_label definition
    x_label = x_symbol
    if x_data.unit not in ["", None]:
        x_label += " [{}]".format(x_data.unit)

    # Get y_data
    if y_symbol in self.keys():  # DataKeeper
        y_data = self[y_symbol]
        y_values = np.array(y_data.result)[idx]
    else:  # ParamSetter
        y_data = self.get_paramexplorer(y_symbol)
        y_values = np.array(y_data.value)[idx]

    # y_label definition
    y_label = y_symbol
    if y_data.unit not in ["", None]:
        y_label += " [{}]".format(y_data.unit)

    # Plot in new figure
    if ax is None:
        fig, ax = plt.subplots()
        if plot_type is "scatter":
            ax.scatter(x_values, y_values, c=COLORS[0])
        elif plot_type is "plot":
            sort_index = np.argsort(x_values)
            ax.plot(x_values[sort_index], y_values[sort_index])

        fig.suptitle(title, fontname=FONT_NAME)
        ax.set_xlabel(x_label, fontname=FONT_NAME)
        ax.set_ylabel(y_label, fontname=FONT_NAME)
        return fig

    # Plot in ax
    else:
        if plot_type is "scatter":
            ax.scatter(x_values, y_values)
        elif plot_type is "plot":
            sort_index = np.argsort(x_values)
            ax.plot(x_values[sort_index], y_values[sort_index])

        ax.set_title(title, fontname=FONT_NAME)
        ax.set_xlabel(x_label, fontname=FONT_NAME)
        ax.set_ylabel(y_label, fontname=FONT_NAME)
        return ax
