# -*- coding: utf-8 -*-

import numpy as np
from SciDataTool import DataTime, DataFreq

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

    # compute needed model parameter from material data
    self.comp_coeff_Bertotti(lam.mat_type)

    # comp. fft of elemental FEA results
    B_fft = output.mag.meshsolution.solution[0].field.time_to_freq()
    print("FFT of B calculated")

    # calculate principle axes and transform for exponentials other than 2
    # TODO

    # TODO time data hot fix
    #output.mag.meshsolution.solution[0].field.axes[0].final=output.mag.time[-1]
    #output.mag.meshsolution.solution[0].field.axes[0].include_endpoint=True

    # apply model
    # #TODO model equation should be a func that takes SciDataTool Data as input
    field = output.mag.meshsolution.solution[0].field

    # TODO filter machine parts
    Loss = self.comp_loss_norm(field)

    # store losses field

    # store results
    if typ == "Lamination":
        if lam.is_stator:
            output.loss.Plam_stator = np.array([np.nan])

    return Loss
