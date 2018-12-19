# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotMFlat.comp_height
SlotMFlat Computation of height method
@date Created on Mon Dec 22 13:25:04 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    Rbo = self.get_Rbo()

    # Computation of the arc height
    alpha = self.comp_angle_opening() / 2
    Harc = float(Rbo * (1 - cos(alpha)))

    if self.is_outwards():
        return self.H0 - Harc
    else:
        return self.H0 + Harc
