import numpy as np
import matplotlib.pyplot as plt
from ....Classes.DataKeeper import DataKeeper


def plot_pareto(self, x_symbol, y_symbol, ax=None, title=None):
    """Plot the pareto front for 2 objective functions
    
    Parameters
    ----------
    self : XOutput
    x_symbol : str
        symbol of the first objective function
    y_symbol: str 
        symbol of the second objective function
    
    """

    # Pyleecan colors
    pyleecan_color = (230 / 255, 175 / 255, 0)

    idx = 0

    # Gather fitness results
    data = [
        val.result
        for _, val in self.xoutput_dict.items()
        if isinstance(val, DataKeeper)
    ]
    fitness = np.array(data).T

    # Get fitness values and ngen
    is_valid = np.array(self["is_valid"])
    ngen = np.array(self["ngen"])

    design_var_list = [pe.value for pe in self.paramexplorer_list]
    design_var = np.array(design_var_list).T

    # Keep only valid values
    indx = np.where(is_valid)
    fitness = fitness[indx]
    ngen = ngen[indx]
    design_var = design_var[indx]

    # Get x_data
    if x_symbol in self.keys():  # DataKeeper
        x_data = self[x_symbol]
        x_values = np.array(x_data.result)[indx]
    else:  # ParamSetter
        x_data = self.get_paramexplorer(x_symbol)
        x_values = np.array(x_data.value)[indx]

    # x_label definition
    x_label = x_symbol
    if x_data.unit not in ["", None]:
        x_label += " [{}]".format(x_data.unit)

    # Get y_data
    if y_symbol in self.keys():  # DataKeeper
        y_data = self[y_symbol]
        y_values = np.array(y_data.result)[indx]
    else:  # ParamSetter
        y_data = self.get_paramexplorer(y_symbol)
        y_values = np.array(y_data.value)[indx]

    # y_label definition
    y_label = y_symbol
    if y_data.unit not in ["", None]:
        y_label += " [{}]".format(y_data.unit)

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
        legend = f"Individual Nr. {idx_non_dom[idx]}\n"
        for ii, symbol in enumerate(design_var_symbols):
            legend += "{:11.10}=".format(symbol)  # sim[d_var])
            if isinstance(sim[ii], float):
                legend += " {:3.3e}\n".format(sim[ii])
            else:
                legend += "{:>11.10}\n".format(str(sim[ii]))
        legend_annot.append(legend[:-2])
    if ax is None:
        fig, ax = plt.subplots()
        return_ax = False
    else:
        return_ax = True
        fig = ax.get_figure()

    # Plot Pareto front
    sc = ax.scatter(
        x_values[idx_non_dom],
        y_values[idx_non_dom],
        facecolors=pyleecan_color,
        edgecolors=(0.35, 0.35, 0.35),
        label="Pareto Front",
    )
    ax.autoscale(1, 1)

    ax.set_title("Pareto Front")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

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
        """ Update annotation """
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

    if return_ax:
        return ax
    else:
        fig.show()
