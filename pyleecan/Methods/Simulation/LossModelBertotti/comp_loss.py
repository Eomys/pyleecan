# -*- coding: utf-8 -*-

from numpy import array, nan, tile, newaxis, ones_like
from SciDataTool import DataTime, DataFreq, Data1D

from ....Classes.SolutionData import SolutionData
from ....Methods.Simulation.Input import InputError
from ....Functions.getattr_recursive import getattr_recursive


def _store_solution(meshsolution, field, label=""):
    solution = SolutionData()
    solution.field = field
    solution.label = label
    meshsolution.solution.append(solution)


def _comp_loss_sum(meshsolution, L1=1, rho=7650, sym=1):
    """
    Compute losses sum
    """
    area = meshsolution.get_mesh().get_cell_area()
    loss_norm = meshsolution.get_field(label="LossDensSum")[0, :]

    loss = area * loss_norm * L1 * rho * sym

    mass = area.sum() * L1 * rho * sym
    print(f"{meshsolution.label} mass = {mass} kg")  # TODO for verification, remove

    return loss.sum()


def comp_loss(self, output):
    """Compute the Losses"""
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

    # get length and material
    simu = self.parent.parent
    
    if not self.lam.startswith("machine"):
        raise Exception("Lam string must start with 'machine'")

    _, *attr_list = self.lam.split(".")

    lam = getattr_recursive(simu.machine, attr_list)

    L1 = lam.L1  
    mat_type = lam.mat_type
    rho = mat_type.struct.rho 

    # compute needed model parameter from material data
    self.comp_coeff_Bertotti(mat_type)

    # compute loss density
    LossDens = self.comp_loss_norm(meshsolution)
    _store_solution(output.loss.meshsolutions[-1], LossDens, label="LossDens")

    # compute sum over frequencies
    axes_list = [axis.name for axis in LossDens.axes]
    freqs_idx = [idx for idx, axis_name in enumerate(axes_list) if axis_name == "freqs"]
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
    _store_solution(output.loss.meshsolutions[-1], loss_sum_, label="LossDensSum")

    # compute overall loss sum
    sym = 1 if not output.simu.mag.is_symmetry_a else output.simu.mag.sym_a
    sym *= output.simu.mag.is_antiper_a + 1

    loss_sum = _comp_loss_sum(output.loss.meshsolutions[-1], L1=L1, rho=rho, sym=sym)

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

    output.loss.losses.append(data)
