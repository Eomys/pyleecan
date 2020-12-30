# -*- coding: utf-8 -*-
from numpy import array, nan, tile, newaxis, ones_like
from SciDataTool import DataTime, DataFreq, Data1D
from logging import getLogger

from ....Classes.SolutionData import SolutionData


def comp_loss(self, output, lam):
    """Compute the Losses"""
    # get logger
    logger = self.get_logger()

    # get the simulation and output
    simu = output.simu

    # setup meshsolution and solution list
    mag_meshsol = output.mag.meshsolution
    meshsolution = mag_meshsol.get_group(self.group)

    # get length and material
    L1 = lam.L1
    mat_type = lam.mat_type
    rho = mat_type.struct.rho

    # compute needed model parameter from material data
    success = self.comp_coeff_Bertotti(mat_type)
    if not success:
        logger.warning("LossModelBertotti: Unable to estimate model coefficents.")

    if success:
        # compute loss density
        LossDens = self.comp_loss_norm(mag_meshsol)

        # compute sum over frequencies
        axes_list = [axis.name for axis in LossDens.axes]
        freqs_idx = [
            idx for idx, axis_name in enumerate(axes_list) if axis_name == "freqs"
        ]
        if len(freqs_idx) > 1:
            raise Exception("more than one freqs axis found")  # TODO improve error msg
        if len(freqs_idx) == 0:
            raise Exception("no freqs axis found")  # TODO improve error msg

        loss_sum = LossDens.get_along(*axes_list)["LossDens"].sum(axis=freqs_idx[0])

        time = Data1D(name="time", unit="", values=array([0, 1]))
        # time = Data1D(name="time", unit="", values=array([0]), ) # TODO squeeze issue
        axes = [axis for axis in LossDens.axes if axis.name not in ["time", "freqs"]]

        # TODO utilize periodicity or use DataFreqs to reduce memory usage
        loss_sum_ = DataTime(
            name="Losses sum",
            unit="W/kg",
            symbol="LossDensSum",
            axes=[time, *axes],
            values=tile(loss_sum, (2, 1)),
            # values=loss_sum[newaxis,:], # TODO squeeze issue
        )

        # Set the symmetry factor according to the machine
        if simu.mag.is_periodicity_a:
            sym, is_antiper_a, _, _ = output.get_machine_periodicity()
            sym *= is_antiper_a + 1
        else:
            sym = 1

        # compute the sum of the losses
        area = meshsolution.get_mesh().get_cell_area()
        t = output.simu.input.time.get_data()
        Time = Data1D(name="time", unit="s", symbol="t", values=t, is_components=False)

        loss_sum = (area * loss_sum * L1 * rho * sym).sum()
        loss_sum *= ones_like(Time.values)
        data = DataTime(
            name=self.name, unit="W", symbol="Loss", axes=[Time], values=loss_sum
        )
        if self.get_meshsolution:
            solution = []
            meshsolution.solution = solution
            solution.append(SolutionData(field=LossDens, label="LossDens"))
            solution.append(SolutionData(field=loss_sum_, label="LossDensSum"))
            return data, meshsolution
        else:
            return data, None
    else:
        return None, None
