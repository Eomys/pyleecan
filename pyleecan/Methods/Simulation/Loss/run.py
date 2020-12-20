# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError
from ....Classes.LossModel import LossModel

DEBUG = True

"""
def _rename(): # TODO adapt and utilize
    names = [mdl.name if mdl.name else "model" for mdl in self.models]

    logger.debug("org. names", names)

    # rename model if there are duplicates
    # TODO: better algorythm to respect order of duplicates
    for idx, model in enumerate(self.models):
        # get list of loss simulation names to rename possible duplicates
        names = [mdl.name if mdl.name else "model" for mdl in self.models]
        name = names[idx]  # use this instead of model.name in case model.name == None
        names.pop(idx)
        # check for dupicate names and rename if needed
        if name in names:
            cnt = 1
            while name + "_" + str(cnt) in names:
                cnt += 1
            model.name = name + "_" + str(cnt)

            logger.warning(f"duplicate name found: {name}")
            logger.warning(f"duplicate name changed to: {model.name}")

    names = [mdl.name if mdl.name else "model" for mdl in self.models]
    logger.debug("new names", names)
"""


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
    output.loss.meshsolution = []

    # iterate through the loss types and models and compute the losses
    prop_list = [self.iron, self.magnet, self.winding]
    out_list = [output.loss.iron, output.loss.magnet, output.loss.winding]
    for loss_prop, loss_out in zip(prop_list, out_list):
        for key, models in loss_prop.items():
            lam = output.simu.machine.get_lam_by_label(key)
            if not isinstance(models, list):
                models = [
                    models,
                ]

            # setup output
            output.iron[key] = [None for i in models]
            if lam is not None:
                loss_out[key] = []
                for idx, model in enumerate(models):
                    data = model.comp_loss(lam)
                    loss_out[key][idx] = data
