import random
from collections.abc import Iterable
from deap.tools import mutPolynomialBounded


def mutate(self, indiv):
    """ Mutate the individual design variables with different strategies according to the variables types :
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

    for k in range(len(indiv.keys)):
        if self.p_mutate < random.random():  # Perform mutation
            is_mutation = True
            if (
                indiv.design_var[indiv.keys[k]].type_var == "interval"
            ):  # Interval variable
                if self.mutator == None:
                    # Using polynomial bounded mutation as in Deb and al., "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II"
                    if isinstance(indiv[k], Iterable):
                        indiv[k] = mutPolynomialBounded(
                            indiv[k], 20, *indiv.design_var[indiv.keys[k]].space, 1
                        )[0]
                    else:
                        # Function takes list in argument and returns list
                        indiv[k] = mutPolynomialBounded(
                            [indiv[k]], 20, *indiv.design_var[indiv.keys[k]].space, 1
                        )[0][0]
                else:  # User defined mutator
                    if isinstance(indiv[k], Iterable):
                        indiv[k] = self.mutator(indiv[k])[0]
                    else:
                        indiv[k] = self.mutator([indiv[k]])[0][0]
            else:
                indiv[k] = indiv.design_var[indiv.keys[k]].function(
                    indiv.design_var[indiv.keys[k]].space
                )
    return is_mutation
