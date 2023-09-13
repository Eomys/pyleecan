# -*- coding: utf-8 -*-
from numpy import pi


def comp_surface(self):
    """Compute the circle surface

    Parameters
    ----------
    self : Circle
        A Circle object

    Returns
    -------
    surf: float
        The circle surface [m**2]

    """

    return pi * self.radius**2
