# -*- coding: utf-8 -*-
"""@package Methods.Slot.HoleM50.comp_alpha
Compute the alpha angle of slot type 5_0
@date Created on Fri Jan 08 11:19:18 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import arcsin, arctan, cos


def comp_alpha(self):
    """Compute the alpha angle of the slot (cf schematics)

    Parameters
    ----------
    self : HoleM50
        a HoleM50 object

    Returns
    -------
    alpha: float
        Cf schematics [rad]
    """
    Rbo = self.get_Rbo()

    alpham = 2 * arcsin(self.W0 / (2 * (Rbo - self.H1)))

    Harc = (Rbo - self.H1) * (1 - cos(alpham / 2))
    return arctan((self.H0 - self.H1 - Harc) / (self.W0 / 2 - self.W1 / 2))
