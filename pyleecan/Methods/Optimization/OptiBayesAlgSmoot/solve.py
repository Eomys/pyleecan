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
    """Method to perform Bayesian optimization using Smoot tools

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
            xoutput = XOutput(
                init_dict=self.problem.simu.parent.as_dict(keep_function=True)
            )
        else:
            xoutput = XOutput(simu=self.problem.simu)

        self.xoutput = xoutput

        # Set-up output data as list to be changed into ndarray at the end of the optimization
        paramexplorer_value = []
        xoutput.xoutput_dict["n_iter"] = DataKeeper(
            name="Generation number", symbol="n_iter"
        )

        xoutput.xoutput_dict["x_opt"] = DataKeeper(  # need to put a better name here
            name="x opt", symbol="x_opt"
        )
        xoutput.xoutput_dict["y_opt"] = DataKeeper(  # need to put a better name here
            name="y opt", symbol="y_opt"
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

        const = [
            lambda x, i=i: self.eval_const(self.problem.constraint[i], x)
            for i in range(len(self.problem.constraint))
        ]

        time = datetime.now()

        moo = MOO(
            n_iter=self.nb_iter,
            criterion=self.criterion,
            n_start=self.nb_start,
            xlimits=xlimits,
            # const=const,
            verbose=True,
            n_gen=self.nb_gen,
            pop_size=self.size_pop,
        )

        moo.optimize(fun=self.evaluate)

        final_time = datetime.now() - time

        print(
            "{} End of optimization, solved in {}.\n".format(
                datetime.now().strftime("%H:%M:%S"), final_time
            )
        )
        res = moo.result

        xoutput.xoutput_dict["x_opt"].result = res.X.tolist()
        xoutput.xoutput_dict["y_opt"].result = res.F.tolist()

        return xoutput

    except KeyboardInterrupt:
        # Except keybord interruption to return the results already computed
        logger.info("Interrupted by the user.")
        # Change xoutput variables in ndarray

        return xoutput

    except Exception as err:
        logger.error("{}: {}".format(type(err).__name__, err))
        raise err
