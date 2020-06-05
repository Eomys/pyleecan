# -*- coding: utf-8 -*-

from numpy import abs as np_abs


def comp_radius(self):
    """Compute the radius of the arc

    Parameters
    ----------
    self : Arc2
        An Arc2 object

    Returns
    -------
    radius: float
        radius of the arc
    """

    self.check()

    z1 = self.begin
    zc = self.center
    return np_abs(z1 - zc)  # Radius of the arc
