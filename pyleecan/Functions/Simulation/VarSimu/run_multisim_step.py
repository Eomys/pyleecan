from numpy import ndarray, min as np_min, max as np_max

from SciDataTool import VectorField, Data
from ....Functions.Load.import_class import import_class


def run_multisim_step(
    simulation,
    index,
    datakeeper_list,
    stop_if_error,
    post_keeper_postproc_list=None,
):
    """
    Execute a simulation step of a multi-simulation and run datakeepers

    Parameters:
    -----------
    simulation: Simulation
        Simulation to run
    index: int
        Index of the simulation (if None:reference simu => Skip DataKeeper)
    datakeeper_list
        List of datakeeper to run and update results
    stop_if_error: bool
        True: Raises an error if the simulation fails
    post_keeper_postproc_list : list
        list of postprocessing to run after the datakeeper
    """
    simulation.index = index
    if stop_if_error:
        is_error = False
        result = simulation.run()
    else:
        # Run simulation
        try:
            result = simulation.run()
            is_error = False
        except Exception as err:
            print(err)
            is_error = True
            result = None

    # Datakeepers
    if index is not None:  # index == None => ref simu => No DataKeeper
        if is_error:  # Execute error_keeper
            for datakeeper in datakeeper_list:
                # readability
                dk_result = datakeeper.result
                if datakeeper.error_keeper is None:
                    dk_result[index] = None
                else:
                    dk_result[index] = datakeeper.error_keeper(simulation)
        else:  # Execute Normal DataKeeper
            msg = "Results: "
            for datakeeper in datakeeper_list:
                # readability
                dk_result = datakeeper.result
                # Run and store Datakeeper
                try:
                    dk_result[index] = datakeeper.keeper(result)
                except Exception as e:
                    simulation.get_logger().error(
                        "ERROR while calling DataKeeper "
                        + datakeeper.name
                        + " for simulation "
                        + str(index)
                        + ":\n"
                        + str(e)
                    )
                    if stop_if_error:
                        raise e
                    dk_result[index] = datakeeper.error_keeper(simulation)
                # Format log
                if isinstance(dk_result[index], ndarray):
                    msg += (
                        datakeeper.symbol
                        + "=array(min="
                        + format(np_min(dk_result[index]), ".8g")
                        + ",max="
                        + format(np_max(dk_result[index]), ".8g")
                        + ")"
                    )
                elif isinstance(dk_result[index], list):
                    msg += (
                        datakeeper.symbol
                        + "=list(min="
                        + format(np_min(dk_result[index]), ".8g")
                        + ",max="
                        + format(np_max(dk_result[index]), ".8g")
                        + ")"
                    )
                elif isinstance(dk_result[index], Data) or isinstance(
                    dk_result[index], VectorField
                ):
                    msg += datakeeper.symbol + "=" + type(dk_result[index]).__name__
                elif dk_result[index] is None:
                    msg += datakeeper.symbol + "= None"
                else:
                    msg += datakeeper.symbol + "=" + format(dk_result[index], ".8g")
                msg += ", "
            msg = msg[:-2]
            simulation.get_logger().info(msg)

            # Run Post datakeeper post-processings
            if post_keeper_postproc_list is not None:
                for postproc in post_keeper_postproc_list:
                    postproc.run(result)
    return result
