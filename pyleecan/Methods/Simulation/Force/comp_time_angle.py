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
    output.force.angle = output.mag.angle
