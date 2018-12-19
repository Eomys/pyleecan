# -*- coding: utf-8 -*-
"""@packageMethods.Machine.SlotW29.comp_height_wind
Slot Type_2_9 computation of the height of the winding area method
@date Created on Thu Feb 23 10:36:36 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    return self.H2
