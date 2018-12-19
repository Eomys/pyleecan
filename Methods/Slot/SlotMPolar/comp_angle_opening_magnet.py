# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotMPolar.comp_angle_opening
SlotMPolar Computation of average opening angle method
@date Created on Mon Dec 22 13:24:56 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_angle_opening_magnet(self):
    """Compute the average opening angle of a single magnet

    Parameters
    ----------
    self : SlotMPolar
        A SlotMPolar object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    return self.W0
