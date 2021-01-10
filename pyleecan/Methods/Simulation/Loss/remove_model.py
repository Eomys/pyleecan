# -*- coding: utf-8 -*-
from ....Classes.LossModel import LossModel
from ....Methods.Simulation.Loss import LossError


def remove_model(self, part, index=None):
    """Remove a loss model from the list of loss models.

    Parameter
    ---------
    self : Loss
        Loss object

    part : str
        Part of the machine to apply the model, e.g. "stator" or "rotor"

    index : int
        index of the model, e.g. if there are multiple 'stator core' loss models

    Return
    ------

    """
    logger = self.get_logger()

    # check if dict key exists
    if part not in self.model_index.keys():
        logger.warning(f"Loss.remove_model(): {part} doesn't exists. No model removed.")

    # check if sub dict key exists
    if index not in self.model_index[part].keys():
        logger.warning(f"Loss.remove_model(): {part} doesn't exists. No model removed.")

    # for simplicity set model to None
    else:
        ii = self.model_index[part][index]
        self.model_list[ii] = None
        self.model_index[part].pop(index)
