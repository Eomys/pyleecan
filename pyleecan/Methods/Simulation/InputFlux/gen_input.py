# -*- coding: utf-8 -*-

from ....Classes.OutMag import OutMag
from ....Methods.Simulation.Input import InputError
from numpy import ndarray


def gen_input(self):
    """Generate the input for the structural module (magnetic output)

    Parameters
    ----------
    self : InFlux
        An InFlux object
    """

    output = OutMag()
    # Load and check time
    if self.time is None:
        raise InputError("ERROR: InFlux.time missing")
    output.time = self.time.get_data()

    if (
        not isinstance(output.time, ndarray)
        or len(output.time.shape) > 2
        or (len(output.time.shape) == 2 and output.time.shape[0] != 1)
    ):
        # time should be a vector
        raise InputError(
            "ERROR: InFlux.time should be a vector, "
            + str(output.time.shape)
            + " shape found"
        )

    # Load and check angle
    if self.angle is None:
        raise InputError("ERROR: InFlux.angle missing")
    output.angle = self.angle.get_data()
    if (
        not isinstance(output.angle, ndarray)
        or len(output.angle.shape) > 2
        or (len(output.angle.shape) == 2 and output.angle.shape[0] != 1)
    ):
        # angle should be a vector
        raise InputError(
            "ERROR: InFlux.angle should be a vector, "
            + str(output.angle.shape)
            + " shape found"
        )

    if self.B is None:
        raise InputError("ERROR: InFlux.B missing")
    if self.B.name is None:
        self.B.name = "Airgap flux density"
    if self.B.symbol is None:
        self.B.symbol = "B"
    B = self.B.get_data()
    output.B = B

    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )
    # Save the Output in the correct place
    self.parent.parent.mag = output

    # Define the electrical Output to set the Operating Point
    if self.OP is not None:
        self.OP.gen_input()
