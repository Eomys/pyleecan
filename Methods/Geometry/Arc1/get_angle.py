# -*- coding: utf-8 -*-

from numpy import pi, arcsin, exp, angle


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
    # Go to center ref with begin on the axis
    Zc = self.get_center()
    Z2 = (self.end - Zc) * exp(-1j * angle(self.begin - Zc))

    if is_deg:
        return angle(Z2) * 180 / pi
    else:
        return angle(Z2)
