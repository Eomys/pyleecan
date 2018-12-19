# -*- coding: utf-8 -*-
"""@package Methods.Slot.HoleM52.comp_radius
Compute the radius of the Slot method
@date Created on Wed Mar 16 17:28:22 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the hole

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the hole [m]

    """

    Rbo = self.get_Rbo()

    Rmax = Rbo - self.H0

    alpha = self.comp_alpha()
    Z1 = (Rbo - self.H0) * exp(1j * alpha / 2)
    Z5 = Z1.real - self.H1
    Rmin = abs(Z5)

    return (Rmin, Rmax)
