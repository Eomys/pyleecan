# -*- coding: utf-8 -*-

from typing import Tuple

import numpy as np


def shape_function(self, points: np.ndarray) -> Tuple[np.ndarray, int]:
    """Return the values of linear shape functions in reference triangle for a given point"""
    if points.ndim == 1:
        points = points.reshape(1, -1)

    nb_shape_func = 3
    values = np.zeros([points.shape[0], 1, nb_shape_func], dtype=float)
    # TODO this implementation assumes that the points are contained in the same z plane
    for i, (x, y) in enumerate(points[:, :2]):
        values[i, 0, 0] = 1 - x - y
        values[i, 0, 1] = x
        values[i, 0, 2] = y

    return values, nb_shape_func
