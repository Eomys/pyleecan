# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW23.comp_height
SlotW23 Computation of height method
@date Created on Mon Jun 29 15:28:55 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo check and unittest
"""


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    Rbo = self.get_Rbo()
    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = self._comp_point_coordinate()

    if self.is_outwards():
        return abs(Z4) - Rbo
    else:
        return Rbo - abs(Z4)
