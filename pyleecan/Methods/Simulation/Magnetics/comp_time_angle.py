# -*- coding: utf-8 -*-


def comp_time_angle(self, output):
    """Compute the time and space discretization of the Magnetics module

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)
    """

    output.mag.Time = output.elec.Time
    output.mag.Angle = output.elec.Angle
