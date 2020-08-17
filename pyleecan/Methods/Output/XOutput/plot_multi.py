import matplotlib.pyplot as plt
import numpy as np
from ....Methods.Output.XOutput import XOutputError


class PlotError(Exception):
    pass


def plot_multi(
    self, symbol_x, symbol_y, plot_type="scatter", idx=None, ax=None, title=None
):
    """
    Plot data from a DataKeeper for a given parameter from a ParamExplorer

    symbol_x: str
        Symbol of Datakeeper or Parameter for X axe
    symbol_y: str
        Symbol of Datakeeper of Parameter for Y axe
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

    if idx is not None:
        assert len(idx) <= len(self.input_param["shape"])
    else:
        idx = slice(None)

    if plot_type not in ["scatter", "plot"]:
        raise PlotError("Unknown plot_type {}.".format(plot_type))

    x_label = symbol_x
    try:
        x_param = self.get_paramexplorer(symbol_x)
        if x_param.unit not in ["", None]:
            x_label += " [{}]".format(x_param.unit)
        x_values = np.array(x_param[idx])
    except XOutputError:
        x_values = np.array(self[symbol_x][idx])

    y_label = symbol_y
    try:
        y_param = self.get_paramexplorer(symbol_y)
        if y_param.unit not in ["", None]:
            y_label += " [{}]".format(y_param.unit)
        y_values = np.array(y_param[idx])
    except XOutputError:
        y_values = np.array(self[symbol_y][idx])

    # Plot in new figure
    if ax is None:
        fig, ax = plt.subplots()
        if plot_type is "scatter":
            ax.scatter(x_values, y_values)
        elif plot_type is "plot":
            sort_index = np.argsort(x_values)
            ax.plot(x_values[sort_index], y_values[sort_index])

        fig.suptitle(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        return fig
    # Plot in ax
    else:
        if plot_type is "scatter":
            ax.scatter(x_values, y_values)
        elif plot_type is "plot":
            sort_index = np.argsort(x_values)
            ax.plot(x_values[sort_index], y_values[sort_index])

        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        return ax
