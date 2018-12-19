# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW15.comp_surface_wind
SlotW15 Computation of winding surface method
@date Created on Mon Nov 27 12:24:32 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from pyleecan.Functions.comp_num_surface import comp_num_surface


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    curve_list = self.build_geometry()
    curve_list = curve_list[1:-1]  # Remove first and last curve

    point_list = list()
    for curve in curve_list:
        point_list.extend(curve.discretize(20))

    return comp_num_surface(point_list)
