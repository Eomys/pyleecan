# -*- coding: utf-8 -*-
from numpy import dot


def is_inside(self, vertice, point, normal_t=None):
    """Check if a point is inside the cell defined by the vertices.

    Parameters
    ----------
    self : RefTriangle3
        an RefTriangle3 object
    vertice : ndarray
        vertices of the cell
    point : ndarray
        coordinates of the checked point
    normal_t : ndarray
        (optional) cell normal vector

    Returns
    -------
    is_inside: bool
        true if the point is inside the cell

    """
    point_ref = self.get_ref_point(vertice, point)
    s = point_ref[0]
    t = point_ref[1]
    a = s
    b = t
    c = 1 - s - t
    is_inside = (a > -self.epsilon) & (b > -self.epsilon) & (c > -self.epsilon)

    # Optional : Check that normals are almost aligned
    if normal_t is not None:
        normal_s = self.get_normal(vertice)
        scal_st = dot(normal_t[0:2], normal_s)
        is_colinear = abs(scal_st) > 1 - 2 * self.epsilon
        is_inside = is_inside & is_colinear

    return is_inside, a, b
