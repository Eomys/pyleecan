# -*- coding: utf-8 -*-
"""@packageMethods.Machine.SlotW10.comp_height_wind
Slot Type_1_0 computation of the height of the winding area method
@date Created on Wed Feb 03 14:31:16 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""
from numpy import array


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotWind
        A SlotWind object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    surf = self.build_geometry_wind(Nrad=1, Ntan=1)

    point_list = surf.discretize(200)
    point_list = abs(array(point_list))

    return max(point_list) - min(point_list)
