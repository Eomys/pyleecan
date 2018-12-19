# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW26.comp_angle_opening
SlotW26 Computation of average opening angle method
@date Created on Mon Feb 22 11:59:35 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import arcsin


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """
    Rbo = self.get_Rbo()

    return float(2 * arcsin(self.W0 / (2 * Rbo)))
