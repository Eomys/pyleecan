# -*- coding: utf-8 -*-
from ....Functions.Geometry.comp_surface_num import comp_surface_num


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
