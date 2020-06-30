# -*- coding: utf-8 -*-

import numpy as np

from ....Methods.Simulation.Input import InputError


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

    if typ == "Lamination":
        if lam.is_stator:
            output.loss.Plam_stator = np.array(np.nan)

            self.comp_coeff_Bertotti(lam.mat_type)
