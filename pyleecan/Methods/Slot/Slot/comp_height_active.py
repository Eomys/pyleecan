# -*- coding: utf-8 -*-
from numpy import array


def comp_height_active(self, Ndisc=200):
    """Compute the height of the active area

    Parameters
    ----------
    self : Slot
        A Slot object
    Ndisc : int
        Number of point to discretize the lines

    Returns
    -------
    Hwind: float
        Height of the active area [m]

    """

    surf = self.get_surface_active()

    point_list = surf.discretize(Ndisc)
    point_list = abs(array(point_list))

    return max(point_list) - min(point_list)
