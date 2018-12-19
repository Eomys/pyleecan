# -*- coding: utf-8 -*-
"""@package Methods.Slot.HoleM53.comp_radius
Compute the radius of the Slot method
@date Created on Fri Mar 16 09:51:15 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import cos, exp
from numpy import abs as np_abs


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the hole

    Parameters
    ----------
    self : HoleM54
        A HoleM54 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the hole [m]

    """

    Rbo = self.get_Rbo()

    surf_list = self.build_geometry()
    point_list = list()
    for curve in surf_list[0].line_list:
        point_list.extend(curve.discretize())

    Rmax = max([np_abs(point) for point in point_list])
    Rmin = Rbo - self.H0 - self.H1
    return (Rmin, Rmax)
