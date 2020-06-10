# -*- coding: utf-8 -*-
from ....Functions.Geometry.comp_surface_num import comp_surface_num


def comp_surface(self, Ndisc=200):
    """Compute the SurfLine surface

    Parameters
    ----------
    self : SurfLine
        A SurfLine object
    Ndisc : int
        Number of point to discretize the lines

    Returns
    -------
    surf: float
        The SurfLine surface [m**2]

    """

    # Discretize the surface with lots of points to compute the surface numerically
    point_list = self.discretize(Ndisc)

    return comp_surface_num(point_list)
