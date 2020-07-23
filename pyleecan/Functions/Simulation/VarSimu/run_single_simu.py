def run_single_simu(
    xoutput,
    datakeeper_list,
    simulation,
    multi_index,
    stop_if_error,
    ref_simu_index,
    is_keep_all_output,
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
    multi_index: tuple
        Index of the simulation
    stop_if_error: bool
        Raises an error if the simulation fails
    ref_simu_index: tuple
        Index of the reference simulation
    is_keep_all_output: bool
        store simulation output
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

    # Extract results
    if is_keep_all_output:
        xoutput.output_list.append(result)

    # Datakeepers
    if is_error:
        # Execute error_keeper if error
        for datakeeper in datakeeper_list:
            if datakeeper.error_keeper is None:
                xoutput.xoutput_dict[datakeeper.symbol][multi_index] = None
            else:
                xoutput.xoutput_dict[datakeeper.symbol][
                    multi_index
                ] = datakeeper.error_keeper(simulation)
    else:
        if multi_index == ref_simu_index:
            for attr in dir(result):
                if (
                    # Not method
                    not callable(getattr(result, attr))
                    # Not private properties
                    and not attr.startswith("_")
                    # Not following properties
                    and attr not in ["VERSION", "logger_name", "parent",]
                ):
                    setattr(xoutput, attr, getattr(result, attr))

        # Execute keepers
        for datakeeper in datakeeper_list:
            xoutput.xoutput_dict[datakeeper.symbol][multi_index] = datakeeper.keeper(
                result
            )
