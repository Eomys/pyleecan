# -*- coding: utf-8 -*-

from deap.tools import selNSGA2
from copy import deepcopy
from datetime import datetime
import numpy as np

from ....Classes.Output import Output
from ....Classes.XOutput import XOutput
from ....Classes.ParamExplorerValue import ParamExplorerValue
from ....Functions.Optimization.evaluate import evaluate
from ....Functions.Optimization.update import update
from ....Functions.Optimization.check_cstr import check_cstr
from ....Functions.Optimization.tournamentDCD import tournamentDCD


def create_setter(accessor, attribute):
    """
    Create a simulation setter
    """
    return lambda simu, val: setattr(eval(accessor), attribute, val)


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

    # Display information
    try:
        filename = self.get_logger().handlers[0].stream.name
        print(
            "{} Starting optimization... \n\tLog file: {}\n\tNumber of generations: {}\n\tPopulation size: {}\n".format(
                datetime.now().strftime("%H:%M:%S"),
                filename,
                self.nb_gen,
                self.size_pop,
            )
        )
    except (AttributeError, IndexError):
        print(
            "{} Starting optimization...\n\tNumber of generations: {}\n\tPopulation size: {}\n".format(
                datetime.now().strftime("%H:%M:%S"), self.nb_gen, self.size_pop
            )
        )

    try:
        # Create the toolbox
        self.create_toolbox()

        # Add the reference output to multi_output
        self.xoutput = XOutput(init_dict=self.problem.output.as_dict())

        # Add the design variable names
        paramexplorer_symbol = list(self.problem.design_var.keys())

        # Create setters to reproduce multisimulation later
        # TODO change OptiDesignVar to have a setter that takes a Simulation in argument
        paramexplorer_setter = []
        for _, d_var in self.problem.design_var.items():
            _, *objs, attr = d_var.name.split(
                "."
            )  # remove output, it assumes that OptiDesignVar.name starts with output.simu
            accessor = ".".join(objs)
            attr = attr
            paramexplorer_setter.append(create_setter(accessor, attr))

        # Get the fitness names
        fitness_names = list(self.problem.obj_func.keys())
        fitness_names.sort()

        # Set-up output data as list to be changed into ndarray at the end of the optimization
        paramexplorer_value = []
        self.xoutput.xoutput_dict["ngen"] = []
        self.xoutput.xoutput_dict["is_valid"] = []

        for fit_name in fitness_names:
            self.xoutput.xoutput_dict[fit_name] = []

        # Create the first population
        pop = self.toolbox.population(self.size_pop)

        # Start of the evaluation of the generation
        time_start_gen = datetime.now().strftime("%H:%M:%S")

        # Keep number of evalutation to create the shape
        shape = self.size_pop

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
                time_start_gen, 0, nb_error, nb_infeasible
            )
        )

        # Add pop to XOutput
        for indiv in pop:
            # Check that at every fitness values is different from inf
            is_valid = indiv.is_simu_valid and indiv.cstr_viol == 0

            if self.is_keep_all_output:
                self.xoutput.output_list.append(indiv.output)

            # is_valid
            self.xoutput.xoutput_dict["is_valid"].append(is_valid)

            # Design variable values
            paramexplorer_value.append(list(indiv))

            # Fitness values
            for i, fit_name in enumerate(fitness_names):
                self.xoutput.xoutput_dict[fit_name].append(indiv.fitness.values[i])

            # ngen
            self.xoutput.xoutput_dict["ngen"].append(0)

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
                child.output = indiv.output.copy()
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

            shape += len(to_eval)

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
                    time_start_gen, ngen, nb_error, nb_infeasible
                )
            )

            # Add pop to XOutput
            for indiv in to_eval:
                # Check that at every fitness values is different from inf
                is_valid = indiv.is_simu_valid and indiv.cstr_viol == 0

                if self.is_keep_all_output:
                    self.xoutput.output_list.append(indiv.output)

                # is_valid
                self.xoutput.xoutput_dict["is_valid"].append(is_valid)

                # Design variable values
                paramexplorer_value.append(list(indiv))

                # Fitness values
                for i, fit_name in enumerate(fitness_names):
                    self.xoutput.xoutput_dict[fit_name].append(indiv.fitness.values[i])

                # ngen
                self.xoutput.xoutput_dict["ngen"].append(ngen)

            # Sorting the population according to NSGA2
            if self.selector == None:
                pop = selNSGA2(pop + children, self.size_pop)
            else:
                pop = self.selector(pop, self.size_pop)

        # Change xoutput variables in ndarray
        paramexplorer_value = np.array(paramexplorer_value)

        self.xoutput.shape = (shape,)
        self.xoutput.nb_simu = shape
        for i, setter, symbol in zip(
            range(shape), paramexplorer_setter, paramexplorer_symbol
        ):
            self.xoutput.paramexplorer_list.append(
                ParamExplorerValue(
                    value=paramexplorer_value[:, i], setter=setter, symbol=symbol,
                )
            )

        self.xoutput.xoutput_dict["is_valid"] = np.array(
            self.xoutput.xoutput_dict["is_valid"]
        )
        self.xoutput.xoutput_dict["ngen"] = np.array(self.xoutput.xoutput_dict["ngen"])

        # Fitness values
        for fit_name in fitness_names:
            self.xoutput.xoutput_dict[fit_name] = np.array(
                self.xoutput.xoutput_dict[fit_name]
            )

        return self.xoutput

    except KeyboardInterrupt:
        # Change xoutput variables in ndarray
        paramexplorer_value = np.array(paramexplorer_value)

        self.xoutput.shape = (shape,)
        self.xoutput.nb_simu = shape
        for i, setter, symbol in zip(
            range(shape), paramexplorer_setter, paramexplorer_symbol
        ):
            self.xoutput.paramexplorer_list.append(
                ParamExplorerValue(
                    value=paramexplorer_value[:, i], setter=setter, symbol=symbol,
                )
            )

        self.xoutput.xoutput_dict["is_valid"] = np.array(
            self.xoutput.xoutput_dict["is_valid"]
        )
        self.xoutput.xoutput_dict["ngen"] = np.array(self.xoutput.xoutput_dict["ngen"])

        # Fitness values
        for fit_name in fitness_names:
            self.xoutput.xoutput_dict[fit_name] = np.array(
                self.xoutput.xoutput_dict[fit_name]
            )

        # Except keybord interruption to return the results already computed
        print("Interrupted by the user.")
        return self.xoutput
