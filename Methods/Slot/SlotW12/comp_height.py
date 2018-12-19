# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW12.comp_height
SlotW12 Computation of height method
@date Created on Tue Mar 07 14:54:30 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

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
        return self.H0 - Harc + self.R1 * 2 + self.H1 + self.R2
    else:
        return self.H0 + Harc + self.R1 * 2 + self.H1 + self.R2
