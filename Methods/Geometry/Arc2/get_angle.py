# -*- coding: utf-8 -*-

from numpy import exp, angle, pi


def get_angle(self, is_deg=False):
    """Return the angle of the arc

    Parameters
    ----------
    self : Arc2
        An Arc2 object
    is_def: bool
        True to convert to degree

    Returns
    -------
    angle: float
        Angle of the arc
    """

    if is_deg:
        return self.angle * 180 / pi
    else:
        return self.angle
