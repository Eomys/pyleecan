import numpy as np

def evaluate(solver, input_x):

    # Nettoyer les valeurs d'obj précédentes
    for obj in solver.problem.obj_func:
        obj.result.clear()

    for x in input_x:
        # Inserer les valeurs d'entrée dans la simu
        i = 0
        for var in solver.problem.design_var:
            var.setter(solver.problem.simu, x[i])
            i += 1

        # Lancer la simu
        if solver.problem.eval_func == None:
            solver.problem.simu.run()
        else:
            solver.problem.eval_func(solver.xoutput)

        for obj in solver.problem.obj_func:
            obj.result.append(obj.keeper(solver.xoutput))

    #Récupérer les (la) valeurs d'objectif souhaitées
    result = np.atleast_2d([obj.result for obj in solver.problem.obj_func])
    print(result)

    return result.T
