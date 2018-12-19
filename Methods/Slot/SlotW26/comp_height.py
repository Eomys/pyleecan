# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW26.comp_height
SlotW26 Computation of height method
@date Created on Mon Feb 22 12:00:58 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import arcsin, cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    Rbo = self.get_Rbo()

    # Computation of the arc height (P1,0,P8)
    alpha = self.comp_angle_opening() / 2
    Harc = float(Rbo * (1 - cos(alpha)))

    # Height of the arc (P2,C1,P7)
    alpha2 = arcsin(self.W0 / (2.0 * self.R1))
    Harc2 = float(self.R1 * (1 - cos(alpha2)))

    if self.is_outwards():
        return self.H0 + self.H1 + 2 * self.R1 - Harc2 - Harc
    else:
        return self.H0 + self.H1 + 2 * self.R1 - Harc2 + Harc
