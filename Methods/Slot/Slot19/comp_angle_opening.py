# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot19.comp_angle_opening
Slot19 Computation of slot opening angle method
@date Created on Mon Jun 29 15:28:55 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import arcsin


def comp_angle_opening(self):
    """Compute the slot opening angle of the Slot

    Parameters
    ----------
    self : Slot19
        A Slot19 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    Rbo = self.get_Rbo()

    if self.Wx_is_rad:
        return self.W0
    else:
        return float(2 * arcsin(self.W0 / (2 * Rbo)))
