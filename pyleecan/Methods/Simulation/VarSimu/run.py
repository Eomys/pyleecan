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
        datakeeper.result = [None] * self.nb_simu

    # Execute the reference simulation it is included in the simulation list
    # Otherwise, the reference simulation is already executed in the simulation.run method
    nb_simu = self.nb_simu
    ref_simu_index = self.ref_simu_index
    index_list = list(range(nb_simu))

    ref_simu_in_multsim = isinstance(self.ref_simu_index, int)

    if ref_simu_in_multsim:
        logger = self.get_logger()
        logger.info("Computing reference simulation")

        simulation = simulation_list.pop(ref_simu_index)
        index_list.pop(ref_simu_index)
        xoutput.simu = simulation

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

        # Set back the var_simu
        simulation.var_simu = self
        print(
            "\r["
            + "=" * (50 * (1) // (nb_simu))
            + " " * (50 - ((50) // (nb_simu)))
            + "] {:3d}%".format(((100 * 1) // (nb_simu)))
        )

    # Reuse some intermediate results from reference simulation (if requested)
    for simu in simulation_list:
        self.set_reused_data(simu, xoutput)

    # Execute the other simulations
    nb_simu = self.nb_simu
    for idx, [i, simulation] in zip(index_list, enumerate(simulation_list)):
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

        print(
            "\r["
            + "=" * (50 * (i + 1 + ref_simu_in_multsim) // (nb_simu))
            + " " * (50 - ((50 * (i + 1 + ref_simu_in_multsim)) // (nb_simu)))
            + "] {:3d}%".format(((100 * (i + 1 + ref_simu_in_multsim)) // (nb_simu))),
            end="",
        )

    # Running postprocessings
    if self.postproc_list:
        logger.info("Running var_simu postprocessings...")
        for postproc in self.postproc_list:
            postproc.run(xoutput)
