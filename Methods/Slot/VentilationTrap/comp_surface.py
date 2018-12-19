# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationTrap.comp_surface
Compute trapezoidal ventulation ducts surface
@date Created on Wed Dec 09 17:36:45 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_surface(self):
    """Compute the surface of all the axial ventilation ducts

    Parameters
    ----------
    self : VentilationTrap
        A VentilationTrap object

    Returns
    -------
    surface: float
        Axial ventilation ducts total surface [m**2]

    """

    self.check()

    return (self.W1 + self.W2) * 0.5 * self.D0 * self.Zh
