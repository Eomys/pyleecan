# -*- coding: utf-8 -*-

from numpy import pi


def get_angle(self, is_deg=False):
    """Return the angle of the arc

    Parameters
    ----------
    self : Arc2
        An Arc2 object
    is_deg: bool
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
