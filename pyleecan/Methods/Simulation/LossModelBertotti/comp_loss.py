# -*- coding: utf-8 -*-
from numpy import array, nan, tile, newaxis, ones
from SciDataTool import DataTime, DataFreq, Data1D
from logging import getLogger

from ....Classes.SolutionData import SolutionData


def _comp_loss_sum(self, LossDensComps, area, k_freq):
    # get the axes
    axes_list = [axis.name for axis in LossDensComps.axes]
    freqs_idx = axes_list.index("freqs")
    comps_idx = axes_list.index("Components")

    # compute the sum over all frequencies and elements of the loss components
    comp_names = ["Hysteresis", "Eddy", "Excess"]
    alphas = [1, self.alpha_ed, self.alpha_ex]  # hyst. is propotional to freq.

    loss_dict = {}
    for comp_name in comp_names:
        axis_data = {"Components": comp_name}
        idx = LossDensComps.axes[comps_idx].values.tolist().index(comp_name)
        axes_list_ = [axis for axis in axes_list]
        axes_list_[comps_idx] += f"[{idx}]"

        data_dict = LossDensComps.get_along(*axes_list_, axis_data=axis_data)
        data_freq_sum = data_dict["LossDensComps"].sum(axis=freqs_idx)
        loss_dict[comp_name] = (area * data_freq_sum).sum()

    # compute the losses of the different speeds
    for comp_name, alpha in zip(comp_names, alphas):
        k = array(k_freq) ** alpha
        loss_dict[comp_name] = loss_dict[comp_name] * k

    # compute the sum of the components
    loss_sum = None
    for comp_name in comp_names:
        if loss_sum is None:
            loss_sum = loss_dict[comp_name]
        else:
            loss_sum = loss_dict[comp_name] + loss_sum

    return loss_sum


def comp_loss(self, output, part_label):
    """Compute the Losses"""
    # get logger
    logger = self.get_logger()

    # check inpurt
    if not "Stator" in part_label and not "Rotor" in part_label:
        logger.warning(
            f"LossModelBertotti.comp_loss(): 'part_label'"
            + f" {part_label} not implemented yet."
        )
        return None, None

    # get the simulation and the lamination
    simu = output.simu
    lam = simu.machine.get_lam_by_label(part_label)

    # get length, material and speed
    L1 = lam.L1
    mat_type = lam.mat_type
    rho = mat_type.struct.rho
    N0 = output.elec.OP.get_N0()
    group_name = part_label.lower() + " " + self.group  # TODO unifiy FEA names

    # setup meshsolution and solution list
    meshsolution = output.mag.meshsolution.get_group(group_name)

    # compute needed model parameter from material data
    success = self.comp_coeff_Bertotti(mat_type)
    if not success:
        logger.warning("LossModelBertotti: Unable to estimate model coefficents.")

    if success:
        # compute loss density
        LossDens, LossDensComps = self.comp_loss_density(meshsolution)

        # compute sum over frequencies
        axes_list = [axis.name for axis in LossDens.axes]
        freqs_idx = axes_list.index("freqs")

        loss_dens_freq_sum = LossDens.get_along(*axes_list)["LossDens"].sum(
            axis=freqs_idx
        )

        time = Data1D(name="time", unit="", values=array([0, 1]))
        # time = Data1D(name="time", unit="", values=array([0]), ) # TODO squeeze issue
        axes = [axis for axis in LossDens.axes if axis.name not in ["time", "freqs"]]

        # TODO utilize periodicity or use DataFreqs to reduce memory usage
        LossDensSum = DataTime(
            name="Losses sum",
            unit="W/kg",
            symbol="LossDensSum",
            axes=[time, *axes],
            values=tile(loss_dens_freq_sum, (2, 1)),
            # values=loss_freqs_sum[newaxis,:], # TODO squeeze issue
        )

        # Set the symmetry factor according to the machine
        if simu.mag.is_periodicity_a:
            sym, is_antiper_a, _, _ = output.get_machine_periodicity()
            sym *= is_antiper_a + 1
        else:
            sym = 1

        # compute the sum of the losses
        area = meshsolution.get_mesh().get_cell_area()
        N0_list = self.N0 if self.N0 else [N0]
        k_freq = [n / N0 for n in N0_list]

        Time = output.elec.axes_dict["time"]
        Speed = Data1D(name="speed", unit="rpm", symbol="N0", values=N0_list)

        loss_sum = _comp_loss_sum(self, LossDensComps, area, k_freq)[newaxis, :]
        loss_sum = (
            loss_sum * ones((Time.get_length(), 1))[:, newaxis]
        )  # TODO use periodicity
        loss_sum *= L1 * rho * sym
        data = DataTime(
            name=self.name, unit="W", symbol="Loss", axes=[Time, Speed], values=loss_sum
        )
        if self.get_meshsolution:
            solution = []
            meshsolution.solution = solution
            solution.append(SolutionData(field=LossDens, label="LossDens"))
            solution.append(SolutionData(field=LossDensComps, label="LossDensComps"))
            solution.append(SolutionData(field=LossDensSum, label="LossDensSum"))
            return data, meshsolution
        else:
            return data, None
    else:
        return None, None
