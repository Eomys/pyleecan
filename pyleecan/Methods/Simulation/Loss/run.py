# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError
from ....Classes.LossModel import LossModel
from ....Classes.MeshSolution import MeshSolution
from SciDataTool import DataND


# TODO case of 'part' string may be problematic -> check
#      should e.g. be 'Stator' but FEMM groups are lower case
# TODO maybe implement machine.get_part_by_label and use here
#      or input label to loss model, so the model has to take care
def run(self):
    """Run the Loss module"""
    if self.parent is None:
        raise InputError("ERROR: The Loss object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("ERROR: The Loss object must be in an Output object to run")

    # get logger
    logger = self.get_logger()

    # get output
    output = self.parent.parent

    # replicate model_list for solutions with respective object types
    output.loss.meshsol_list = [None for ii in self.model_list]
    output.loss.loss_list = [None for ii in self.model_list]

    # iterate through the loss models and compute losses
    for part_label in self.model_index.keys():
        if part_label not in output.loss.loss_index.keys():
            output.loss.loss_index[part_label] = {}
        for key, index in self.model_index[part_label].items():
            if key not in output.loss.loss_index[part_label].keys():
                output.loss.loss_index[part_label][key] = {}
            # run the loss model
            output.loss.loss_index[part_label][key] = index
            data, mshsol = self.model_list[index].comp_loss(output, part_label)
            # store the results
            if data is not None:
                output.loss.loss_list[index] = data
            if mshsol is not None:
                output.loss.meshsol_list[index] = mshsol
