import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def plot_generation(self, obj1=0, obj2=1):
    """Plot every fitness values according to the two fitness
    
    Parameters
    ----------
    self : OutputMultiOpti
    """

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
        obj1 = self.fitness_names.index(obj1)
    if isinstance(obj2, int):
        idx_obj2 = obj2
        obj2 = self.fitness_names[idx_obj2]
    else:
        obj2 = self.fitness_names.index(obj2)

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

    # Keep only valid values
    indx = np.where(is_valid)[0]

    fitness = fitness[indx]
    ngen = ngen[indx]
    fig, ax = plt.subplots()

    # Plot fitness values
    scatter = ax.scatter(
        fitness[:, idx_obj1], fitness[:, idx_obj2], s=8, c=ngen, cmap=cm
    )
    legend1 = ax.legend(
        *scatter.legend_elements(), loc="upper right", title="Generation"
    )
    ax.add_artist(legend1)
    ax.set_xlabel(obj1)
    ax.set_ylabel(obj2)
    ax.set_title("Fitness values for each individual")

    ax.autoscale()
    fig.show()
