# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW12.comp_surface_wind
SlotW12 Computation of winding surface method
@date Created on Tue Mar 07 14:54:30 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    S3 = 2 * self.R2 * self.H1
    S4 = pi * self.R2 ** 2 / 2.0

    return S3 + S4
