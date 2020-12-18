# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError

DEBUG = True


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

    names = [mdl.name if mdl.name else "model" for mdl in self.models]

    logger.debug("org. names", names)

    # rename model if there are duplicates
    # TODO: better algorithym to respect order of duplicates
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

            logger.debug(f"duplicate name found: {name}")
            logger.debug(f"duplicate name changed to: {model.name}")

    names = [mdl.name if mdl.name else "model" for mdl in self.models]
    logger.debug("new names", names)

    # iterate through the models and compute the losses
    # setup losses output structure and meshsolution beforehand
    n_lam = len(output.simu.machine.get_lam_list())
    output.loss.lamination = [[] for x in range(n_lam)]
    output.loss.winding = [[] for x in range(n_lam)]
    output.loss.magnet = [[] for x in range(n_lam)]
    output.loss.meshsolution = []

    for model in self.models:
        model.comp_loss()
