# -*- coding: utf-8 -*-
"""@package Methods.Slot.Slot.comp_angle_opening
Slot Computation of average opening angle method
@date Created on Tue Dec 09 16:28:38 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import angle


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    line_list = self.build_geometry()
    Z1 = line_list[0].get_begin()
    Z2 = line_list[-1].get_end()

    return angle(Z2) - angle(Z1)
