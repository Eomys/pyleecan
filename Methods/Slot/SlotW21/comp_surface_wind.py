# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW21.comp_surface_wind
SlotW21 Computation of winding surface method
@date Created on Mon Dec 08 17:42:35 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW21
        A SlotW21 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    S3 = 0.5 * (self.W1 + self.W2) * self.H2

    return S3
