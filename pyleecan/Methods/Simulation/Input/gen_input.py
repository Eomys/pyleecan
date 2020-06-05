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

    output = OutElec()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: Input.time missing")
    output.time = self.time.get_data()

    if not isinstance(output.time, ndarray) or len(output.time.shape) != 1:
        # time should be a vector
        raise InputError(
            "ERROR: Input.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )
    Nt_tot = len(output.time)

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: Input.angle missing")
    output.angle = self.angle.get_data()
    if not isinstance(output.angle, ndarray) or len(output.angle.shape) != 1:
        # angle should be a vector
        raise InputError(
            "ERROR: Input.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )

    # Get the phase number for verifications
    if self.parent is None:
        raise InputError("ERROR: Input object should be inside a Simulation object")
    simu = self.parent

    if self.parent.parent is None:
        raise InputError(
            "ERROR: Input parent error: The Simulation object must be in an Output object to run"
        )
    # Save the Output in the correct place
    self.parent.parent.elec = output
