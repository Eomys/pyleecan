import numpy as np
import matplotlib.pyplot as plt
from ....Classes.OptiObjective import OptiObjective


def get_pareto_index(self):
    """Return index of individuals in the pareto

    Parameters
    ----------
    self: XOutput

    Returns
    -------
    idx_non_dom: list
        list of index of non dominated individuals
    """

    # Gather fitness results
    data = [
        val.result
        for _, val in self.xoutput_dict.items()
        if isinstance(val, OptiObjective)
    ]
    fitness = np.array(data).T

    # Get fitness values and ngen
    is_valid = np.array(self["is_valid"])

    # Keep only valid values
    indx = np.where(is_valid)
    fitness = fitness[indx]

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

    return idx_non_dom
