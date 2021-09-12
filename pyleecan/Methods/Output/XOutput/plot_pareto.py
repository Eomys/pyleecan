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
    self : XOutput
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

    # Gather fitness results
    data = [
        val.result
        for _, val in self.xoutput_dict.items()
        if isinstance(val, OptiObjective)
    ]
    fitness = np.array(data).T

    # Get fitness values and ngen
    is_valid = np.array(self["is_valid"].result)
    # ngen = np.array(self["ngen"].result)  # unused

    design_var_list = [pe.value for pe in self.paramexplorer_list]
    design_var = np.array(design_var_list).T

    # Keep only valid values
    indx = np.where(is_valid)
    fitness = fitness[indx]
    # ngen = ngen[indx]   # unused
    design_var = design_var[indx]

    # get data and labels
    x_values, x_label = _get_symbol_data_(self, x_symbol, indx)
    y_values, y_label = _get_symbol_data_(self, y_symbol, indx)

    # Get pareto front
    pareto = fitness

    # Get dominated values
    idx_non_dom = list(range(len(pareto)))
    N = len(pareto)
    for i in range(N):
        for j in idx_non_dom:
            if all(pareto[j] <= pareto[i]) and any(pareto[j] < pareto[i]):
                idx_non_dom.remove(i)
                break

    pareto = pareto[idx_non_dom]
    design_var_values = design_var[idx_non_dom]

    # Write annotations
    legend_annot = []

    design_var_symbols = [pe.symbol for pe in self.paramexplorer_list]

    for idx, sim in enumerate(design_var_values.tolist()):
        legend = f"Individual Nr. {indx[0][idx_non_dom[idx]]}\n"
        for ii, symbol in enumerate(design_var_symbols):
            legend += "{:11.10}=".format(symbol)  # sim[d_var])
            if isinstance(sim[ii], float):
                legend += " {:3.3e}\n".format(sim[ii])
            else:
                legend += "{:>11.10}\n".format(str(sim[ii]))
        legend_annot.append(legend[:-1])
    if ax is None:
        fig, ax = plt.subplots()
        return_ax = False
    else:
        return_ax = True
        fig = ax.get_figure()

    if c_symbol is None:
        colors = pyleecan_color
    else:
        # get the color data
        c_values, _ = _get_symbol_data_(self, c_symbol, indx)
        colors = c_values[idx_non_dom][:, np.newaxis]

    if cmap is None:
        cmap = plt.cm.jet

    # Plot Pareto front
    sc = ax.scatter(
        x_values[idx_non_dom][:, np.newaxis],
        y_values[idx_non_dom][:, np.newaxis],
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
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if grid:
        ax.set_axisbelow(True)
        ax.grid()

    # Add anotations in the plot see https://stackoverflow.com/a/47166787
    annot = ax.annotate(
        "",
        xy=(0, 0),
        xytext=(20, 20),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="w"),
        arrowprops=dict(arrowstyle="->"),
    )
    annot.set_visible(False)

    def update_annot(ind):
        """Update annotation"""
        # Get ind position
        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos

        # Set the annotation
        annot.set_text(legend_annot[ind["ind"][0]])
        annot.get_bbox_patch().set_facecolor(pyleecan_color)
        annot.get_bbox_patch().set_alpha(0.4)

    def hover(event):
        # Check if annotation is visible
        vis = annot.get_visible()

        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()

    if is_show_fig:
        fig.show()

    if return_ax:
        return ax
    else:
        fig.show()
