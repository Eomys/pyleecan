# -*- coding: utf-8 -*-
import logging
import traceback
import sys
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

    # Keep previous stdout
    orig_stdout = sys.stdout
    orig_stderr = sys.stderr
    file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f") + ".log"
    with open(file_name, "w") as log_file:
        sys.stdout = log_file
        sys.stderr = log_file

        try:
            if solver.problem.eval_func == None:
                indiv.output.simu.run()
            else:
                solver.problem.eval_func(indiv.output)

            # Sort the obj_func
            keys = list(solver.problem.obj_func.keys())
            keys.sort()

            # Add the fitness values
            fitness = []
            for key in keys:
                fitness.append(solver.problem.obj_func[key].func(indiv.output))

            indiv.fitness.values = fitness
            indiv.is_simu_valid = True

            # Reset standard output and error
            sys.stdout = orig_stdout
            sys.stderr = orig_stderr

            evaluation_failure = False  # Evaluation succeed

        except KeyboardInterrupt:
            print("Stopped by the user.")
            # Reset standard output and error
            sys.stdout = orig_stdout
            sys.stderr = orig_stderr
            raise KeyboardInterrupt("Stopped by the user.")

        except:
            # TODO logging
            traceback.print_exc()

            # Sort the obj_func
            keys = list(solver.problem.obj_func.keys())
            keys.sort()

            # Set fitness as inf
            indiv.fitness.values = [float("inf") for _ in keys]
            indiv.is_simu_valid = False

            # Reset standard output and error
            sys.stdout = orig_stdout
            sys.stderr = orig_stderr
            evaluation_failure = True  # Evaluation failed

    if stat(file_name).st_size == 0:  # Delete the file if empty
        remove(file_name)
    else:  # Add the design variables at the beggining of the file
        with open(file_name, "r") as f:
            f_lines = f.readlines()
            lines = ["Design variables :\n"]
        for i in range(len(indiv.keys)):
            lines.append(indiv.keys[i] + " : " + str(indiv[i]) + "\n")

        lines.append("\nExecution:\n")
        lines.extend(f_lines)
        with open(file_name, "w") as f:
            f.writelines(lines)

    return evaluation_failure
