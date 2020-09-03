# -*- coding: utf-8 -*-

from numpy import array, nan, tile, sum as npsum
from SciDataTool import DataTime, DataFreq, Data1D

from ....Classes.SolutionData import SolutionData
from ....Methods.Simulation.Input import InputError


def _comp_loss_sum(meshsolution, grp, L1=1, rho=7650):
    """ 
    Compute losses sum
    """

    grp_sol = meshsolution.get_group(grp)

    area = grp_sol.get_mesh().get_cell_area()
    loss_norm = grp_sol.get_field(label="LossSum")[0, :]

    loss = area * loss_norm * L1 * rho

    mass = area.npsum() * L1 * rho
    print(f"{grp} mass = {mass} kg")

    return loss.sum()


def comp_loss(self, output, lam, typ):
    """Compute the Losses
    """
    if self.parent is None:
        raise InputError(
            "ERROR: The LossModelBertotti object must be in a Loss object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The LossModel object must be in a Simulation object to run"
        )

    if self.parent.parent.parent is None:
        raise InputError(
            "ERROR: The LossModelBertotti object must be in an Output object to run"
        )

    # compute needed model parameter from material data
    self.comp_coeff_Bertotti(lam.mat_type)

    # comp. fft of elemental FEA results
    print(type(output.mag.meshsolution).__name__)
    print(type(output.mag.meshsolution.solution[0]).__name__)

    # B_fft = output.mag.meshsolution.solution[0].field.time_to_freq()
    # print("FFT of B calculated")

    # calculate principle axes and transform for exponentials other than 2
    # TODO

    # apply model
    # #TODO model equation should be a func that takes SciDataTool Data as input
    field = output.mag.meshsolution.get_solution(label="B").field

    field_list = []
    for comp in field.components.values():
        field_list.append(comp)

    # TODO filter machine parts
    Loss = self.comp_loss_norm(field_list)

    # store losses density field
    sol = SolutionData()
    sol.field = Loss
    sol.label = "LossDens"
    output.mag.meshsolution.solution.append(sol)

    # --- compute sum over freqs axes ---
    axes_list = [axis.name for axis in sol.field.axes]
    freqs_idx = [idx for idx, axis_name in enumerate(axes_list) if axis_name == "freqs"]
    if len(freqs_idx) > 1:
        # TODO error
        raise ("more than one freqs axis found")
    if len(freqs_idx) == 0:
        # TODO error
        raise ("no freqs axis found")

    loss_sum = sol.field.get_along(*axes_list)["LossDens"].sum(axis=freqs_idx[0])

    time = Data1D(name="time", unit="", values=array([0, 1]))
    axes = [axis for axis in sol.field.axes if axis.name not in ["time", "freqs"]]

    loss_sum_ = DataTime(
        name="Losses sum",
        unit="W/kg",
        symbol="LossSum",
        axes=[time, *axes],
        values=tile(loss_sum, (2, 1)),
    )
    data = SolutionData()
    data.field = loss_sum_
    data.label = "LossSum"
    output.mag.meshsolution.solution.append(data)

    # compute FFT of induction magnitude
    field_list = [f for f in field.components.values()]
    Bmag_sq = None
    for component in field_list:
        axes_names = ["freqs" if x.name == "time" else x.name for x in component.axes]

        mag_dict = component.get_magnitude_along(*axes_names)
        symbol = component.symbol

        Bmag_sq = (
            mag_dict[symbol] ** 2
            if Bmag_sq is None
            else Bmag_sq + mag_dict[symbol] ** 2
        )

    Freq = Data1D(name="freqs", unit="", values=mag_dict["freqs"])
    axes = [Freq if x.name == "time" else x for x in component.axes]

    Bmag = DataFreq(
        name="Bfft", unit="T", symbol="Bfft", axes=axes, values=Bmag_sq ** 0.5,
    )
    sol = SolutionData()
    sol.field = Bmag
    sol.label = "Bfft"
    output.mag.meshsolution.solution.append(sol)

    # store results
    if typ == "Lamination":
        if lam.is_stator:
            L1 = output.simu.machine.stator.L1
            rho = output.simu.machine.stator.mat_type.struct.rho
            loss_sum = _comp_loss_sum(
                output.mag.meshsolution, grp="stator", L1=L1, rho=rho
            )
            output.loss.Plam_stator = array([loss_sum])

    return Loss
