# -*- coding: utf-8 -*-

from pyleecan.Functions.Geometry.inter_line_circle import inter_line_circle
from numpy import abs as np_abs


def intersect_line(self, Z1, Z2):
    """Return a list (0, 1 or 2 complex) of coordinates of the 
    intersection of the arc with a line defined by two complex

    Parameters
    ----------
    self : Arc
        An Arc object

    Returns
    -------
    Z_list: list
        Complex coordinates of the intersection (if any)
    """

    Zc = self.get_center()
    R = self.comp_radius()

    # Get intersetion between line and the full circle
    Zlist = inter_line_circle(Z1=Z1, Z2=Z2, R=R, Zc=Zc)

    # Keep only the points actualy on the arc
    return [Z for Z in Zlist if self.is_on_arc(Z)]
