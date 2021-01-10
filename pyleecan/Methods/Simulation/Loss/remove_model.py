# -*- coding: utf-8 -*-
from ....Classes.LossModel import LossModel
from ....Methods.Simulation.Loss import LossError


def remove_model(self, part, group, index=None):
    """Remove a loss model to the list of loss models.

    Parameter
    ---------
    self : Loss
        Loss object

    part : str
        Part of the machine to apply the model, e.g. "stator" or "rotor"

    group : str
        Group of the loss model

    index : int
        explicit index of the model, e.g. if there are multiple 'stator core'
        loss models one may give an index to each of them

    Return
    ------

    """
    logger = self.get_logger()
