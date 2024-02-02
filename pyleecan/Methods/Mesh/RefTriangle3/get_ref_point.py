# -*- coding: utf-8 -*-

import numpy as np


def get_ref_point(
    self, element_coordinate: np.ndarray, point: np.ndarray
) -> np.ndarray:
    """Return the coordinate of the equivalent point in the ref element

    Parameters
    ----------
    self : RefTriangle3
        a RefTriangle3 object
    element_coordinate : ndarray
        coordinates of the element
    point : ndarray
        coordinates of a point

        Returns
    -------
    pt1_ref : ndarray
        coordinates of the ref point
    """

    jacob, _ = self.jacobian(point, element_coordinate)
    inv_jacob = np.linalg.inv(jacob)
    point_ref = np.dot((point - element_coordinate[0, :]), inv_jacob)

    return point_ref
