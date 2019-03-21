# -*- coding: utf-8 -*-

from numpy import pi, arcsin


def get_angle(self, is_deg=False):
    """Return the angle of the arc

    Parameters
    ----------
    self : Arc1
        An Arc1 object
    is_deg: bool
        True to convert to degree

    Returns
    -------
    angle: float
        Angle of the arc
    """
    z_begin = self.begin
    z_end = self.end
    alpha = 2 * arcsin(abs(z_end - z_begin) / (2 * self.radius))
    if self.radius < 0:
        alpha = -alpha
    if is_deg:
        return alpha * 180 / pi
    else:
        return alpha
