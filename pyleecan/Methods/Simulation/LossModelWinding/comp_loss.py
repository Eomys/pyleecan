# -*- coding: utf-8 -*-

from numpy import array, nan, tile, newaxis, ones_like
from SciDataTool import DataTime, Data1D

from ....Classes.SolutionData import SolutionData
from ....Methods.Simulation.Input import InputError
from ....Functions.getattr_recursive import getattr_recursive

from logging import getLogger

# TODO add the possibility to compute single (or group of) phase losses


def comp_loss(self):
    """Compute the Losses"""
    if self.parent is None:
        raise InputError(
            "ERROR: The LossModelWinding object must be in a Loss object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The LossModel object must be in a Simulation object to run"
        )

    if self.parent.parent.parent is None:
        raise InputError(
            "ERROR: The LossModelBertotti object must be in an Output object to run"
        )
    # get logger
    logger = self.get_logger()

    # get length and material
    simu = self.parent.parent
    output = simu.parent
    lam = simu.machine.get_lam_list()[self.lam_id]

    # check that lamination has a winding
    if hasattr(lam, "winding") and lam.winding is not None:
        R = lam.comp_resistance_wind(T=self.temperature)
        if lam.is_stator:
            I = output.elec.get_Is()
            name = "Is"  # TODO extract the data name instead
        else:
            I = output.elec.get_Ir()
            name = "Ir"  # TODO extract the data name instead

        data_dict = I.get_along("time")
        Time = Data1D(
            name="time",
            unit="s",
            symbol="t",
            values=data_dict["time"],
            symmetries={},
            is_components=False,
        )

        data = DataTime(
            name=self.name,
            unit="W",
            symbol="Loss",
            axes=[Time],
            values=lam.winding.qs * R * data_dict[name] ** 2,
        )

        output.loss.winding[self.lam_id].append(data)
