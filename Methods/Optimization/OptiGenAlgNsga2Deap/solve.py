# -*- coding: utf-8 -*-

from deap.tools import selNSGA2
from copy import deepcopy
from datetime import datetime

from ....Classes.Output import Output
from ....Functions.Optimization.evaluate import evaluate
from ....Functions.Optimization.update import update
from ....Functions.Optimization.check_cstr import check_cstr
from ....Functions.Optimization.tournamentDCD import tournamentDCD


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

    # Check input parameters
    self.check_optimization_input()

    try:
        # Create the toolbox
        self.create_toolbox()

        # Add the design variable names
        self.multi_output.design_var_names = list(self.problem.design_var.keys())
        self.multi_output.design_var_names.sort()

        # Add the fitness names
        self.multi_output.fitness_names = list(self.problem.obj_func.keys())
        self.multi_output.fitness_names.sort()

        # Add the reference output to multi_output
        self.multi_output.output_ref = self.problem.output

        # Create the first population
        pop = self.toolbox.population(self.size_pop)

        # Start of the evaluation of the generation
        time_start_gen = datetime.now().strftime("%H:%M:%S")

        # Evaluate the population
        nb_error = 0
        for i in range(0, self.size_pop):
            nb_error += evaluate(self, pop[i])
            print(
                "\r{}  gen {:>5}: {:>5.2f}%, {:>4} errors.".format(
                    time_start_gen, 0, (i + 1) * 100 / self.size_pop, nb_error
                ),
                end="",
            )

        # Check the constraints violation
        nb_infeasible = 0
        if len(self.problem.constraint) > 0:
            for indiv in pop:
                nb_infeasible += check_cstr(self, indiv) == False
        print(
            "\r{}  gen {:>5}: 100%, {:>4} errors,{:>4} infeasible.".format(
                time_start_gen, 0, nb_error, nb_infeasible - nb_error
            )
        )

        # Add pop to OutputMultiOpt
        for indiv in pop:
            # Check that at every fitness values is different from inf
            is_valid = (
                indiv.fitness.valid and indiv.is_simu_valid and indiv.cstr_viol == 0
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
            time_start_gen = datetime.now().strftime("%H:%M:%S")
            # Extracting parents using
            parents = tournamentDCD(pop, self.size_pop)

            # Copy new indivuals
            children = []

            for indiv in parents:
                child = self.toolbox.individual()
                for i in range(len(indiv)):
                    child[i] = deepcopy(indiv[i])
                child.output = Output(init_dict=indiv.output.as_dict())
                child.fitness = deepcopy(indiv.fitness)
                children.append(child)

            for indiv1, indiv2 in zip(children[::2], children[::-2]):
                # Crossover
                is_cross = self.cross(indiv1, indiv2)

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

            nb_error = 0
            for i in range(len(to_eval)):
                nb_error += evaluate(self, to_eval[i])
                print(
                    "\r{}  gen {:>5}: {:>5.2f}%, {:>4} errors.".format(
                        time_start_gen, ngen, (i + 1) * 100 / len(to_eval), nb_error
                    ),
                    end="",
                )

            # Check the constraints violation
            nb_infeasible = 0
            if len(self.problem.constraint) > 0:
                for indiv in to_eval:
                    nb_infeasible += check_cstr(self, indiv) == False
            print(
                "\r{}  gen {:>5}: 100%, {:>4} errors,{:>4} infeasible.".format(
                    time_start_gen, ngen, nb_error, nb_infeasible - nb_error
                )
            )
            # Add children to OutputMultiOpti
            for indiv in children:
                # Check that at every fitness values is different from inf
                is_valid = (
                    indiv.fitness.valid and indiv.is_simu_valid and indiv.cstr_viol == 0
                )

                # Add the indiv to the multi_output
                self.multi_output.add_evaluation(
                    indiv.output, is_valid, list(indiv), indiv.fitness.values, ngen
                )

            # Sorting the population according to NSGA2
            if self.selector == None:
                pop = selNSGA2(pop + children, self.size_pop)
            else:
                pop = self.selector(pop, self.size_pop)

        return self.multi_output

    except KeyboardInterrupt:
        # Except keybord interruption to return the results already computed
        print("Interrupted by the user.")
        return self.multi_output
