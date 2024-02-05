# -*- coding: utf-8 -*-

import numpy as np


def grad_shape_function(self, points: np.ndarray):
    """Return the values of linear shape functions in reference triangle for a given point"""

    values = np.zeros([2, 2], dtype=float)
    [x, y] = points
    if (x >= -1) and (x <= 1):
        values[0, 0] = -1 / 2
        values[0, 1] = 1 / 2

    return values
