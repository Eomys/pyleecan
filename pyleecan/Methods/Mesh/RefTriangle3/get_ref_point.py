# -*- coding: utf-8 -*-

import numpy as np


def get_ref_point(self, vertice, point):
    """Return the coordinate of the equivalent point in the ref element

    Parameters
    ----------
    self : RefTriangle3
        a RefTriangle3 object
    vertice : ndarray
        vertice of the element
    point : ndarray
        coordinates of a point

        Returns
    -------
    pt1_ref : ndarray
        coordinates of the ref point
    """

    [jacob, detJ] = self.jacobian(point, vertice)
    inv_jacob = np.linalg.inv(jacob)
    point_ref = np.dot((point - vertice[0, :]), inv_jacob)

    return point_ref
