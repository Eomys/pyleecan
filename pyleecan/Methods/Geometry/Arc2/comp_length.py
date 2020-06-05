# -*- coding: utf-8 -*-
from numpy import pi


def comp_length(self):
    """Compute the length of the arc

    Parameters
    ----------
    self : Arc2
        An Arc2 object

    Returns
    -------
    length: float
        length of the arc
    """

    R = self.comp_radius()  # Radius of the arc
    angle = self.angle

    # 2*pi*R is the length of the total circle
    # The arc is an alpha / 2pi portion of the cercle
    return float(2 * pi * R * (angle / (2 * pi)))
