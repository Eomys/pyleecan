# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW60.comp_surface_wind
SlotW60 Computation of winding surface method
@date Created on Wed Aug 01 10:40:07 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return 2 * (self.H2 - self.H3 - self.H4) * ((self.W1 - self.W2) / 2 - self.W3)
