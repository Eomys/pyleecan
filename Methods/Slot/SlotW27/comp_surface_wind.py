# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW27.comp_surface_wind
SlotW27 Computation of winding surface method
@date Created on Mon Mar 07 17:42:35 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW27
        A SlotW27 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    S2 = 0.5 * (self.W1 + self.W2) * self.H1
    S3 = 0.5 * (self.W2 + self.W3) * self.H2

    return S2 + S3
