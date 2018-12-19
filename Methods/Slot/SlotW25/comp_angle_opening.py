# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW25.comp_angle_opening
SlotW25 Computation of average opening angle method
@date Created on Mon Jul 06 11:40:07 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import arcsin, pi


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """
    Rbo = self.get_Rbo()

    slot_pitch = 2 * pi / self.Zs

    alpha_4 = float(2 * arcsin(self.W4 / (2 * Rbo)))
    return slot_pitch - alpha_4
