# -*- coding: utf-8 -*-
from logging import WARNING
import traceback
import sys

if sys.version_info > (3, 0):
    from io import StringIO
else:
    from StringIO import StringIO

from os import stat, remove
from datetime import datetime


def evaluate(solver, indiv):
    """Evaluate the individual according to the solver method
    
    Parameters
    ----------
    solver : Solver
        optimization solver
    indiv : individual 
        individual to evaluate
    
    Returns
    -------
    evaluation_failure : bool
        failure of the evaluation
    """
    # Get solver logger
    logger = solver.get_logger()

    tb = StringIO()  # to store the traceback in case of error

    logger.debug("Design variables :")
    for i, design_variable in enumerate(indiv.design_var_name_list):
        logger.debug(design_variable + " : " + str(indiv[i]))

    try:
        if solver.problem.eval_func == None:
            indiv.output.simu.run()
        else:
            solver.problem.eval_func(indiv.output)

        # Sort the obj_func
        obj_func_list = list(solver.problem.obj_func.keys())
        obj_func_list.sort()

        # Add the fitness values
        fitness = []
        for of in obj_func_list:
            fitness.append(solver.problem.obj_func[of].func(indiv.output))

        indiv.fitness.values = fitness
        indiv.is_simu_valid = True

        evaluation_failure = False  # Evaluation succeed

    except KeyboardInterrupt:
        raise KeyboardInterrupt("Stopped by the user.")

    except:
        # Logging
        print("The following simulation failed :", file=tb)

        if logger.level > 10:  # Log design variables values if it is not already done
            print("Design variables :", file=tb)
            for i, design_variable in enumerate(indiv.design_var_name_list):
                print(design_variable + " : " + str(indiv[i]), file=tb)

        # Log the simulation error
        traceback.print_exc(file=tb)
        logger.warning(tb.getvalue())

        # Sort the obj_func
        obj_func_list = list(solver.problem.obj_func.keys())
        obj_func_list.sort()

        # Set fitness as inf
        indiv.fitness.values = [float("inf") for _ in obj_func_list]
        indiv.is_simu_valid = False

        # Reset standard output and error
        evaluation_failure = True  # Evaluation failed

    return evaluation_failure
