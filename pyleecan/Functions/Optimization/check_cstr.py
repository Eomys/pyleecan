# -*- coding: utf-8 -*-


def check_cstr(solver, indiv):
    """Check the number of constraints violations of the individual

    Parameters
    ----------
    solver : Solver
        Global optimization problem solver
    indiv : individual
        Individual of the population

    Returns
    -------
    is_feasible : bool
        Individual feasibility
    """

    # Non valid simulation violate every constraints
    if indiv.is_simu_valid == False:
        indiv.cstr_viol = len(solver.problem.constraint)
        return True  # To not add errors to infeasible

    # Browse constraints
    for constraint in solver.problem.constraint:
        # Compute value to compare
        var_val = constraint.keeper(indiv.output)

        # Compare the value with the constraint
        type_const = constraint.type_const

        if type_const == "<=":
            if var_val > constraint.value:
                indiv.cstr_viol += 1
        elif type_const in ["==", "="]:
            if var_val != constraint.value:
                indiv.cstr_viol += 1
        elif type_const == ">=":
            if var_val < constraint.value:
                indiv.cstr_viol += 1
        elif type_const == "<":
            if var_val >= constraint.value:
                indiv.cstr_viol += 1
        elif type_const == ">":
            if var_val <= constraint.value:
                indiv.cstr_viol += 1
        else:
            raise ValueError("Wrong type of constraint")

    return indiv.cstr_viol == 0
