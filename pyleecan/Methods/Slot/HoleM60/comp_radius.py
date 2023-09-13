# -*- coding: utf-8 -*-

from numpy import abs as np_abs

from pyleecan.Classes.Arc3 import Arc3


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : HoleM60
        A HoleM60 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]
    """
    point_dict = self._comp_point_coordinate()

    point_list = list()
    # Discretize arcs to get the higher point and the lower point
    curve = Arc3(begin=point_dict["Z2"], end=point_dict["Z4"], is_trigo_direction=True)
    point_list.extend(curve.discretize())
    curve = Arc3(begin=point_dict["Z5"], end=point_dict["Z1"], is_trigo_direction=True)
    point_list.extend(curve.discretize())

    abs_list = [np_abs(point) for point in point_list]
    Rmax = max(abs_list)
    Rmin = min(abs_list)

    return (Rmin, Rmax)
