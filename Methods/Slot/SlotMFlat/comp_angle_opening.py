# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotMFlat.comp_angle_opening
SlotMFlat Computation of average opening angle method
@date Created on Mon Dec 22 13:24:56 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    alpha0 = self.comp_angle_opening_magnet()
    alpha3 = self.W3

    Nmag = len(self.magnet)
    if Nmag > 0:
        return alpha0 * Nmag + alpha3 * (Nmag - 1)
    else:
        0
