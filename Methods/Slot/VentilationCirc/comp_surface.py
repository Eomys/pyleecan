# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationCirc.comp_surface
Compute circular ventulation ducts surface
@date Created on Wed Dec 09 16:59:18 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

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

    return pi * ((self.D0 / 2.0) ** 2) * self.Zh
