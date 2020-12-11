# -*- coding: utf-8 -*-
from numpy import array


def comp_height_wind(self, Ndisc=200):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotWind
        A SlotWind object
    Ndisc : int
        Number of point to discretize the lines

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    surf = self.get_surface_wind()

    point_list = surf.discretize(Ndisc)
    point_list = abs(array(point_list))

    return max(point_list) - min(point_list)
