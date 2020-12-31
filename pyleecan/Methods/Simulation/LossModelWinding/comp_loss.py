# -*- coding: utf-8 -*-

from numpy import array, nan, tile, newaxis, ones_like
from SciDataTool import DataTime, Data1D

from ....Classes.SolutionData import SolutionData
from ....Functions.getattr_recursive import getattr_recursive

from logging import getLogger


def comp_loss(self, output, lam):
    """Compute the Losses"""
    # get logger
    logger = self.get_logger()

    # get length and material
    simu = output.simu

    # check that lamination has a winding
    if hasattr(lam, "winding") and lam.winding is not None:
        R = lam.comp_resistance_wind(T=self.temperature)
        if lam.is_stator:
            current = output.elec.get_Is()
        else:
            current = output.elec.get_Ir()

        axes_names = [axis.name for axis in current.axes]
        data_dict = current.get_along(*axes_names)

        data = DataTime(
            name=self.name,
            unit="W",
            symbol="Loss",
            axes=current.axes,
            values=R * data_dict[current.symbol] ** 2,
        )

        return data, None
