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

    # The simulation is the reference one
    if index == ref_simu_index:
        # Convert XOutput to Output
        Output = import_class("pyleecan.Classes", "Output")
        result = Output(init_dict=Output.as_dict(result))
        # Set the Output properties into XOutput
        for attr in dir(result):
            if (
                # Not method
                not callable(getattr(result, attr))
                # Not private properties
                and not attr.startswith("_")
                # Not following properties
                and attr not in ["VERSION", "logger_name", "parent"]
            ):
                setattr(xoutput, attr, getattr(result, attr))

    # Extract results
    if is_keep_all_output:
        xoutput.output_list.append(result)

    # Datakeepers
    if is_error:  # Execute error_keeper
        for datakeeper in datakeeper_list:
            if datakeeper.error_keeper is None:
                xoutput.xoutput_dict[datakeeper.symbol].result[index] = None
            else:
                xoutput.xoutput_dict[datakeeper.symbol].result[
                    index
                ] = datakeeper.error_keeper(simulation)
    else:  # Execute Normal DataKeeper
        msg = "Results: "
        for datakeeper in datakeeper_list:
            # Run and store Datakeeper
            xoutput.xoutput_dict[datakeeper.symbol].result[index] = datakeeper.keeper(
                result
            )
            # Format log
            if isinstance(
                xoutput.xoutput_dict[datakeeper.symbol].result[index], ndarray
            ):
                msg += (
                    datakeeper.symbol
                    + "=array(min="
                    + format(
                        np_min(xoutput.xoutput_dict[datakeeper.symbol].result[index]),
                        ".8g",
                    )
                    + ",max="
                    + format(
                        np_max(xoutput.xoutput_dict[datakeeper.symbol].result[index]),
                        ".8g",
                    )
                    + ")"
                )
            elif isinstance(
                xoutput.xoutput_dict[datakeeper.symbol].result[index], Data
            ) or isinstance(
                xoutput.xoutput_dict[datakeeper.symbol].result[index], VectorField
            ):
                msg += (
                    datakeeper.symbol
                    + "="
                    + type(
                        xoutput.xoutput_dict[datakeeper.symbol].result[index]
                    ).__name__
                )
            else:
                msg += (
                    datakeeper.symbol
                    + "="
                    + format(
                        xoutput.xoutput_dict[datakeeper.symbol].result[index], ".8g"
                    )
                )
            msg += ", "
        msg = msg[:-2]
        simulation.get_logger().info(msg)

        # Run Post datakeeper post-processings
        if post_keeper_postproc_list is not None:
            for postproc in post_keeper_postproc_list:
                postproc.run(result)
