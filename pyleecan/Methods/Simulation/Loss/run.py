# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError
from ....Classes.LossModel import LossModel


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

    # replicate model_list for solutions
    output.loss.meshsol_list = [None for ii in self.model_list]
    output.loss.loss_list = [None for ii in self.model_list]

    # iterate through the loss models and compute losses
    for part in self.model_index.keys():
        for index in self.model_index[part].values():
            # run the loss model
            data, mshsol = self.model_list[index].comp_loss(output, part)
            # store the results
            output.loss.meshsol_list[index] = mshsol
            output.loss.loss_list[index] = mshsol
