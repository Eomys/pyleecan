# -*- coding: utf-8 -*-

from numpy import pi


def comp_surface(self):
    """Compute the surface of all the axial ventilation ducts

    Parameters
    ----------
    self : VentilationPolar
        A VentilationPolar object

    Returns
    -------
    surface: float
        Axial ventilation ducts total surface [m**2]

    """

    self.check()

    return pi * ((self.H0 + self.D0) ** 2 - self.H0**2) / (2 * pi / self.W1)
