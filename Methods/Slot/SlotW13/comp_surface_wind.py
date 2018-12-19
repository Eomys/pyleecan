# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW13.comp_surface_wind
SlotW13 Computation of winding surface method
@date Created on Mon Jul 11 13:58:57 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW13
        A SlotW13 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return 0.5 * (self.W2 + self.W3) * self.H2
