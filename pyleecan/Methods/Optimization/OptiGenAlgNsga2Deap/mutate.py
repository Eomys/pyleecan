import random
from collections.abc import Iterable
from deap.tools import mutPolynomialBounded
from ....Classes.OptiDesignVarInterval import OptiDesignVarInterval
from ....Classes.OptiDesignVarSet import OptiDesignVarSet


def mutate(self, indiv):
    """Mutate the individual design variables with different strategies according to the variables types :
        - interval : Polynomial Bounded mutation or user defined
        - set : Resampling the variable according to its initialization function
        - pyleecan : Resampling the variable according to its initialization function

    Parameters
    ----------
    solver : Solver
        solver to perform the genetic algorithm with DEAP
    indiv : individual (e.g. OptiGenAlgIndivDeap)
        individual to mutate

    Returns
    -------
    is_mutation : boolean
        True if at least one mutation occured
    """
    is_mutation = False

    for k, design_var in enumerate(indiv.design_var):
        if self.p_mutate < random.random():  # Perform mutation
            is_mutation = True

            if self.mutator == None:
                if isinstance(design_var, OptiDesignVarInterval):  # Interval variable
                    # Using polynomial bounded mutation as in Deb and al., "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II"
                    if isinstance(indiv[k], Iterable):
                        indiv[k] = mutPolynomialBounded(
                            indiv[k], 20, *design_var.space, 1
                        )[0]
                    else:
                        # Function takes list in argument and returns list
                        indiv[k] = mutPolynomialBounded(
                            [indiv[k]], 20, *design_var.space, 1
                        )[0][0]
                else:  # Uniform mutation
                    indiv[k] = random.choice(design_var.space)
            else:  # User defined mutator
                if isinstance(design_var, OptiDesignVarInterval):  # Interval variable
                    indiv[k] = self.mutator(indiv[k])
                else:
                    # TODO Allow to redefine mutators for set
                    indiv[k] = design_var.function(design_var.space)
    return is_mutation
