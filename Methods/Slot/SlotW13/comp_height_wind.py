# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW13.comp_height_wind
Slot Type_1_3 computation of the height of the winding area method
@date Created on Mon Jul 11 13:58:25 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW13
        A SlotW13 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    return self.H2
