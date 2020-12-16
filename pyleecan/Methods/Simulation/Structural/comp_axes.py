# -*- coding: utf-8 -*-
from ....Methods.Simulation.Input import InputError
from ....Classes.OutStruct import OutStruct


def comp_axes(self, output):
    """Compute axes used for the Structural module

    Parameters
    ----------
    self : Structural
        a Structural object
    output : Output
        an Output object (to update)
    """
    if self.parent is None:
        raise InputError(
            "ERROR: The Structural object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    # setup OutStruct if None
    if self.parent.parent.struct is None:
        self.parent.parent.struct = OutStruct()

    # readability
    N0 = getattr(self.parent.input, "N0", None)
    machine = self.parent.machine

    Time, Angle = self.parent.input.comp_axes(machine, N0=N0)

    # TODO maybe remove periodicity ?

    output.struct.Time = Time
    # output.struct.Nt_tot = len(output.struct.time)

    output.struct.Angle = Angle
    # output.struct.Na_tot = len(output.struct.angle)
