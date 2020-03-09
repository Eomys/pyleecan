try:
    from deap.tools import cxOnePoint
except ImportError:
    cxOnePoint = None

import random


def cross(self, indiv1, indiv2):
    """Perform the crossover (One crossover by default)
    
    Parameters
    ----------
    self : OptiGenNsga2Deap
        Optimization solver

    indiv1 : individual 
        first individual to modify
    indiv2 : individual 
        second individual to modify

    Returns
    -------
    is_cross : bool
        True if the crossover append
    """

    if random.random() < self.p_cross:
        if self.crossover == None:
            if cxOnePoint == None:
                raise ImportError("deap module is needed.")
            else:
                cxOnePoint(indiv1, indiv2)
        else:
            self.crossover(indiv1, indiv2)

        return True
    else:
        return False
