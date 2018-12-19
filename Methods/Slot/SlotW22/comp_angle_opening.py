# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW22.comp_angle_opening
SlotW22 Computation of average opening angle method
@date Created on Tue Dec 09 16:32:39 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    return self.W0
