import numpy as np


def run(self):
    """Run each simulation contained in """

    # Check var_simu parameters
    self.check_param()

    # Get xoutput to store results
    xoutput = self.parent.parent

    # Extact simulations
    simu_dict = self.get_simulations()

    # Fill input_parameters
    xoutput.input_param["shape"] = simu_dict["shape"]
    xoutput.input_param["symbol"] = [
        param_setter.symbol for param_setter in self.paramsetter_list
    ]
    xoutput.input_param["value"] = simu_dict["value"]
    simu_array = simu_dict["simulation"]

    # Construct results
    for datakeeper in self.datakeeper_list:
        xoutput.xoutput_dict[datakeeper.name] = np.ndarray(
            simu_array.shape, dtype=datakeeper.dtype
        )

    # TODO Parallelization
    if self.nb_proc > 1:
        pass
    else:
        with np.nditer(simu_array, flags=["multi_index", "refs_ok"]) as simu_iterator:
            nb_simu = self.nb_simu
            for idx, simulation in enumerate(simu_iterator):
                # Skip multisimulation
                print(
                    "\r["
                    + "=" * ((50 * idx) // (nb_simu))
                    + " " * (50 - ((50 * idx) // (nb_simu)))
                    + "] {:3d}%".format(((100 * idx) // (nb_simu))),
                    end="",
                )
                simulation = simulation.flat[0]
                if self.stop_if_error:
                    is_error = False
                    result = simulation.run()
                else:
                    # Run simulation
                    try:
                        result = simulation.run()
                        is_error = False
                    except:
                        is_error = True

                # Extract results
                if self.is_keep_all_output:
                    xoutput.output_list.append(result)

                # Datakeepers
                if is_error:
                    # Execute error_keeper if error
                    for datakeeper in self.datakeeper_list:
                        if datakeeper.error_keeper is None:
                            xoutput.xoutput_dict[datakeeper.name][
                                simu_iterator.multi_index
                            ] = None
                        else:
                            xoutput.xoutput_dict[datakeeper.name][
                                simu_iterator.multi_index
                            ] = datakeeper.error_keeper(simulation)
                else:
                    if idx == self.ref_simu_index:
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
                    for datakeeper in self.datakeeper_list:
                        xoutput.xoutput_dict[datakeeper.name][
                            simu_iterator.multi_index
                        ] = datakeeper.keeper(result)

        print("\r[" + "=" * 50 + "] 100%")
