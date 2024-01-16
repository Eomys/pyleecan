# -*- coding: utf-8 -*-

from typing import Tuple

import numpy as np


def jacobian(
    self, point: np.ndarray, element_coordinate: np.ndarray
) -> Tuple[np.ndarray, float]:
    """Compute jacobian, jacobian determinant and jacobian derivatives for linear triangle.

    Parameters
    ----------
    point: ndarray
        coordinates of the point where the jabobian is computed
    element_coordinate: ndarray
        coordinates of the element

    Returns
    -------

    """

    grad_func = self.grad_shape_function(point)
    jacob = np.dot(grad_func, element_coordinate[:, :2])
    det_jacob = np.linalg.det(jacob)

    return jacob, det_jacob
