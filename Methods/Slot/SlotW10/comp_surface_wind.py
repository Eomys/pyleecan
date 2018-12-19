# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW10.comp_surface_wind
SlotW10 Computation of winding surface method
@date Created on Mon Dec 08 17:40:36 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return 0.5 * (self.W0 + self.W2) * self.H2
