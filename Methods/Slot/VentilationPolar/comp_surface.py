# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationPolar.comp_surface
Compute polar ventulation ducts surface
@date Created on Wed Mar 07 17:36:45 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

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

    return (
        pi * ((self.H0 + self.D0) ** 2 - self.H0 ** 2) / (2 * pi / (self.Zh * self.W1))
    )
