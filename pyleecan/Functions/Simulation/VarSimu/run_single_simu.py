from numpy import ndarray, min as np_min, max as np_max

from SciDataTool import VectorField, Data
from ....Functions.Load.import_class import import_class


def run_single_simu(
    xoutput,
    datakeeper_list,
    simulation,
    index,
    stop_if_error,
    ref_simu_index,
    is_keep_all_output,
    post_keeper_postproc_list=None,
):
    """
    Execute a simulation and run datakeepers

    Parameters:
    -----------
    xoutput: XOutput
        Contains results
    datakeeper_list
        List of datakeeper to extract results
    simulation: Simulation
        Simulation to run
    index: int
        Index of the simulation
    stop_if_error: bool
        Raises an error if the simulation fails
    ref_simu_index: tuple
        Index of the reference simulation
    is_keep_all_output: bool
        store simulation output
    post_keeper_postproc_list : list
        list of postprocessing to run after the datakeeper
    """
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

    # if the simulation is the reference one then create new Output 
    # from XOutput content to store in the output_list, 
    # i.e. get rid of the empty XOutput part
    if index == ref_simu_index and not is_error and simulation.var_simu is None:
        Output = import_class("pyleecan.Classes", "Output")
        result = Output(init_dict=Output.as_dict(result))

    # Extract results
    if is_keep_all_output:
        xoutput.output_list.append(result)

    # Datakeepers
    if is_error:  # Execute error_keeper
        for datakeeper in datakeeper_list:
            # readability
            dk_result = xoutput.xoutput_dict[datakeeper.symbol].result
            if datakeeper.error_keeper is None:
                dk_result[index] = None
            else:
                dk_result[index] = datakeeper.error_keeper(simulation)
    else:  # Execute Normal DataKeeper
        msg = "Results: "
        for datakeeper in datakeeper_list:
            # readability
            dk_result = xoutput.xoutput_dict[datakeeper.symbol].result
            # Run and store Datakeeper
            dk_result[index] = datakeeper.keeper(result)
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
