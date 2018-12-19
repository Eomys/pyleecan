# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW24.comp_angle_opening
SlotW24 Computation of average opening angle method
@date Created on Mon Jul 06 11:40:07 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    (alpha_0, alpha_2) = self.comp_alphas()
    return alpha_0
