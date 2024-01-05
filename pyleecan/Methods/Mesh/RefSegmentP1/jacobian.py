# -*- coding: utf-8 -*-

from typing import Tuple

import numpy as np


def jacobian(
    self, point: np.ndarray, element_coordinate: np.ndarray
) -> Tuple[np.ndarray, float]:
    """Compute jacobian, jacobian determinant and jacobian derivatives for linear triangle.

    Parameters
    ----------
    point : ndarray
        coordinate of the point where the jacobian is calculated
    element_coordinate : ndarray
        coordinates of the element

    Returns
    -------
    jabob : ndarray
        jacobian matrix
    det_jacob : float
        jacobian matrix determinant
    """

    grad_func = self.grad_shape_function(point)
    jacob = np.dot(grad_func, element_coordinate)
    det_jacob = (
        np.sqrt(
            (element_coordinate[1, 0] - element_coordinate[0, 0]) ** 2
            + (element_coordinate[1, 1] - element_coordinate[0, 1]) ** 2
        )
        / 2
    )

    return jacob, det_jacob
