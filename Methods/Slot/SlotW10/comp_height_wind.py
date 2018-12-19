# -*- coding: utf-8 -*-
"""@packageMethods.Machine.SlotW10.comp_height_wind
Slot Type_1_0 computation of the height of the winding area method
@date Created on Wed Feb 03 14:31:16 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    return self.H2
