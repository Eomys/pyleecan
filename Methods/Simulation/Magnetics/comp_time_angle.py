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

    output.mag.time = output.elec.time
    output.mag.Nt_tot = len(output.mag.time)

    output.mag.angle = output.elec.angle
    output.mag.Na_tot = len(output.mag.angle)
