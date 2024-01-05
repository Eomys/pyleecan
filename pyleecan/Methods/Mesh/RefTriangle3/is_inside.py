# -*- coding: utf-8 -*-
from typing import Optional, Tuple

from numpy import dot, ndarray


def is_inside(
    self, node: ndarray, point: ndarray, normal_t: Optional[ndarray] = None
) -> Tuple[bool, float, float]:
    """Check if a point is inside the element defined by the nodes.

    Parameters
    ----------
    self : RefTriangle3
        an RefTriangle3 object
    node : ndarray
        nodes of the element
    point : ndarray
        coordinates of the checked point
    normal_t : ndarray
        (optional) normal of another element

    Returns
    -------
    is_inside: bool
        true if the point is inside the element
    """
    point_ref = self.get_ref_point(node, point)
    s = point_ref[0]
    t = point_ref[1]
    a = s
    b = t
    c = 1 - s - t
    is_inside = (a > -self.epsilon) & (b > -self.epsilon) & (c > -self.epsilon)

    # Optional : Check that normals are almost aligned
    if normal_t is not None:
        normal_s = self.get_normal(node)
        scal_st = dot(normal_t[0:2], normal_s)
        is_colinear = abs(scal_st) > 1 - 2 * self.epsilon
        is_inside = is_inside & is_colinear

    return is_inside, a, b
