# -*- coding: utf-8 -*-
"""@package Methods.Geometry.SurfLine.comp_surface
Compute the SurfLine surface method
@date Created on Thu Jul 27 13:51:43 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""
from pyleecan.Functions.Geometry.comp_surface_num import comp_surface_num


def comp_surface(self):
    """Compute the SurfLine surface

    Parameters
    ----------
    self : SurfLine
        A SurfLine object

    Returns
    -------
    surf: float
        The SurfLine surface [m**2]

    """

    # Discretize the surface with lots of points to compute the surface numerically
    point_list = self.discretize(200)

    return comp_surface_num(point_list)
