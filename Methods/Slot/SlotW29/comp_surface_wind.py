# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW29.comp_surface_wind
SlotW29 Computation of winding surface method
@date Created on Thu Feb 23 10:36:36 2017
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return self.W2 * self.H2
