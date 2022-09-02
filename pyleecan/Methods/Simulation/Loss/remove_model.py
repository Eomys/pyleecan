# -*- coding: utf-8 -*-
from ....Classes.LossModel import LossModel
from ....Methods.Simulation.Loss import LossError


def remove_model(self, part_label, index):
    """Remove a loss model from the list of loss models.

    Parameters
    ----------
    self : Loss
        Loss object

    part_label : str
        Part label of the model to remove.

    index : int
        Index of the model, e.g. if there are multiple 'stator core' loss models

    Returns
    -------

    is_success : bool
        Could the model be removed?

    """
    logger = self.get_logger()

    # check if dict key exists
    if part_label not in self.model_index.keys():
        logger.warning(
            f"Loss.remove_model(): Loss model for part '{part_label}' "
            + "doesn't exists. No model removed."
        )
        return False

    # check if sub dict key exists
    if index not in self.model_index[part_label].keys():
        logger.warning(
            f"Loss.remove_model(): Loss model for part '{part_label}' "
            + f"with index {index} doesn't exists. No model removed."
        )
        return False

    # for simplicity set model to None
    else:
        ii = self.model_index[part_label][index]
        self.model_list[ii] = None
        self.model_index[part_label].pop(index)

        return True
