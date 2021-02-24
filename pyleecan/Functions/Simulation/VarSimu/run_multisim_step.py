from numpy import ndarray, min as np_min, max as np_max

from SciDataTool import VectorField, Data
from ....Functions.Load.import_class import import_class
from logging import WARNING
from ....loggers import CONSOLE_LEVEL


def run_multisim_step(
    simulation,
    datakeeper_list,
    stop_if_error,
    post_keeper_postproc_list=None,
    simu_type=None,
):
    """
    Execute a simulation step of a multi-simulation and run datakeepers

    Parameters:
    -----------
    simulation: Simulation
        Simulation to run
    datakeeper_list
        List of datakeeper to run and update results
    stop_if_error: bool
        True: Raises an error if the simulation fails
    post_keeper_postproc_list : list
        list of postprocessing to run after the datakeeper
    simu_type : str
        To adapt the text ex: "Variable Load Results"
    """
    # Change console logger level from a specific layer (if requested)
    if (
        simulation.layer_log_warn is not None
        and simulation.layer >= simulation.layer_log_warn
    ):
        simulation.get_logger().handlers[0].level = WARNING

    # Run the simulation with/without error handling
    if stop_if_error:
        is_error = False
        result = simulation.run()
    else:
        try:
            result = simulation.run()
            is_error = False
        except Exception as err:
            print(err)
            is_error = True
            result = None

    # Revert logger level
    simulation.get_logger().handlers[0].level = CONSOLE_LEVEL

    # Datakeepers
    index = simulation.index
    if is_error:  # Execute error_keeper
        for datakeeper in datakeeper_list:
            if datakeeper.error_keeper is None:
                value = None
            else:
                value = datakeeper.error_keeper(simulation)
            if simulation.index is None:  # index == None => ref simu
                datakeeper.result_ref = value
            else:
                datakeeper.result[index] = value
    else:  # Execute Normal DataKeeper
        if simu_type is not None:
            msg = simu_type + " Results: "
        else:
            msg = "Results: "
        for datakeeper in datakeeper_list:
            # Run and store Datakeeper
            try:
                value = datakeeper.keeper(result)
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
                value = datakeeper.error_keeper(simulation)
            if simulation.index is None:  # index == None => ref simu
                datakeeper.result_ref = value
            else:
                datakeeper.result[index] = value
            # Format log
            if isinstance(value, ndarray):
                msg += (
                    datakeeper.symbol
                    + "=array(min="
                    + format(np_min(value), ".4g")
                    + ",max="
                    + format(np_max(value), ".4g")
                    + ")"
                )
            elif isinstance(value, list):
                msg += (
                    datakeeper.symbol
                    + "=list(min="
                    + format(np_min(value), ".4g")
                    + ",max="
                    + format(np_max(value), ".4g")
                    + ")"
                )
            elif isinstance(value, Data) or isinstance(value, VectorField):
                msg += datakeeper.symbol + "=" + type(value).__name__
            elif value is None:
                msg += datakeeper.symbol + "=None"
            else:
                msg += datakeeper.symbol + "=" + format(value, ".4g")
            if datakeeper.unit is not None:
                msg += " [" + datakeeper.unit + "], "
            else:
                msg += ", "
        msg = msg[:-2]
        simulation.get_logger().info(msg)

        # Run Post datakeeper post-processings
        if post_keeper_postproc_list is not None:
            for postproc in post_keeper_postproc_list:
                postproc.run(result)
    return result
