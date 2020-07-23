import matplotlib.pyplot as plt
import numpy as np


class PlotError(Exception):
    pass


def plot_multi(self, param, data, plot_type="scatter", idx=None, ax=None, title=None):
    """
    Plot data from a DataKeeper for a given parameter from a ParamExplorer

    param: str
        ParamExplorer symbol
    data: str
        DataKeeper symbol
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

    x_values = self.get_param_array(param)[idx]
    y_values = self[data][idx]

    if ax is None:
        fig, ax = plt.subplots()
        if plot_type is "scatter":
            ax.scatter(x_values, y_values)
        elif plot_type is "plot":
            sort_index = np.argsort(x_values)
            ax.plot(x_values[sort_index], y_values[sort_index])

        # ax.set_title("Pareto Front")
        fig.suptitle(title)
        ax.set_xlabel(param)
        ax.set_ylabel(data)
        return fig
    else:
        if plot_type is "scatter":
            ax.scatter(x_values, y_values)
        elif plot_type is "plot":
            sort_index = np.argsort(x_values)
            ax.plot(x_values[sort_index], y_values[sort_index])

        ax.set_title(title)
        ax.set_xlabel(param)
        ax.set_ylabel(data)
        return ax
