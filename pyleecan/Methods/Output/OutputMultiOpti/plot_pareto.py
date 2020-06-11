import numpy as np
import matplotlib.pyplot as plt


def plot_pareto(self, obj1=0, obj2=1):
    """Plot the pareto front for 2 objective functions
    
    Parameters
    ----------
    self : OutputMultiOpti
    obj1 : str or int
        label or number of the first objective function
    obj2: str ot int
        label or number of the second objective function
    
    """

    # Pyleecan colors
    pyleecan_color = (230 / 255, 175 / 255, 0)

    # Check inputs
    if not isinstance(obj1, int) and not isinstance(obj1, str):
        raise TypeError("Expecting int or str for obj1, received", type(obj1))
    if not isinstance(obj2, int) and not isinstance(obj2, str):
        raise TypeError("Expecting int or str for obj2, received", type(obj2))

    # Get both objective function index and name
    if isinstance(obj1, int):
        idx_obj1 = obj1
        obj1 = self.fitness_names[idx_obj1]
    else:
        idx_obj1 = self.fitness_names.index(obj1)
    if isinstance(obj2, int):
        idx_obj2 = obj2
        obj2 = self.fitness_names[idx_obj2]
    else:
        idx_obj2 = self.fitness_names.index(obj2)

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
    d_v_v_iterator = range(design_var_values.shape[1])
    for sim in design_var_values.tolist():
        legend = ""
        for d_var in d_v_v_iterator:
            legend += "{:11.10}=".format(self.design_var_names[d_var])  # sim[d_var])
            if isinstance(sim[d_var], float):
                legend += " {:3.3e}\n".format(sim[d_var])
            else:
                legend += "{:>11.10}\n".format(str(sim[d_var]))
        legend_annot.append(legend[:-2])

    fig, axs = plt.subplots()

    # Plot Pareto front
    sc = axs.scatter(
        pareto[:, idx_obj1],
        pareto[:, idx_obj2],
        facecolors=pyleecan_color,
        edgecolors=(0.35, 0.35, 0.35),
        label="Pareto Front",
    )
    axs.autoscale(1, 1)
    axs.legend()
    axs.set_title("Pareto Front")
    axs.set_xlabel(obj1)
    axs.set_ylabel(obj2)

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
        annot.get_bbox_patch().set_facecolor(pyleecan_color)
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

    fig.show()
