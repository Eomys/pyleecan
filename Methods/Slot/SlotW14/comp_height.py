# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Mar 31 12:25:47 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import arcsin, cos, exp, pi, sin, tan


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    Rbo = self.get_Rbo()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9] = self._comp_point_coordinate()

    if self.is_outwards():
        return abs(Z5) - Rbo
    else:
        return Rbo - abs(Z4)
