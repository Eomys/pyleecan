# -*- coding: utf-8 -*-

from numpy import cos, exp
from numpy import abs as np_abs


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the hole

    Parameters
    ----------
    self : Hole
        A Hole object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the hole

    """

    surf_list = self.build_geometry()
    point_list = list()
    for surf in surf_list:
        for curve in surf.get_lines():
            point_list.extend(curve.discretize())

    abs_list = [np_abs(point) for point in point_list]
    Rmax = max(abs_list)
    Rmin = min(abs_list)
    return (Rmin, Rmax)
