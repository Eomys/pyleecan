# -*- coding: utf-8 -*-

import numpy as np


def is_inside(self, vertice, point, normal_t=None):
    """Check if a point is inside the element.

    Parameters
    ----------
    self : RefSegmentP1
        a RefSegmentP1 object
    vertice : ndarray
        vertice of the element
    point : ndarray
        coordinates of a point
    normal : ndarray
        normal of another element. Additional facultative criterion.

        Returns
    -------
    is_inside : bool
        true if the point is inside the element
    """

    epsilon = self.epsilon

    point_ref = self.get_ref_point(vertice, point)
    s = point_ref[0]
    t = point_ref[1]

    a = abs(s) - (1 + epsilon / 5)
    b = abs(t) / 2

    # The point projected in the reference element domain must be in a rectangle of size (1+2*epsilon)×(2*epsilon)
    # ? Why the tolerance is different according to the direction
    is_inside = (-epsilon < point_ref[0] < 1 + epsilon) & (
        -epsilon < point_ref[1] < epsilon
    )

    # Check that normals are almost aligned
    if normal_t is not None:
        normal_s = self.get_normal(vertice)
        scal_st = np.dot(normal_t[0:2], normal_s)
        is_colinear = abs(scal_st) > 1 - 2 * epsilon
        is_inside = is_colinear & is_inside

    # TODO return the distance to the element from a different method
    return is_inside, a, b
