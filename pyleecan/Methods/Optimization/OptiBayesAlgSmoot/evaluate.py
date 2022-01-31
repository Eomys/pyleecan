import numpy as np


def evaluate(solver, input_x):

    # Nettoyer les valeurs d'obj précédentes
    for obj in solver.problem.obj_func:
        obj.result.clear()

    # Inserer les valeurs d'entrée dans la simu
    # simu = solver.problem.simu
    # nx = input_x[0].size
    for x in input_x:
        i = 0
        for var in solver.problem.design_var:
            var.setter(solver.problem.simu, x[i])
            i += 1

        # Lancer la simu
        # TO DO Vectoriser ?
        if solver.problem.eval_func == None:
            solver.problem.simu.run()
        else:
            solver.problem.eval_func(solver.xoutput)

        for obj in solver.problem.obj_func:
            obj.result.append(obj.keeper(solver.xoutput))
    """ solver.xoutput.output_list.append()
    print(solver.problem.datakeeper_list)
    for datakeeper in solver.problem.datakeeper_list:
        print(datakeeper)
        try:
            datakeeper.result.append(datakeeper.keeper(solver.xoutput))
        except KeyboardInterrupt:
            raise KeyboardInterrupt("Stopped by the user.")
        except Exception as err:
            solver.logger.warning(
                "DataKeeper"
                + datakeeper.name
                + ".keeper execution failed:"
                + str(err)
            )
            if datakeeper.error_keeper:
                try:
                    datakeeper.result.append(
                        datakeeper.error_keeper(solver.xoutput.simu)
                    )
                except KeyboardInterrupt:
                    raise KeyboardInterrupt("Stopped by the user.")
                except Exception as err:
                    solver.logger.warning(
                        "DataKeeper"
                        + datakeeper.name
                        + ".error_keeper execution failed:"
                        + str(err)
                    )
                    datakeeper.result.append(np.nan)
            else:
                datakeeper.result.append(np.nan) """

    #Récupérer les (la) valeur d'objectif souhaitée
    result = np.atleast_2d([obj.result for obj in solver.problem.obj_func])
    print(result)

    return result.T
