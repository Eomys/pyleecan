# -*- coding: utf-8 -*-

from numpy import array, nan, tile, newaxis, ones_like
from SciDataTool import DataTime, Data1D

from ....Classes.SolutionData import SolutionData
from ....Functions.getattr_recursive import getattr_recursive

from logging import getLogger


def comp_loss(self, output, part_label):
    """Compute the Losses"""
    # get logger
    logger = self.get_logger()

    # check inpurt
    if not "Stator" in part_label and not "Rotor" in part_label:
        logger.warning(
            f"LossModelWinding.comp_loss(): 'part_label'"
            + f" {part_label} not implemented yet."
        )
        return None, None

    # get the simulation and the lamination
    simu = output.simu
    lam = simu.machine.get_lam_by_label(part_label)

    # check that lamination has a winding
    if hasattr(lam, "winding") and lam.winding is not None:
        R = lam.comp_resistance_wind(T=self.temperature)
        if lam.is_stator:
            current = output.elec.get_Is()
        else:
            current = output.elec.get_Ir()

        axes_names = [axis.name + "[smallestperiod]" for axis in current.axes]
        data_dict = current.get_along(*axes_names)

        data = DataTime(
            name=self.name,
            unit="W",
            symbol="Loss",
            axes=current.axes,
            values=R * data_dict[current.symbol] ** 2,
        )

        return data, None

    else:
        logger.warning("LossModelWinding.comp_loss(): Lamination has no winding.")
        return None, None
