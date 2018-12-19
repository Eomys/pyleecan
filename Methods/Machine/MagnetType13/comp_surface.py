# -*- coding: utf-8 -*-
"""@package Methods.Machine.Magnet_Type_3.comp_surface
Compute the Magnet surface method
@date Created on Wed Dec 17 15:33:08 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import arcsin, sin


def comp_surface(self):
    """Compute the Magnet surface (by analytical computation)

    Parameters
    ----------
    self : MagnetType13
        A MagnetType13 object

    Returns
    -------
    S: float
        Magnet surface [m**2]

    """
    # Rectangle surface
    S1 = self.Hmag * self.Wmag

    # opening angle
    alpha = 2 * arcsin(self.Wmag / (2 * self.Rtop))
    # Arc surface
    S2 = (self.Rtop ** 2.0) / 2.0 * (alpha - sin(alpha))

    return S1 + S2
