# -*- coding: utf-8 -*-

from numpy import pi


def comp_surface(self):
    """Compute the surface of the conductor

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    S: float
        Surface of the conductor (with insulation) [m**2]

    """

    return pi * ((self.comp_width() / 2.0) ** 2)
