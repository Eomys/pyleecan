# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW12.comp_height_wind
Slot Type_1_2 computation of the height of the winding area method
@date Created on Wed Feb 03 14:41:46 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    return self.H1 + self.R2
