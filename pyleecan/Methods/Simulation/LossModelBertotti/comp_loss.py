# -*- coding: utf-8 -*-

from numpy import array, nan, tile, newaxis, ones_like
from SciDataTool import DataTime, DataFreq, Data1D

from ....Classes.SolutionData import SolutionData
from ....Methods.Simulation.Input import InputError


def _store_solution(meshsolution, field, label=""):
    solution = SolutionData()
    solution.field = field
    solution.label = label
    meshsolution.solution.append(solution)


def _comp_loss_sum(meshsolution, grp, L1=1, rho=7650, sym=1):
    """ 
    Compute losses sum
    """

    grp_sol = meshsolution.get_group(grp)

    area = grp_sol.get_mesh().get_cell_area()
    loss_norm = grp_sol.get_field(label="LossSum")[0, :]

    loss = area * loss_norm * L1 * rho * sym

    mass = area.sum() * L1 * rho * sym
    print(f"{grp} mass = {mass} kg")

    return loss.sum()


def comp_loss(self, output):
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
    # setup meshsolution, clear solution
    meshsolution = output.mag.meshsolution
    output.loss.meshsolutions.append(meshsolution.get_group(self.group))
    output.loss.meshsolutions[-1].solution = []

    # compute needed model parameter from material data
    self.comp_coeff_Bertotti(self.mat_type)

    # compute loss density
    LossDens = self.comp_loss_norm(meshsolution)
    _store_solution(output.loss.meshsolutions[-1], LossDens, label="LossDens")

    """
    # --- compute sum over freqs axes ---
    axes_list = [axis.name for axis in LossDens.axes]
    freqs_idx = [idx for idx, axis_name in enumerate(axes_list) if axis_name == "freqs"]
    if len(freqs_idx) > 1:
        raise Exception("more than one freqs axis found")  # TODO improve error msg
    if len(freqs_idx) == 0:
        raise Exception("no freqs axis found")  # TODO improve error msg

    loss_sum = LossDens.get_along(*axes_list)["LossDens"].sum(axis=freqs_idx[0])

    time = Data1D(name="time", unit="", values=array([0, 1]),)
    # time = Data1D(name="time", unit="", values=array([0]), ) # TODO squeeze issue
    axes = [axis for axis in LossDens.axes if axis.name not in ["time", "freqs"]]

    loss_sum_ = DataTime(
        name="Losses sum",
        unit="W/kg",
        symbol="LossSum",
        axes=[time, *axes],
        values=tile(loss_sum, (2, 1)),
        # values=loss_sum[newaxis,:], # TODO squeeze issue
    )
    _store_solution(output.mag.meshsolution, loss_sum_, label="LossSum")

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
    _store_solution(output.mag.meshsolution, Bmag, label="Bfft")

    # store results
    sym = 1 if not output.simu.mag.is_symmetry_a else output.simu.mag.sym_a
    sym *= output.simu.mag.is_antiper_a + 1

    L1 = self.L1 # TODO find better solution to get the length
    rho = self.mat_type.struct.rho # TODO find better solution ...
    loss_sum = _comp_loss_sum(
        output.mag.meshsolution, grp=self.group, L1=L1, rho=rho, sym=sym
    )

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
        symbol="P",
        axes=[Time],
        values=loss_sum*ones_like(Time.values),
    )


    output.loss.losses.append(data)
    """
