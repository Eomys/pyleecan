import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def plot_pareto_design_space(self, dvar1=0, dvar2=1):
    """Plot every individuals from the pareto front in the design space according to the two design variables selected
    
    Parameters
    ----------
    self : OutputMultiOpti
    dvar1 : int or str
        design variable name or position in the dict to represent
    dvar2 : int or str
        second design variable name or position in the dict to represent
    """

    # Check inputs
    if not isinstance(dvar1, int) and not isinstance(dvar1, str):
        raise TypeError("Expecting int or str for dvar1, received", type(dvar1))
    if not isinstance(dvar2, int) and not isinstance(dvar2, str):
        raise TypeError("Expecting int or str for dvar2, received", type(dvar2))

    # Get both objective function index and name
    if isinstance(dvar1, int):
        idx_dvar1 = dvar1
        dvar1 = self.design_var_names[idx_dvar1]
    else:
        dvar1 = self.design_var_names.index(dvar1)
    if isinstance(dvar2, int):
        idx_dvar2 = dvar2
        dvar2 = self.design_var_names[idx_dvar2]
    else:
        dvar2 = self.design_var_names.index(dvar2)

    # TODO define the colormap according to Pyleecan graphical chart
    # Colormap definition
    cm = LinearSegmentedColormap.from_list(
        "colormap",
        [(35 / 255, 89 / 255, 133 / 255), (250 / 255, 202 / 255, 56 / 255)],
        N=max(self.ngen),
    )

    # Get fitness and ngen
    is_valid = np.array(self.is_valid)
    fitness = np.array(self.fitness)
    ngen = np.array(self.ngen)
    design_var = np.array(self.design_var)

    # Keep only valid values
    indx = np.where(is_valid)[0]
    fitness = fitness[indx]
    ngen = ngen[indx]
    design_var = design_var[indx]

    # Get pareto front
    fitness.tolist()
    pareto = fitness

    # Get dominated values
    idx_non_dom = list(range(len(pareto)))
    N = len(pareto)
    for i in range(N):
        for j in idx_non_dom:
            if all(pareto[j] <= pareto[i]) and any(pareto[j] < pareto[i]):
                idx_non_dom.remove(i)
                break

    pareto = np.array(pareto)
    pareto = pareto[idx_non_dom]
    design_var_values = design_var[idx_non_dom]

    # Write annotations
    legend_annot = []
    p_iterator = range(pareto.shape[1])
    for sim in pareto.tolist():
        legend = ""
        for fit in p_iterator:
            legend += "{:11.10}=".format(self.fitness_names[fit])  # sim[d_var])
            if isinstance(sim[fit], float):
                legend += " {}\n".format(sim[fit])
            else:
                legend += "{:>11.10}\n".format(str(sim[fit]))
        legend_annot.append(legend[:-2])

    fig, axs = plt.subplots()

    # Plot Pareto front
    sc = axs.scatter(
        design_var_values[:, idx_dvar1],
        design_var_values[:, idx_dvar2],
        facecolors=(230 / 255, 175 / 255, 0),
        edgecolors=(0.35, 0.35, 0.35),
        label="Pareto Front",
    )
    axs.autoscale(1, 1)
    axs.legend()
    axs.set_title("Pareto Front")
    axs.set_xlabel(dvar1)
    axs.set_ylabel(dvar2)

    # Add anotations in the plot see https://stackoverflow.com/a/47166787
    annot = axs.annotate(
        "",
        xy=(0, 0),
        xytext=(20, 20),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="w"),
        arrowprops=dict(arrowstyle="->"),
    )
    annot.set_visible(False)

    def update_annot(ind):
        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        annot.set_text(legend_annot[ind["ind"][0]])
        annot.get_bbox_patch().set_facecolor(
            (230 / 255, 175 / 255, 0)
        )  # Color of the annotation background (230,175,0) from Pyleecan graphic chart
        annot.get_bbox_patch().set_alpha(0.4)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == axs:
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

    plt.show()
