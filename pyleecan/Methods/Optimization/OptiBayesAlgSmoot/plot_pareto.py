import numpy as np
import matplotlib.pyplot as plt
from ....Classes.OptiObjective import OptiObjective
from ....Methods.Output.XOutput import _get_symbol_data_


def plot_pareto(
    self,
    x_symbol,
    y_symbol,
    c_symbol=None,
    cmap=None,
    ax=None,
    title=None,
    grid=False,
    is_show_fig=True,
    save_path=None,
):
    """Plot the pareto front for 2 objective functions

    Parameters
    ----------
    self : OptiBayesAlgSmoot
    x_symbol : str
        symbol of the first objective function
    y_symbol: str
        symbol of the second objective function
    c_symbol: str
        optional symbol to set the plot colors
    cmap: colormap
        optional colormap
    is_show_fig : bool
        True to show figure after plot
    save_path : str
        full path of the png file where the figure is saved if save_path is not None
    """

    # Pyleecan colors
    pyleecan_color = (230 / 255, 175 / 255, 0)

    # Get the correct objectives
    idx = 0
    idy = 0
    for i in range(len(self.problem.obj_func)):
        if self.problem.obj_func[i].symbol == x_symbol:
            idx = i
        if self.problem.obj_func[i].symbol == y_symbol:
            idy = i

    x_values = [
        self.xoutput["y_opt"].result[i][idx]
        for i in range(len(self.xoutput["y_opt"].result))
    ]
    y_values = [
        self.xoutput["y_opt"].result[i][idy]
        for i in range(len(self.xoutput["y_opt"].result))
    ]

    colors = pyleecan_color

    if cmap is None:
        cmap = plt.cm.jet

    if ax is None:
        fig, ax = plt.subplots()
        return_ax = False
    else:
        return_ax = True
        fig = ax.get_figure()

    # Plot Pareto front
    sc = ax.scatter(
        x_values,
        y_values,
        # facecolors=colors,
        c=colors,
        edgecolors=(0.35, 0.35, 0.35),
        label="Pareto Front",
        cmap=cmap,
    )
    # Add legend
    if c_symbol is not None:
        legend1 = ax.legend(*sc.legend_elements(), loc="upper right", title=c_symbol)
        ax.add_artist(legend1)

    ax.autoscale(1, 1)

    ax.set_title("Pareto Front")
    ax.set_xlabel(x_symbol)
    ax.set_ylabel(y_symbol)

    if grid:
        ax.set_axisbelow(True)
        ax.grid()

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()

    if is_show_fig:
        fig.show()

    if return_ax:
        return ax
    else:
        fig.show()
