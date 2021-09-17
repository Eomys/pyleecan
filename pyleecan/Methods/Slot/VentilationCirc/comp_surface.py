# -*- coding: utf-8 -*-

from numpy import pi


def comp_surface(self):
    """Compute the surface of all the axial ventilation ducts

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object

    Returns
    -------
    Svent:
        Axial ventilation ducts total surface [m**2]

    """

    self.check()

    return pi * ((self.D0 / 2.0) ** 2)
