# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Structural module"""
    if self.parent is None:
        raise InputError(
            "ERROR: The Structural object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    output = self.parent.parent

    self.comp_time_angle(output)

    group = self.force.group  # Magnetic force target

    # Init model, generate or import mechanical mesh
    self.init_mechanical_model(output, group)

    # Compute the magnetic force according to the Force model
    self.force.comp_force(output)
