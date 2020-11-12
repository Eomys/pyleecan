# -*- coding: utf-8 -*-


def comp_axes(self, output):
    """Compute axes used for the Structural module

    Parameters
    ----------
    self : Structural
        a Structural object
    output : Output
        an Output object (to update)
    """

    output.struct.Time = output.mag.Time
    # output.struct.Nt_tot = len(output.struct.time)

    output.struct.Angle = output.mag.Angle
    # output.struct.Na_tot = len(output.struct.angle)
