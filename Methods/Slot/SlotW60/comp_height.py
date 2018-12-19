# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW60.comp_height
SlotW60 Computation of height method
@date Created on Wed Aug 01 10:07:35 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    Rbo = self.get_Rbo()
    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11] = self._comp_point_coordinate()

    return Rbo - abs(Z5)
