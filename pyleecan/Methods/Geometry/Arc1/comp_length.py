# -*- coding: utf-8 -*-
from numpy import pi


def comp_length(self):
    """Compute the length of the arc

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    length: float
        length of the arc
    """

    self.check()

    R = abs(self.radius)

    # alpha is the opening angle
    alpha = abs(self.get_angle())

    # 2*pi*R is the length of the total circle
    # The arc is an alpha / 2pi portion of the cercle
    return float(2 * pi * R * (alpha / (2 * pi)))
