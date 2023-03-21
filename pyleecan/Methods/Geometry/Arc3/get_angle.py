# -*- coding: utf-8 -*-

from numpy import pi


def get_angle(self, is_deg=False):
    """Return the angle of the arc

    Parameters
    ----------
    self : Arc3
        An Arc3 object
    is_deg: bool
        True to convert to degree

    Returns
    -------
    angle: float
        Angle of the arc
    """

    if self.is_trigo_direction:
        sign = 1
    else:
        sign = -1

    if is_deg:
        return sign * 180
    else:
        return sign * pi
