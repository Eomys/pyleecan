# -*- coding: utf-8 -*-

from ....Classes.OutForce import OutForce
from ....Methods.Simulation.Input import InputError


def gen_input(self):
    """Generate the input for the structural module (skip force computation)

    Parameters
    ----------
    self : InputForce
        An InputForce object
    """

    output = OutForce()

    if self.P is None:
        raise InputError("ERROR: InForce.P missing")
    if self.P.name is None:
        self.P.name = "Magnetic airgap surface force"
    if self.P.symbol is None:
        self.P.symbol = "P"
    P = self.P.get_data()
    output.P = P

    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )
    # Save the Output in the correct place
    self.parent.parent.struct = output
