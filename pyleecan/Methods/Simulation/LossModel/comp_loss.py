# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


def comp_loss(self, output):
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

    output = float("NaN")  # for testing
