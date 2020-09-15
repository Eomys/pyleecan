import numpy as np
import itertools
from ....Functions.Simulation.VarSimu.run_single_simu import run_single_simu


def run(self):
    """Run each simulation contained"""

    # Check var_simu parameters
    self.check_param()

    # Get xoutput to store results
    xoutput = self.parent.parent

    # Extact simulation list and ParamExplorerValue list
    simu_dict = self.get_simulations()

    # Fill input_parameters
    xoutput.nb_simu = simu_dict["nb_simu"]
    xoutput.paramexplorer_list = simu_dict["paramexplorer_list"]
    simulation_list = simu_dict["simulation_list"]

    # Construct results
    for datakeeper in self.datakeeper_list:
        xoutput.xoutput_dict[datakeeper.symbol] = datakeeper
        datakeeper.result = [None for _ in range(self.nb_simu)]

    # Execute the reference simulation if needed
    nb_simu = self.nb_simu
    ref_simu_index = self.ref_simu_index
    index_list = list(range(nb_simu))

    if ref_simu_index != None:
        logger = self.get_logger()
        logger.info("Computing reference simulation")

        simulation = simulation_list.pop(ref_simu_index)
        index_list.pop(ref_simu_index)

        # Run the simulation handling errors
        run_single_simu(
            xoutput,
            self.datakeeper_list,
            simulation,
            ref_simu_index,
            self.stop_if_error,
            self.ref_simu_index,
            self.is_keep_all_output,
        )
    # Execute the other (TODO parallelization)
    for idx, simulation in zip(index_list, simulation_list):
        # Skip multisimulation
        print(
            "\r["
            + "=" * ((50 * idx) // (nb_simu))
            + " " * (50 - ((50 * idx) // (nb_simu)))
            + "] {:3d}%".format(((100 * idx) // (nb_simu))),
            end="",
        )

        # Run the simulation handling errors
        run_single_simu(
            xoutput,
            self.datakeeper_list,
            simulation,
            idx,
            self.stop_if_error,
            self.ref_simu_index,
            self.is_keep_all_output,
        )

    print("\r[" + "=" * 50 + "] 100%")
