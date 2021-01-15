# -*- coding: utf-8 -*-

from ....Classes.OutElec import OutElec
from ....Methods.Simulation.Input import InputError
from numpy import ndarray


def gen_input(self):
    """Generate the input for the electrical module (time/space discretization)

    Parameters
    ----------
    self : Input
        An Input object
    """
    # Get the simulation and check output
    if self.parent is None:
        raise InputError("ERROR: Input object should be inside a Simulation object")
    simu = self.parent

    if self.parent.parent is None:
        raise InputError(
            "ERROR: Input parent error:"
            + " The Simulation object must be in an Output object to run"
        )

    # Create the correct Output object
    output = OutElec()
    self.comp_axes(machine=simu.machine, N0=self.N0)

    # Save the Output in the correct place
    self.parent.parent.elec = output
