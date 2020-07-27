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
        xoutput.xoutput_dict[datakeeper.symbol] = [None for _ in range(self.nb_simu)]

    # TODO Parallelization
    if self.nb_proc > 1:
        pass
    else:
        nb_simu = self.nb_simu
        for idx, simulation in zip(range(nb_simu), simulation_list):
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
