# -*- coding: utf-8 -*-

from ....Classes.OutMag import OutMag
from ....Classes.Simulation import Simulation
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

    # get the simulation
    if isinstance(self.parent, Simulation):
        simu = self.parent
    elif isinstance(self.parent.parent, Simulation):
        simu = self.parent.parent
    else:
        raise InputError(
            "ERROR: InputCurrent object should be inside a Simulation object"
        )

    # Set discretization
    Time, Angle = self.comp_axes(simu.machine, self.N0)
    output.time = Time
    output.angle = Angle

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
