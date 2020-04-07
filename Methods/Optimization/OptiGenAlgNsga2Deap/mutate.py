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

    for k, design_var_name in enumerate(indiv.design_var_name_list):
        if self.p_mutate < random.random():  # Perform mutation
            is_mutation = True

            if self.mutator == None:
                if (
                    indiv.design_var[design_var_name].type_var == "interval"
                ):  # Interval variable
                    # Using polynomial bounded mutation as in Deb and al., "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II"
                    if isinstance(indiv[k], Iterable):
                        indiv[k] = mutPolynomialBounded(
                            indiv[k], 20, *indiv.design_var[design_var_name].space, 1
                        )[0]
                    else:
                        # Function takes list in argument and returns list
                        indiv[k] = mutPolynomialBounded(
                            [indiv[k]], 20, *indiv.design_var[design_var_name].space, 1
                        )[0][0]
                else:
                    indiv[k] = indiv.design_var[design_var_name].function(
                        indiv.design_var[design_var_name].space
                    )
            else:  # User defined mutator
                if (
                    indiv.design_var[design_var_name].type_var == "interval"
                ):  # Interval variable
                    indiv[k] = self.mutator(indiv[k])
                else:
                    # TODO Allow to redefine mutators for pyleecan types or set
                    indiv[k] = indiv.design_var[design_var_name].function(
                        indiv.design_var[design_var_name].space
                    )
    return is_mutation
