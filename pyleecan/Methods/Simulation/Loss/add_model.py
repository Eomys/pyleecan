# -*- coding: utf-8 -*-
from ....Classes.LossModel import LossModel
from ....Methods.Simulation.Loss import LossError

"""
The loss models are stored in a list 'model_list'. The losses are categorized by the
respective machine part_label 'part_label', e.g. 'Stator', 'Rotor' or 'Bearings'. It has to 
corespond to the first part_label of the name of the respective FEA group for FEA based loss
models to form the complete FEA group name together with the models 'group' property.

To organize the stored models the 'model_list' is supplemented by 'model_index'
property. 'model_index' is a double stacked dict, where the first layer is for
'part_label', the 2nd layeris for an optional index (if one wants to e.g. have multiple 
stator core loss models). The reason to use a dict with int keys is to have a kind
of sparse list.

To retrieve the model from the 'model_list' the 'model_index' stores the respective
list index where the model is added.

"""
# TODO maybe use machine part_label directly, e.g. use 'machine.stator'
#      and request name from the part_label
def add_model(self, model, part_label, index=None):
    """Add a loss model to the list of loss models. For further details on
    Loss organization see Loss.add_model() comments.

    Parameters
    ----------
    self : Loss
        Loss object

    model : LossModel
        the model to add to the list of loss models

    part_label : str
        Label of the machine part to apply the model, e.g. "Stator" or "Rotor"

    index : int
        explicit index of the model, e.g. if there are multiple 'Stator core'
        loss models one may give an index to each of them
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

    # get actual index for model
    mdl_index = len(self.model_list)

    # check if dict key exists
    if part_label not in self.model_index.keys():
        self.model_index[part_label] = {}

    # get index if it is not specified
    if index is None:
        keys = [key for key in self.model_index[part_label].keys()]
        if not keys:  # if there is no index, set index to zero
            index = 0
        else:  # if there are other models increment max index by one
            index = max(keys) + 1

    # store the model and the index
    if index in self.model_index[part_label].keys():
        # override model by request
        ii = self.model_index[part_label][index]
        logger.info(
            f"Loss.add_model(): Loss model {self.model_list[ii].name}' "
            + f"with index {index} for {part_label}"
            + f"overriden by model '{model.name}''."
        )
        self.model_list[ii] = model
    else:
        # append model
        self.model_list.append(model)
        self.model_index[part_label][index] = mdl_index
