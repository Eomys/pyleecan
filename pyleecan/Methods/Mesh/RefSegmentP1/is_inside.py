# -*- coding: utf-8 -*-

from typing import Optional, Tuple

import numpy as np


def is_inside(
    self,
    element_coordinate: np.ndarray,
    point: np.ndarray,
    normal_t: Optional[np.ndarray] = None,
) -> Tuple[bool, float, float]:
    """Check if a point is inside the element.

    Parameters
    ----------
    self : RefSegmentP1
        a RefSegmentP1 object
    element_coordinate : ndarray
        coordinates of the element
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

    # Convert world coordinates (x,y) to reference segment (-1,0)--(1,0)
    point_ref = self.get_ref_point(element_coordinate, point)
    s = point_ref[0]
    t = point_ref[1]

    a = max(0, abs(s) - 1)
    b = abs(t) / 2

    # The point projected in the reference element domain must be in a rectangle of size (2+2*epsilon)×(2*epsilon)
    # ? Why the tolerance is different according to the direction
    is_inside = (-1 - epsilon < point_ref[0] < 1 + epsilon) & (
        -epsilon < point_ref[1] < epsilon
    )

    # Check that normals are almost aligned
    if normal_t is not None:
        normal_s = self.get_normal(element_coordinate)
        scal_st = np.dot(normal_t[0:2], normal_s)
        is_colinear = abs(scal_st) > 1 - 2 * epsilon
        is_inside = is_colinear & is_inside

    # TODO return the distance to the element from a different method
    return is_inside, a, b
