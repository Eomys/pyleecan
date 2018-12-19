# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW25.comp_height_wind
Slot Type_2_5 computation of the height of the winding area method
@date Created on Wed Feb 03 14:56:35 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    return self.H2
