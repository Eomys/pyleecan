# -*- coding: utf-8 -*-


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
    bool : bool
        success of the evaluation

    """

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
        return 0
    except:
        # TODO logging
        # print("error")
        # traceback.print_exc()
        # Sort the obj_func
        keys = list(solver.problem.obj_func.keys())
        keys.sort()

        # Set fitness as inf
        indiv.fitness.values = [float("inf") for _ in keys]
        indiv.is_simu_valid = False

        return 1
