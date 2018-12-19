# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW23.comp_angle_opening
SlotW23 Computation of average opening angle method
@date Created on Mon Jun 29 15:28:55 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo check definition
"""

from numpy import arcsin


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    Rbo = self.get_Rbo()

    return float(2 * arcsin(self.W0 / (2 * Rbo)))
