# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW22.comp_surface_wind
SlotW22 Computation of winding surface method
@date Created on Tue Dec 09 17:39:57 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import pi


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """
    Rbo = self.get_Rbo()

    if self.is_outwards():
        # Surface of the external disk
        Sext = ((self.H2 + self.H0 + Rbo) ** 2) * pi

        # Surface of the internal disk
        Sint = ((self.H0 + Rbo) ** 2) * pi
    else:
        # Surface of the external disk
        Sext = ((Rbo - self.H0) ** 2) * pi

        # Surface of the internal disk
        Sint = ((Rbo - self.H2 - self.H0) ** 2) * pi

    # Surface of the ring
    Sring = Sext - Sint

    # Only an W2 angle of the ring
    return Sring * self.W2 / (2 * pi)
