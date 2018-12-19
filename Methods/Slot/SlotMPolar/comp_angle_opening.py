# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotMPolar.comp_angle_opening
SlotMPolar Computation of average opening angle method
@date Created on Mon Dec 22 13:24:56 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotMPolar
        A SlotMPolar object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    Nmag = len(self.magnet)
    return self.W0 * Nmag + self.W3 * (Nmag - 1)
