# -*- coding: utf-8 -*-

from numpy import array, nan, tile, newaxis, ones_like
from SciDataTool import DataTime, DataFreq, Data1D

from ....Classes.SolutionData import SolutionData
from ....Functions.getattr_recursive import getattr_recursive

from logging import getLogger


def _append_solution(solution, field, label=""):
    sol = SolutionData()
    sol.field = field
    sol.label = label
    solution.append(sol)


def _comp_loss_sum(meshsolution, L1=1, rho=7650, sym=1, logger=None):
    """
    Compute losses sum
    """
    area = meshsolution.get_mesh().get_cell_area()
    loss_norm = meshsolution.get_field(label="LossDensSum")[0, :]

    loss = area * loss_norm * L1 * rho * sym

    mass = area.sum() * L1 * rho * sym

    # Get logger
    if logger is None:
        logger = getLogger()

    logger.debug(f"{meshsolution.label} mass = {mass} kg")

    return loss.sum()


def comp_loss(self, output, lam):
    """Compute the Losses"""
    # get logger
    logger = self.get_logger()

    # get the simulation and output
    simu = output.simu

    # setup meshsolution and solution list
    solution = []
    mag_meshsol = output.mag.meshsolution
    meshsolution = mag_meshsol.get_group(self.group)
    meshsolution.solution = solution

    # get length and material
    L1 = lam.L1
    mat_type = lam.mat_type
    rho = mat_type.struct.rho

    # compute needed model parameter from material data
    success = self.comp_coeff_Bertotti(mat_type)

    if success:
        # compute loss density
        LossDens = self.comp_loss_norm(mag_meshsol)
        _append_solution(solution, LossDens, label="LossDens")

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

        time = Data1D(
            name="time",
            unit="",
            values=array([0, 1]),
        )
        # time = Data1D(name="time", unit="", values=array([0]), ) # TODO squeeze issue
        axes = [axis for axis in LossDens.axes if axis.name not in ["time", "freqs"]]

        loss_sum_ = DataTime(
            name="Losses sum",
            unit="W/kg",
            symbol="LossDensSum",
            axes=[time, *axes],
            values=tile(loss_sum, (2, 1)),
            # values=loss_sum[newaxis,:], # TODO squeeze issue
        )
        _append_solution(solution, loss_sum_, label="LossDensSum")

        # compute overall loss sum
        # Set the symmetry factor according to the machine
        if simu.mag.is_periodicity_a:
            (sym, is_antiper_a, _, _) = output.get_machine_periodicity()
            if is_antiper_a:
                sym = sym * 2
        else:
            sym = 1

        """
        sym = 1 if not output.simu.mag.is_symmetry_a else output.simu.mag.sym_a
        sym *= output.simu.mag.is_antiper_a + 1
        """
        loss_sum = _comp_loss_sum(meshsolution, L1=L1, rho=rho, sym=sym, logger=logger)

        Time = Data1D(
            name="time",
            unit="s",
            symbol="t",
            values=output.simu.input.time.get_data(),
            symmetries={},
            is_components=False,
        )

        data = DataTime(
            name=self.name,
            unit="W",
            symbol="Loss",
            axes=[Time],
            values=loss_sum * ones_like(Time.values),
        )

        return data, meshsolution
