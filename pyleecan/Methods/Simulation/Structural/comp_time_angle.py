# -*- coding: utf-8 -*-


def comp_time_angle(self, output):
    """Compute the time and space discretization of the Structural module

    Parameters
    ----------
    self : Structural
        a Structural object
    output : Output
        an Output object (to update)
    """

    output.struct.time = output.mag.time
    output.struct.Nt_tot = len(output.struct.time)

    output.struct.angle = output.mag.angle
    output.struct.Na_tot = len(output.struct.angle)
