# -*- coding: utf-8 -*-

import numpy as np


def grad_shape_function(self, point):
    """Return the gradient of linear shape functions in reference triangle for a given point"""

    values = np.zeros([2, 3], dtype=float)
    (x, y) = point[0:2]

    values[0, 0] = -1
    values[0, 1] = 1
    values[0, 2] = 0
    values[1, 0] = -1
    values[1, 1] = 0
    values[1, 2] = 1

    return values
