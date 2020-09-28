# -*- coding: utf-8 -*-

import numpy as np

from ....Methods.Simulation.Input import InputError

from SciDataTool import Data1D, DataTime


def comp_loss(self, output):
    """Compute the Losses"""
    # if self.parent is None:
    #     raise InputError("ERROR: The LossModel object must be in a Loss object to run")
    # if self.parent.parent is None:
    #     raise InputError(
    #         "ERROR: The LossModel object must be in a Simulation object to run"
    #     )

    # if self.parent.parent.parent is None:
    #     raise InputError(
    #         "ERROR: The LossModel object must be in an Output object to run"
    #     )
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
        values=[None for x in Time.values],
    )

    output.loss.losses.append(data)
