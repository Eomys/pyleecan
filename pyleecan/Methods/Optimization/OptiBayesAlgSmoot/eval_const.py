import numpy as np


def eval_const(solver, constraint, input_x):
    """
    Evaluate the constraint at given points x
    """
    constraint_values = []

    for x in input_x:
        i = 0
        for var in solver.problem.design_var:
            var.setter(solver.problem.simu, x[i])
            i += 1

        const_value = constraint.get_variable(solver.xoutput)
        if constraint.type_const == "<=":
            constraint_values.append(const_value - constraint.value)
        elif constraint.type_const == ">=":
            constraint_values.append(constraint.value - const_value)

    return constraint_values
