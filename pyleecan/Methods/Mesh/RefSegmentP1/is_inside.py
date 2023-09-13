# -*- coding: utf-8 -*-

import numpy as np


def is_inside(self, vertice, point, normal_t=None):
    """Check if a point is inside the cell.

    Parameters
    ----------
    self : RefSegmentP1
        a RefSegmentP1 object
    vertice : ndarray
        vertice of the cell
    point : ndarray
        coordinates of a point
    normal : ndarray
        normal of another cell. Additional facultative criterion.

        Returns
    -------
    is_inside : bool
        true if the point is inside the cell
    """

    epsilon = self.epsilon

    point_ref = self.get_ref_point(vertice, point)
    s = point_ref[0]
    t = point_ref[1]

    a = abs(s) - (1 + epsilon)
    b = abs(t) - (epsilon * ((1 - s**2) + 1))
    is_inside = (a < 0) & (b < 0)  # >= in case the point is "just" on the border

    # Check that normals are almost aligned
    if normal_t is not None:
        normal_s = self.get_normal(vertice)
        scal_st = np.dot(normal_t[0:2], normal_s)
        is_colinear = abs(scal_st) > 1 - 2 * epsilon
        is_inside = is_inside & is_colinear

    return is_inside, a, b
