# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW28.comp_height
SlotW28 Computation of height method
@date Created on Wed Jul 13 12:18:11 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import arcsin, exp, pi, sqrt


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    Rbo = self.get_Rbo()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, rot_sign] = self._comp_point_coordinate()
    if self.is_outwards():
        Ztan2 = Z5 + Z5.imag * (1 - 1j)
        return Ztan2.real - Rbo
    else:
        Ztan2 = Z5 + Z5.imag * (-1 - 1j)
        return Rbo - Ztan2.real
