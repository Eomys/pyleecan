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

        # Add the fitness values, handle exception for each fitness
        fitness = []
        for obj_func in solver.problem.obj_func:
            try:
                fitness.append(float(obj_func.keeper(indiv.output)))
            # Raise KeyboardInterrupt to stop optimization
            except KeyboardInterrupt:
                raise KeyboardInterrupt

            # Except error and try to compute the error_keeper
            except Exception as err:
                logger.warning(
                    "Objectif computation " + obj_func.name + " failed:" + err
                )
                if obj_func.error_keeper is None:  # Set fitness value as infinity
                    fitness.append(float("inf"))
                else:
                    try:
                        fitness.append(float(obj_func.error_keeper(indiv.output)))
                    # Raise KeyboardInterrupt to stop optimization
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    # Set the fitness value as infinity
                    except Exception as err:
                        logger.warning(
                            "Objectif error computation "
                            + obj_func.name
                            + " failed:"
                            + err
                        )
                        fitness.append(float("inf"))

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

        # Set fitness as inf
        indiv.fitness.values = [float("inf") for _ in solver.problem.obj_func]
        indiv.is_simu_valid = False

        # Reset standard output and error
        evaluation_failure = True  # Evaluation failed

    return evaluation_failure
