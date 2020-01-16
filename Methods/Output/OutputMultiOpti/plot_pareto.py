import numpy as np
import matplotlib.pyplot as plt


def plot_pareto(self):
    """Plot every fitness values with the pareto front for 2 fitness
    
    Parameters
    ----------
    self : OutputMultiOpti
    """

    # TODO Add a feature to return the design_varibles of each indiv from the Pareto front

    # Get fitness and ngen
    is_valid = np.array(self.is_valid)
    fitness = np.array(self.fitness)
    ngen = np.array(self.ngen)

    # Keep only valid values
    indx = np.where(is_valid)[0]

    fitness = fitness[indx]
    ngen = ngen[indx]
    _, ax = plt.subplots()

    # Plot fitness values
    scatter = ax.scatter(fitness[:, 0], fitness[:, 1], c=ngen)
    legend1 = ax.legend(
        *scatter.legend_elements(), loc="upper right", title="Generation"
    )
    ax.add_artist(legend1)

    # Get pareto front
    pareto = list(np.unique(fitness, axis=0))

    # Get dominated values
    to_remove = []
    N = len(pareto)
    for i in range(N):
        for j in range(N):
            if all(pareto[j] <= pareto[i]) and any(pareto[j] < pareto[i]):
                to_remove.append(pareto[i])
                break

    # Remove dominated values
    for i in to_remove:
        for l in range(len(pareto)):
            if all(i == pareto[l]):
                pareto.pop(l)
                break

    pareto = np.array(pareto)

    # Plot Pareto front
    ax.scatter(pareto[:, 0], pareto[:, 1], facecolors="none", edgecolors="r")
    ax.plot(pareto[:, 0], pareto[:, 1], "--", color="r")
    ax.autoscale()
    plt.show()
