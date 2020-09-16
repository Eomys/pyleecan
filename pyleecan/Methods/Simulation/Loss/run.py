# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError

DEBUG = True


def run(self):
    """Run the Loss module
    """
    if self.parent is None:
        raise InputError("ERROR: The Loss object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("ERROR: The Loss object must be in an Output object to run")

    output = self.parent.parent
    # machine = self.parent.machine

    names = [mdl.name if mdl.name else "model" for mdl in self.models]
    if DEBUG:
        print("org. names", names)

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

            if DEBUG:
                print(f"duplicate name found: {name}")
            if DEBUG:
                print(f"duplicate name changed to: {model.name}")

    if DEBUG:
        names = [mdl.name if mdl.name else "model" for mdl in self.models]
    if DEBUG:
        print("new names", names)

    # iterate through the models and compute the losses
    # clear losses and meshsolutions beforehand
    # TODO check for OutLoss
    output.loss.losses = []
    output.loss.meshsolutions = []

    for model in self.models:
        model.comp_loss(output)
