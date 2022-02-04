# -*- coding: utf-8 -*-

from smoot.smoot import MOO
from copy import deepcopy
from datetime import datetime
import numpy as np
from pymoo.visualization.scatter import Scatter

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
    """Method to perform Bayesian optimization using SMT tools

    Parameters
    ----------
    self : OptiBayesAlgSmoot
        Solver to perform Bayesian model creation, then use a genetic algorithm

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
                datetime.now().strftime("%H:%M:%S"), filename, self.nb_iter
            )
        )
    except (AttributeError, IndexError):
        print(
            "{} Starting optimization...\n\tNumber of iterations: {}\n\t".format(
                datetime.now().strftime("%H:%M:%S"), self.nb_iter
            )
        )

    try:
        # Add the reference output to multi_output
        if isinstance(self.problem.simu.parent, Output):
            xoutput = XOutput(init_dict=self.problem.simu.parent.as_dict())
        else:
            xoutput = XOutput(simu=self.problem.simu)

        self.xoutput = xoutput

        # Set-up output data as list to be changed into ndarray at the end of the optimization
        paramexplorer_value = []
        xoutput.xoutput_dict["n_iter"] = DataKeeper(
            name="Generation number", symbol="n_iter"
        )
        xoutput.xoutput_dict["is_valid"] = DataKeeper(
            name="Individual validity", symbol="is_valid"
        )
        xoutput.xoutput_dict["x_opt"] = DataKeeper(  # need to put a better name here
            name="x opt", symbol="x_opt"
        )
        xoutput.xoutput_dict["y_opt"] = DataKeeper(  # need to put a better name here
            name="y opt", symbol="y_opt"
        )
        xoutput.xoutput_dict["x_data"] = DataKeeper(  # need to put a better name here
            name="x data", symbol="x_data"
        )
        xoutput.xoutput_dict["y_data"] = DataKeeper(  # need to put a better name here
            name="y data", symbol="y_data"
        )

        # Add datakeeper to XOutput to store additionnal values
        for dk in self.problem.datakeeper_list:
            assert dk.symbol not in xoutput.xoutput_dict
            xoutput.xoutput_dict[dk.symbol] = dk

        # Put objective functions in XOutput
        for obj_func in self.problem.obj_func:
            # obj_func is a DataKeeper instance
            xoutput.xoutput_dict[obj_func.symbol] = obj_func

        n_iter = self.nb_iter
        xlimits = np.array([var.space for var in self.problem.design_var])
        
        moo = MOO(
            n_iter=n_iter,
            criterion = 'PI',
            n_start=20,
            xlimits=xlimits,
            n_gen=10*self.nb_gen,
            pop_size=4*self.size_pop
        ) 

        moo.optimize(fun=self.evaluate)

        res = moo.result
        plot = Scatter()
        plot.add(res.F, color="red")
        plot.show()

        """ print(x_opt, y_opt)
        xoutput.xoutput_dict["x_opt"].result.append(x_opt)
        xoutput.xoutput_dict["y_opt"].result.append(y_opt)
        xoutput.xoutput_dict["x_data"].result.append(x_data)
        xoutput.xoutput_dict["y_data"].result.append(y_data) """
        # xoutput.output_list.append(x_opt)
        # xoutput.output_list.append(y_opt)
        # xoutput.output_list.append(x_data)
        # xoutput.output_list.append(y_data)

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
