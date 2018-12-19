# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW23.comp_height_wind
Slot Type_2_3 computation of the height of the winding area method
@date Created on Wed Feb 03 14:44:43 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    Rbo = self.get_Rbo()
    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = self._comp_point_coordinate()

    if self.is_outwards():
        return abs(Z4) - abs((Z3 + Z6) / 2)
    else:
        return abs(Z3) - abs(Z4)
