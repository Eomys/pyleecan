# -*- coding: utf-8 -*-
from ....Classes.LossModel import LossModel
from ....Methods.Simulation.Loss import LossError

# TODO maybe use machine part directly, e.g. use 'machine.stator'
#      and request name from part
def add_model(self, model, part):
    """Add a loss model to the list of loss models.

    Parameter
    ---------
    self : Loss
        Loss object

    model : LossModel
        the model to add to the list of loss models

    part : str
        Part of the machine to apply the model, e.g. "stator" or "rotor"

    Return
    ------

    """
    # check type of model
    if not isinstance(model, LossModel):
        raise LossError("Input argument 'model' has to be of type 'LossModel'.")

    # get group string
    if hasattr(model, "group"):
        group = model.group
    else:
        group = "None"

    # get actual index for model
    index = len(self.model_list)

    # check if dict key exists
    if part not in self.model_index.keys():
        self.model_index[part] = {}

    # check if sub dict key exists
    if group not in self.model_index[part].keys():
        self.model_index[part][group] = []

    # add model to list and register index in dict
    self.model_list.append(model)
    self.model_index[part][group].append(index)
