# -*- coding: utf-8 -*-

from numpy import pi


def comp_length(self):
    """Compute the length of the arc

    Parameters
    ----------
    self : Arc3
        An Arc3 object

    Returns
    -------
    length: float
        length of the arc
    """

    self.check()

    R = self.comp_radius()

    # Half circle
    return float(pi * R)
