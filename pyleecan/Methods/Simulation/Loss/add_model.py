# -*- coding: utf-8 -*-
from ....Classes.LossModel import LossModel
from ....Methods.Simulation.Loss import LossError

"""
The loss models are stored in a list 'model_list'. The losses are categorized by the
respective machine part 'part', e.g. stator, rotor or bearings. It has to corespond 
to the first part of the name of the respective FEA group for FEA basedb loss models 
to form the complete FEA group name together with the models group property.

To organize the stored models the 'model_list' is supplemented by 'model_index'
property. 'model_index' is a triple stacked dict, where the first layer is for
'part', the 2nd layer is for 'group' and the 3rd layer is for an optional index 
(if one wants to e.g. have multiple stator core loss models). The reason to use a 
dict with int keys is to have a kind of sparse list.

To retrieve the model from the 'model_list' the 'model_index' stores the respective
list index where the model is added.

"""
# TODO maybe use machine part directly, e.g. use 'machine.stator'
#      and request name from the part
def add_model(self, model, part, index=None):
    """Add a loss model to the list of loss models. For further details on
    Loss organization see Loss.add_model() comments.

    Parameter
    ---------
    self : Loss
        Loss object

    model : LossModel
        the model to add to the list of loss models

    part : str
        Part of the machine to apply the model, e.g. "stator" or "rotor"

    index : int
        explicit index of the model, e.g. if there are multiple 'stator core'
        loss models one may give an index to each of them

    Return
    ------

    """
    logger = self.get_logger()

    # check type of index
    if not isinstance(index, int) and index is not None:
        logger.warning(
            "Loss.add_model(): Input argument 'index' "
            + f"is of type {type(index).__name__} but should be of type int."
            + "Index set to None."
        )

    # check type of model
    if not isinstance(model, LossModel):
        raise LossError("Input argument 'model' has to be of type 'LossModel'.")

    # get group string
    if hasattr(model, "group"):
        group = model.group
    else:
        group = "None"

    # get actual index for model
    mdl_index = len(self.model_list)

    # check if dict key exists
    if part not in self.model_index.keys():
        self.model_index[part] = {}

    # check if sub dict key exists
    if group not in self.model_index[part].keys():
        self.model_index[part][group] = {}

    # get next free index
    if index is None:
        keys = [key for key in self.model_index[part][group].keys()]
        if not keys:
            index = 0
        else:
            index = max(keys)

    # store the model and the index
    if index in self.model_index[part][group].keys():
        # override model by request
        ii = self.model_index[part][group][index]
        logger.info(
            f"Loss.add_model(): Model '{self.model_list[ii].name}' "
            + f"overriden by model {model.name}."
        )
        self.model_list[ii] = model
    else:
        # append model
        self.model_list.append(model)
        self.model_index[part][group][index] = mdl_index
