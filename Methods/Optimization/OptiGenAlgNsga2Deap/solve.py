# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
from deap.tools import selNSGA2, selTournamentDCD, cxOnePoint
from copy import deepcopy
import random
import numpy as np
from datetime import datetime
import traceback
import time

from pyleecan.Classes.Output import Output
from pyleecan.Classes.OptiGenAlgIndivDeap import OptiGenAlgIndivDeap
from pyleecan.Functions.Optimization.evaluate import evaluate


def solve(self):
    """Method to perform NSGA-II using DEAP tools
    
    Parameters
    ----------
    self : OptiGenAlgNsga2Deap
        Solver to perform NSGA-II

    Returns
    -------
    multi_output : OutputMultiOpti
        class containing the results
    """

    # Add the reference output to multi_output
    self.multi_output.output_ref = self.problem.output

    # Create the first population
    self.gen_pop()

    # Evaluate the population
    nb_error = 0
    for i in range(0, self.size_pop):
        nb_error += evaluate(self, self.pop[i])
        print(
            "\rgen 0: {:>3}%, {:>4} errors.".format(
                (i + 1) * 100 / self.size_pop, nb_error
            ),
            end="",
        )
    print("\n")

    # Add pop to OutputMultiOpt
    for indiv in self.pop:
        # Check that at every fitness values is different from NaN
        is_valid = (
            indiv.fitness.valid
            and sum([j == float("inf") for j in indiv.fitness.values]) == 0
        )

        # Add the indiv to the multi_output
        self.multi_output.add_evaluation(
            indiv.output, is_valid, indiv.design_var_value, indiv.fitness.values, 0
        )

    if self.selector == None:
        self.pop = selNSGA2(self.pop, len(self.pop))
    else:
        parents = self.selector(self.pop, len(self.pop))

    ############################
    # LOOP FOR EACH GENERATION #
    ############################
    for ngen in range(1, self.nb_gen):
        print(datetime.now().strftime("%H:%M:%S"), "Generation:", ngen)
        # Extracting parents
        parents = []

        # for _ in range(len(self.pop)):
        #     pass
        # TODO constraint
        parents = selTournamentDCD(self.pop, len(self.pop))

        start = time.time()
        # Copy new indivuals
        children = []
        for indiv in parents:
            indiv2 = OptiGenAlgIndivDeap(
                Output(init_dict=indiv.output.as_dict()), indiv.design_var
            )
            for i in range(len(indiv)):
                indiv2[i] = indiv[i]

            indiv2.fitness = deepcopy(indiv.fitness)
            children.append(indiv2)

        print("Time copy :", time.time() - start)

        start = time.time()
        for indiv1, indiv2 in zip(children[::2], children[::-2]):
            # Crossover
            is_cross = False
            if random.random() < self.p_cross:
                is_cross = True
                if self.crossover == None:
                    cxOnePoint(indiv1, indiv2)

            # Mutation
            is_mutation = self.mutate(indiv1)

            if is_cross or is_mutation:
                indiv1.update()

            is_mutation = self.mutate(indiv2)
            if is_cross or is_mutation:
                indiv2.update()
        print("Time cross mut :", time.time() - start)

        start = time.time()
        # Evaluate the children
        to_eval = []
        for indiv in children:
            if indiv.fitness.valid == False:
                to_eval.append(indiv)

        for indiv in to_eval:
            evaluate(self, indiv)

        # Evaluate the population
        nb_error = 0
        for i in range(len(to_eval)):
            nb_error += evaluate(self, to_eval[i])
            print(
                "\rgen {}: {:>3}%, {:>4} errors.".format(
                    ngen, (i + 1) * 100 / len(to_eval), nb_error
                ),
                end="",
            )

        print("\nTime evaluation :", time.time() - start)

        start = time.time()
        # Add children to OutputMultiOpti
        for indiv in children:
            # Check that at every fitness values is different from NaN
            is_valid = (
                indiv.fitness.valid
                and sum([np.isnan(j) for j in indiv.fitness.values]) == 0
            )
            # Add the indiv to the multi_output
            self.multi_output.add_evaluation(
                indiv.output,
                is_valid,
                indiv.design_var_value,
                indiv.fitness.values,
                ngen,
            )
        print("Time add res :", time.time() - start)

        start = time.time()
        # Sorting the population according to NSGA2
        if self.selector == None:
            self.pop = selNSGA2(self.pop + children, len(self.pop))
        else:
            self.pop = self.selector(self.pop, len(self.pop))
        print("Time selection pop:", time.time() - start)

    return self.multi_output
