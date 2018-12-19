# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW28.comp_height_wind
Slot Type_2_8 computation of the height of the winding area method
@date Created on Wed Jul 13 12:23:08 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import arcsin, exp, pi, sqrt


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, rot_sign] = self._comp_point_coordinate()
    if self.is_outwards():
        Ztan2 = Z5 + Z5.imag * (-1 - 1j)
    else:
        Ztan2 = Z5 + Z5.imag * (+1 - 1j)
    Ztan1 = (Z2 + Z7) / 2.0

    return abs(Ztan2 - Ztan1)
