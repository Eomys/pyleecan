# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Force module"""
    if self.parent is None:
        raise InputError(
            "ERROR: The Force object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError("ERROR: The Force object must be in an Output object to run")

    output = self.parent.parent

    # Compute and store time and angle axes from previous output
    # and returns additional axes in axes_dict
    axes_dict = self.comp_time_angle(output)

    # Compute the magnetic force according to the Force model
    self.comp_force(output, axes_dict)
