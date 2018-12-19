# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW12.comp_angle_opening
SlotW12 Computation of average opening angle method
@date Created on Tue Mar 07 14:54:30 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import arcsin


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    Rbo = self.get_Rbo()

    return float(2 * arcsin(self.R2 / Rbo))
