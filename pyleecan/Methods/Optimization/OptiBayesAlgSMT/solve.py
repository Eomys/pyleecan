# -*- coding: utf-8 -*-

from deap.tools import selNSGA2
from copy import deepcopy
from datetime import datetime
import numpy as np
from smt.applications import EGO

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
        if isinstance(self.problem.simu.parent, Output):
            xoutput = XOutput(init_dict=self.problem.simu.parent.as_dict())
        else:
            xoutput = XOutput(simu=self.problem.simu.copy())

        self.xoutput = xoutput


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
        n_iter = 6

        ego = EGO(n_iter=n_iter)

        x_opt, y_opt, _, x_data, y_data = ego.optimize(fun=obj_func)
        xoutput.output_list.append(x_opt, y_opt,x_data, y_data)
        
        return xoutput

    except KeyboardInterrupt:
        # Except keybord interruption to return the results already computed
        logger.info("Interrupted by the user.")
        # Change xoutput variables in ndarray
        
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
