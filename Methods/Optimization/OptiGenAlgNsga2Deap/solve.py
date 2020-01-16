# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
from deap.tools import selNSGA2, selTournamentDCD, cxOnePoint
from copy import deepcopy
import random
import numpy as np
from datetime import datetime

import time
import inspect
from pyleecan.Classes.Output import Output

# from pyleecan.Classes.OptiGenAlgIndivDeap import OptiGenAlgIndivDeap
from pyleecan.Functions.Optimization.evaluate import evaluate
from pyleecan.Functions.Optimization.update import update


class MissingProblem(Exception):
    def __init__(self, message):
        self.message = message


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

    if self.problem == None:
        raise MissingProblem(
            "The problem has not been defined, please add a problem to OptiGenAlgNsga2Deap"
        )

    # Create the toolbox
    self.create_toolbox()

    # Add the reference output to multi_output
    self.multi_output.output_ref = self.problem.output

    # Create the first population
    pop = self.toolbox.population(self.size_pop)

    # Evaluate the population
    nb_error = 0
    for i in range(0, self.size_pop):
        nb_error += evaluate(self, pop[i])
        print(
            "\rgen 0: {:>3}%, {:>4} errors.".format(
                (i + 1) * 100 / self.size_pop, nb_error
            ),
            end="",
        )
    print("\n")

    # Add pop to OutputMultiOpt
    for indiv in pop:
        # Check that at every fitness values is different from NaN
        is_valid = (
            indiv.fitness.valid
            and sum([j == float("inf") for j in indiv.fitness.values]) == 0
        )

        # Add the indiv to the multi_output
        self.multi_output.add_evaluation(
            indiv.output, is_valid, list(indiv), indiv.fitness.values, 0
        )

    if self.selector == None:
        pop = selNSGA2(pop, self.size_pop)
    else:
        parents = self.selector(pop, self.size_pop)

    ############################
    # LOOP FOR EACH GENERATION #
    ############################
    for ngen in range(1, self.nb_gen):
        print(datetime.now().strftime("%H:%M:%S"), "Generation:", ngen)
        # Extracting parents
        parents = []

        # for _ in range(len(pop)):
        #     pass
        # TODO constraint
        parents = selTournamentDCD(pop, self.size_pop)

        # start = time.time()
        # Copy new indivuals
        children = []

        for indiv in parents:
            child = self.toolbox.individual()
            for i in range(len(indiv)):
                child[i] = indiv[i]
            child.output = Output(init_dict=indiv.output.as_dict())
            child.fitness = deepcopy(indiv.fitness)
            children.append(child)

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
                update(indiv1)

            is_mutation = self.mutate(indiv2)
            if is_cross or is_mutation:
                update(indiv2)

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
        print("\n")

        # Add children to OutputMultiOpti
        for indiv in children:
            # Check that at every fitness values is different from NaN
            is_valid = (
                indiv.fitness.valid
                and sum([j == float("inf") for j in indiv.fitness.values]) == 0
            )
            # Add the indiv to the multi_output
            self.multi_output.add_evaluation(
                indiv.output, is_valid, list(indiv), indiv.fitness.values, ngen,
            )

        # Sorting the population according to NSGA2
        if self.selector == None:
            pop = selNSGA2(pop + children, self.size_pop)
        else:
            pop = self.selector(pop, self.size_pop)

    return self.multi_output
