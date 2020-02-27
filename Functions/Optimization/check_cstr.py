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
        is_infeasible : bool
            Individual feasibility     
    """

    keys = list(solver.problem.constraint.keys())
    keys.sort()

    # Non valid simulation violate every constraints
    if indiv.is_simu_valid == False:
        indiv.cstr_viol = len(keys)
        return True

    # Browse constraints
    for key in keys:
        constraint = solver.problem.constraint[key]

        # Compute value to compare
        var_val = constraint.get_variable(indiv.output)

        # Compare the value with the constraint
        type_const = constraint.type_const
        # print(var_val, type_const, constraint.value)
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

    return indiv.cstr_viol > 0
