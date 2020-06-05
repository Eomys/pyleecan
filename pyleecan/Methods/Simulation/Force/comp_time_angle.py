# -*- coding: utf-8 -*-


def comp_time_angle(self, output):
    """Compute the time and space discretization of the Force module

    Parameters
    ----------
    self : Force
        a Force object
    output : Output
        an Output object (to update)
    """

    output.force.time = output.mag.time
    output.force.Nt_tot = output.mag.Nt_tot

    output.force.angle = output.mag.angle
    output.force.Na_tot = output.mag.Na_tot
