# -*- coding: utf-8 -*-

from numpy import abs as np_abs


def comp_radius(self):
    """Compute the radius of the arc

    Parameters
    ----------
    self : Arc3
        An Arc3 object

    Returns
    -------
    radius: float
        radius of the arc

    """

    self.check()

    z1 = self.begin
    z2 = self.end

    return np_abs(z1 - z2) / 2.0  # Radius of the arc
