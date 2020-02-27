import numpy as np
import matplotlib.pyplot as plt


def get_pareto(self):
    """Return the Output from the pareto front
    
    Parameters
    ----------
    self : OutputMultiOpti
    
    Returns
    -------
    pareto : [dict]
        list of dictionnary containing Output, fitness and ngen from the pareto front
    """

    # Get fitness and ngen
    is_valid = np.array(self.is_valid)
    fitness = np.array(self.fitness)
    outputs = np.array(self.outputs)
    ngen = np.array(self.ngen)

    # Keep only valid values
    indx = np.where(is_valid)[0]
    fitness = fitness[indx]
    outputs = outputs[indx]
    ngen = ngen[indx]

    # Get pareto front
    # Get unique values
    indx_unique = []
    values = []
    fit_list = fitness.tolist()
    for i in range(len(fit_list)):
        if fit_list[i] not in values:
            values.append(fit_list[i])
            indx_unique.append(i)

    fitness = fitness[indx_unique]
    outputs = outputs[indx_unique]
    ngen = ngen[indx_unique]

    # Get dominated values
    iterator = range(len(fitness))
    idx_non_dom = list(iterator)
    for i in iterator:
        for j in idx_non_dom:
            if all(fitness[j] <= fitness[i]) and any(fitness[j] < fitness[i]):
                idx_non_dom.remove(i)
                break

    # Extract the pareto front
    fitness = fitness[idx_non_dom]
    outputs = outputs[idx_non_dom]
    ngen = ngen[idx_non_dom]

    # Fill pareto
    pareto = []
    for i in range(outputs.size):
        pareto.append({"fitness": fitness[i], "output": outputs[i], "ngen": ngen[i]})

    return pareto
