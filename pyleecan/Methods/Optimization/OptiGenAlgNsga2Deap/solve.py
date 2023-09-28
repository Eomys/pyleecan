# -*- coding: utf-8 -*-

from deap.tools import selNSGA2
from copy import deepcopy
from datetime import datetime
import numpy as np

from ....Classes.Output import Output
from ....Classes.XOutput import XOutput
from ....Classes.DataKeeper import DataKeeper
from ....Classes.ParamExplorerSet import ParamExplorerSet
from ....Functions.Optimization.evaluate import evaluate
from ....Functions.Optimization.update import update
from ....Functions.Optimization.check_cstr import check_cstr
from ....Functions.Optimization.tournamentDCD import tournamentDCD


def create_setter(accessor, attribute):
    """
    Create a simulation setter
    """
    return lambda simu, val: setattr(eval(accessor), attribute, val)


def solve(self, xoutput=None):
    """Method to perform NSGA-II using DEAP tools

    Parameters
    ----------
    self : OptiGenAlgNsga2Deap
        Solver to perform NSGA-II

    Returns
    -------
    multi_output : OutputMultiOpti
        class containing the results
    xoutput : XOutput
        class containing the results of the simulations
    """

    logger = self.get_logger()

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
        # Keep number of evalutation to create the shape
        shape = self.size_pop

        # Create the toolbox
        self.create_toolbox()

        # Add the reference output to multi_output
        if xoutput is not None:
            xoutput = xoutput
        else:
            xoutput = XOutput(simu=self.problem.simu.copy())

        self.xoutput = xoutput

        # Fitness symbol
        fitness_symbol = [of.symbol for of in self.problem.obj_func]

        # Set-up output data as list to be changed into ndarray at the end of the optimization
        paramexplorer_value = []
        xoutput.xoutput_dict["ngen"] = DataKeeper(
            name="Generation number", symbol="ngen"
        )
        xoutput.xoutput_dict["is_valid"] = DataKeeper(
            name="Individual validity", symbol="is_valid"
        )
        # Add datakeeper to XOutput to store additionnal values
        for dk in self.problem.datakeeper_list:
            assert dk.symbol not in xoutput.xoutput_dict
            xoutput.xoutput_dict[dk.symbol] = dk

        # Put objective functions in XOutput
        for obj_func in self.problem.obj_func:
            # obj_func is a DataKeeper instance
            xoutput.xoutput_dict[obj_func.symbol] = obj_func

        # Create the first population
        pop = self.toolbox.population(self.size_pop)

        # Evaluate the population
        nb_error = 0
        for i in range(0, self.size_pop):
            time = datetime.now().strftime("%H:%M:%S")
            print_gen_simu(time, 0, i, self.size_pop, nb_error, pop)
            nb_error += evaluate(self, pop[i])
            print_obj(self.problem.obj_func, pop[i])

        # Check the constraints violation
        nb_infeasible = 0
        if len(self.problem.constraint) > 0:
            time = datetime.now().strftime("%H:%M:%S")
            for indiv in pop:
                nb_infeasible += check_cstr(self, indiv) == False
        print(
            "\r{}  gen {:>5}: Finished, {:>4} errors,{:>4} infeasible.\n".format(
                time, 0, nb_error, nb_infeasible
            )
        )

        # Add pop to XOutput
        for indiv in pop:
            # Check that at every fitness values is different from inf
            is_valid = indiv.is_simu_valid and indiv.cstr_viol == 0

            if self.is_keep_all_output:
                xoutput.output_list.append(indiv.output)

            # is_valid
            xoutput.xoutput_dict["is_valid"].result.append(is_valid)

            # Design variable values
            paramexplorer_value.append(list(indiv))

            # Add fitness values to DataKeeper
            for i, symbol in enumerate(fitness_symbol):
                xoutput.xoutput_dict[symbol].result.append(indiv.fitness.values[i])

            # ngen
            xoutput.xoutput_dict["ngen"].result.append(0)

        if self.selector == None:
            pop = selNSGA2(pop, self.size_pop)
        else:
            parents = self.selector(pop, self.size_pop)

        ############################
        # LOOP FOR EACH GENERATION #
        ############################
        for ngen in range(1, self.nb_gen):
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
                time = datetime.now().strftime("%H:%M:%S")
                print_gen_simu(time, ngen, i, self.size_pop, nb_error, to_eval)
                nb_error += evaluate(self, to_eval[i])
                print_obj(self.problem.obj_func, to_eval[i])

            # Check the constraints violation
            nb_infeasible = 0
            if len(self.problem.constraint) > 0:
                time = datetime.now().strftime("%H:%M:%S")
                for indiv in to_eval:
                    nb_infeasible += check_cstr(self, indiv) == False
            print(
                "\r{}  gen {:>5}: Finished, {:>4} errors,{:>4} infeasible.\n".format(
                    time, ngen, nb_error, nb_infeasible
                )
            )

            # Add pop to XOutput
            for indiv in to_eval:
                # Check that at every fitness values is different from inf
                is_valid = indiv.is_simu_valid and indiv.cstr_viol == 0

                if self.is_keep_all_output:
                    xoutput.output_list.append(indiv.output)

                # is_valid
                xoutput.xoutput_dict["is_valid"].result.append(is_valid)

                # Design variable values
                paramexplorer_value.append(list(indiv))

                # Fitness values
                for i, symbol in enumerate(fitness_symbol):
                    xoutput.xoutput_dict[symbol].result.append(indiv.fitness.values[i])
                # ngen
                xoutput.xoutput_dict["ngen"].result.append(ngen)

            # Sorting the population according to NSGA2
            if self.selector == None:
                pop = selNSGA2(pop + children, self.size_pop)
            else:
                pop = self.selector(pop, self.size_pop)

        # Change xoutput variables in ndarray
        paramexplorer_value = np.array(paramexplorer_value)

        # Storing number of simulations
        xoutput.nb_simu = shape

        # Save design variable values in ParamExplorerSet
        for i, param_explorer in enumerate(self.problem.design_var):
            if param_explorer._setter_str is None:
                setter = param_explorer._setter_func
            else:
                setter = param_explorer._setter_str
            xoutput.paramexplorer_list.append(
                ParamExplorerSet(
                    name=param_explorer.name,
                    unit=param_explorer.unit,
                    symbol=param_explorer.symbol,
                    setter=setter,
                    value=paramexplorer_value[:, i].tolist(),
                )
            )

        # Delete toolbox so that classes created with DEAP remains after the optimization
        self.delete_toolbox()

        return xoutput

    except KeyboardInterrupt:
        # Except keybord interruption to return the results already computed
        logger.info("Interrupted by the user.")
        # Change xoutput variables in ndarray
        paramexplorer_value = np.array(paramexplorer_value)

        # Storing number of simulations
        xoutput.nb_simu = shape

        # Save design variable values in ParamExplorerSet
        for i, param_explorer in enumerate(self.problem.design_var):
            xoutput.paramexplorer_list.append(
                ParamExplorerSet(
                    name=param_explorer.name,
                    unit=param_explorer.unit,
                    symbol=param_explorer.symbol,
                    setter=param_explorer.setter,
                    value=paramexplorer_value[:, i].tolist(),
                )
            )

        # Delete toolbox so that classes created with DEAP remains after the optimization
        self.delete_toolbox()

        return xoutput

    except Exception as err:
        logger.error("{}: {}".format(type(err).__name__, err))
        raise err


def print_gen_simu(time, gen_id, simu_id, size_pop, nb_error, to_eval):
    print(
        "\r{}  gen {:>5}: simu {}/{} ({:>5.2f}%), {:>4} errors.".format(
            time,
            gen_id,
            (simu_id + 1),
            size_pop,
            (simu_id) * 100 / size_pop,
            nb_error,
        )
    )
    msg = "Design Variables: "
    for ii in range(len(to_eval[simu_id])):
        msg += (
            to_eval[simu_id].design_var[ii].symbol
            + ": "
            + format(to_eval[simu_id][ii], ".2e")
            + ", "
        )
    print(msg[:-2])


def print_obj(obj_func, indiv):
    msg = "Objectives: "
    for ii in range(len(obj_func)):
        msg += (
            obj_func[ii].symbol + ": " + format(indiv.fitness.values[ii], ".2e") + ", "
        )
    print(msg[:-2] + "\n")
