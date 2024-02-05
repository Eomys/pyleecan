# -*- coding: utf-8 -*-

import numpy as np


def grad_shape_function(self, point: np.ndarray) -> np.ndarray:
    """Return the gradient of linear shape functions in reference triangle for a given point

    Parameters
    ----------
    point : np.ndarray
        point where to compute the shape functions gradient values

    Returns
    -------
    np.ndarray
        shape function gradient values
    """

    return np.array([[-1, 1, 0], [-1, 0, 1]], dtype=np.float64)
