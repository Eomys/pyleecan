# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotMFlat.comp_angle_opening
SlotMFlat Computation of average opening angle method
@date Created on Mon Dec 22 13:24:56 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import arcsin


def comp_angle_opening_magnet(self):
    """Compute the average opening angle of the slot for a single magnet

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    if self.W0_is_rad:
        return self.W0
    else:  # Convert W0 from m to rad
        Rbo = self.get_Rbo()
        return float(2 * arcsin(self.W0 / (2 * Rbo)))
