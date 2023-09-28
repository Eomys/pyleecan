import numpy as np


def evaluate(solver, input_x):
    # Clean previous obj value
    for obj in solver.problem.obj_func:
        obj.result.clear()

    for x in input_x:
        # Add simulation input value
        i = 0
        for var in solver.problem.design_var:
            var.setter(solver.problem.simu, x[i])
            i += 1

        # Start the simulation
        if solver.problem.eval_func == None:
            solver.problem.simu.run()
        else:
            solver.problem.eval_func(solver.xoutput)

        for obj in solver.problem.obj_func:
            obj.result.append(obj.keeper(solver.xoutput))

    # Get the requested result value(s)
    result = np.atleast_2d([obj.result for obj in solver.problem.obj_func])

    return result.T
