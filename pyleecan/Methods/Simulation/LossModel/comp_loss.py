# -*- coding: utf-8 -*-

import numpy as np

from ....Methods.Simulation.Input import InputError


def comp_loss(self, output, attr):
    """Compute the Losses
    """
    if self.parent is None:
        raise InputError("ERROR: The LossModel object must be in a Loss object to run")
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The LossModel object must be in a Simulation object to run"
        )

    if self.parent.parent.parent is None:
        raise InputError(
            "ERROR: The LossModel object must be in an Output object to run"
        )

    setattr(output.loss, attr, np.array(np.nan))  # for testing
