# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW60.comp_angle_opening
SlotW60 Computation of average opening angle method
@date Created on Wed Aug 01 10:40:07 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi, arcsin


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    slot_pitch = 2 * pi / self.Zs
    tooth_angle = float(2 * arcsin(self.W0 / (2 * self.get_Rbo())))

    return slot_pitch - tooth_angle
