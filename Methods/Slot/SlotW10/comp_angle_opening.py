# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW10.comp_angle_opening
SlotW10 Computation of average opening angle method
@date Created on Tue Dec 09 16:28:38 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import arcsin


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    Rbo = self.get_Rbo()

    return float(2 * arcsin(self.W0 / (2 * Rbo)))
