import numpy as np
import itertools
from ....Functions.Simulation.VarSimu.run_multisim_step import run_multisim_step
from ....Functions.Simulation.VarSimu.log_datakeeper_step_result import (
    log_datakeeper_step_result,
)
from ....Functions.Load.import_class import import_class


def run(self):
    """Run the multi-simulation
    The VarSimu object must be in a Simulation object (and not a VarSimu one)

    Parameters
    ----------
    self : VarSimu
        A VarSimu object
    """

    logger = self.get_logger()
    Output = import_class("pyleecan.Classes", "Output")

    # Check var_simu parameters
    self.check_param()  # Check isinstance(self.parent, Simulation)

    # Get xoutput to store results (created in Simulation.run)
    xoutput = self.parent.parent

    # Create reference simulation
    ref_simu = self.parent.copy(keep_function=True)
    ref_simu.var_simu = self.var_simu  # var_simu default is None
    ref_simu.index = None
    ref_simu.layer = self.parent.layer + 1

    # Generate simulation list and ParamExplorerValue list
    simu_dict = self.generate_simulation_list(ref_simu)

    # Check if one of the simulation from the list matches the reference one
    ref_simu_index = None
    for ii, simu in enumerate(simu_dict["simulation_list"]):
        if simu == ref_simu:
            ref_simu_index = ii
            break
    if self.NAME == "Variable Load" and ref_simu_index is None:
        logger.warning(
            "Reference Operating point is not in OP_matrix, one extra simulation will be computed"
        )

    # Fill/initialize input/output parameters
    nb_simu = len(simu_dict["simulation_list"])
    xoutput.nb_simu = nb_simu
    self.nb_simu = nb_simu
    xoutput.paramexplorer_list = simu_dict["paramexplorer_list"]
    simulation_list = simu_dict["simulation_list"]
    if self.is_keep_all_output:
        xoutput.output_list = [None] * self.nb_simu
    keeper_list = list()  # Copy keeper to store results in xoutput and not in simu
    for datakeeper in self.datakeeper_list:
        keeper_list.append(datakeeper.copy(keep_function=True))
        xoutput.xoutput_dict[datakeeper.symbol] = keeper_list[-1]
        keeper_list[-1].result = [None] * self.nb_simu

    # Run Reference simulation
    if ref_simu.layer == 2:
        logger.info("    Computing reference simulation for " + self.NAME)
    else:
        logger.info("Computing reference simulation for " + self.NAME)

    progress = 0  # For progress bar
    nb_simu += 1  # Count reference simulation in progress bar

    # Run the simulation & call DataKeeper and post-proc handling errors
    xoutput_ref = run_multisim_step(
        ref_simu,
        datakeeper_list=keeper_list,  # datakeeper.result will be updated (if needed)
        stop_if_error=True,  # Reference simulation must be correct
        post_keeper_postproc_list=self.post_keeper_postproc_list,
        simu_type=self.NAME,
    )
    # Save reference xoutput (if requested)
    if self.is_keep_all_output:
        if ref_simu_index is None:
            xoutput.xoutput_ref = xoutput_ref
        else:  # Avoid duplicating the XOutput
            xoutput.xoutput_ref_index = ref_simu_index

    progress += 1
    print_progress_bar(nb_simu, progress, ref_simu.layer)

    # Store the Ouput part of the xoutput_ref into the main xoutput
    ref_out_dict = Output.as_dict(xoutput_ref)
    if "simu" in ref_out_dict:  # Avoid erasing original simulation
        ref_out_dict.pop("simu")
    ref_out_dict.pop("__class__")
    for key, value in ref_out_dict.items():
        setattr(xoutput, key, value)

    # Reuse some intermediate results from reference simulation (if requested)
    for ii, simu in enumerate(simulation_list):
        # Log only for first simulation
        self.set_reused_data(
            simu,
            xoutput_ref,
            is_log=ii == 0,
            simu_type=self.NAME,
        )

    # Update the postprocessing list if needed
    if self.pre_keeper_postproc_list is not None:
        # Different post between simu list and ref simu
        for simu in simulation_list:
            simu.postproc_list = self.pre_keeper_postproc_list

    # Execute the simulation list
    for idx, simu_step in enumerate(simulation_list):
        # Display simulation progress
        log_step_simu(
            idx, self.nb_simu, xoutput.paramexplorer_list, logger, simu_step.layer
        )
        simu_step.index = idx
        if idx != ref_simu_index:
            # Run the simulation & call DataKeeper and post-proc handling errors
            xoutput_step = run_multisim_step(
                simu_step,
                keeper_list,  # datakeeper.result will be updated (if needed)
                self.stop_if_error,
                post_keeper_postproc_list=self.post_keeper_postproc_list,
                simu_type=self.NAME,
            )
            if self.is_keep_all_output:
                xoutput.output_list[idx] = xoutput_step
        else:
            if simu_step.layer == 2:
                logger.info(
                    "    Simulation matches reference one: Skipping computation"
                )
            else:
                logger.info("Simulation matches reference one: Skipping computation")
            # Copy results from reference
            for keeper in keeper_list:
                keeper.result[idx] = keeper.result_ref
            if self.is_keep_all_output:
                xoutput.output_list[idx] = xoutput_ref
            # Print DataKeeper content
            log_datakeeper_step_result(simu_step, keeper_list, idx, self.NAME)
        progress += 1
        print_progress_bar(nb_simu, progress, simu_step.layer)

    # Running postprocessings
    if self.postproc_list:
        logger.info("Running " + self.NAME + " postprocessings...")
        for postproc in self.postproc_list:
            postproc.run(xoutput)


def log_step_simu(index, nb_simu, paramexplorer_list, logger, layer):
    """Add in the log some information about the simulation about to run
    Ex: "Running simulation 3/4 with Id=-135.41881, Iq=113.62987"

    Parameters
    ----------
    index : int
        Index of the simulation about to run
    nb_simu : int
        Total number of simulation to run
    paramexplorer_list : list
        List of ParamExplorer to get the modification of the simu
    logger : Logger
        Logger to use (info)
    """

    if layer == 2:
        msg = "    "
    else:
        msg = ""
    InputCurrent = import_class("pyleecan.Classes", "InputCurrent")
    msg += "Running simulation " + str(index + 1) + "/" + str(nb_simu) + " with "
    for param_exp in paramexplorer_list:
        value = param_exp.get_value()[index]
        if isinstance(value, InputCurrent):
            msg += "N0=" + format(value.N0, ".6g") + " [rpm]"
            msg += ", Id=" + format(value.Id_ref, ".4g") + " [Arms]"
            msg += ", Iq=" + format(value.Iq_ref, ".4g") + " [Arms], "
        elif isinstance(value, (list, np.ndarray)):
            msg += param_exp.symbol
            msg += "="
            msg += format(value)
            msg += ", "
        else:
            try:
                data_str = format(value, ".8g")
            except:
                data_str = "'NA'"
            msg += param_exp.symbol
            msg += "="
            msg += data_str
            msg += ", "
    msg = msg[:-2]
    logger.info(msg)


def print_progress_bar(Nsimu, index, layer):
    """Print the progress bar
    Ex: "[=========================                         ]  50%"

    Parameters
    ----------
    Nsimu : int
        Total number of simulation
    index : int
        Index of the simulation about to run
    """
    if layer == 2:
        msg = "               "
    else:
        msg = ""
    print(
        "\r"
        + msg
        + "["
        + "=" * (50 * index // (Nsimu))
        + " " * (50 - ((50 * index) // (Nsimu)))
        + "] {:3d}%".format(((100 * index) // (Nsimu)))
    )
