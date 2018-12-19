# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW22.comp_surface
SlotW22 Computation of surface method
@date Created on Tue Dec 09 17:40:08 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import pi


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    Rbo = self.get_Rbo()

    Swind = self.comp_surface_wind()

    # Computation of isthmus surface
    if self.is_outwards():
        # Surface of the external disk
        Sext = ((self.H0 + Rbo) ** 2) * pi

        # Surface of the internal disk
        Sint = (Rbo ** 2) * pi
    else:
        # Surface of the external disk
        Sext = (Rbo ** 2) * pi

        # Surface of the internal disk
        Sint = ((Rbo - self.H0) ** 2) * pi
    # Surface of the ring
    Sring = Sext - Sint

    # Only an W0 angle of the ring
    Sisth = Sring * self.W0 / (2 * pi)

    return Swind + Sisth
