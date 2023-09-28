# -*- coding: utf-8 -*-

import numpy as np


def shape_function(self, points, nb_pt):
    """Return the values of linear shape functions in reference triangle for a given point"""
    # nb_pt = points.shape[0]
    values = np.zeros([nb_pt, 1, 3], dtype=float)
    for i in range(nb_pt):
        if nb_pt == 1:
            [x, y] = points[0:2]
        else:
            [x, y] = points[i, 0:2]

        # if (x >= 0) and (y >= 0) and (1 - x - y >= 0):
        values[i, 0, 0] = 1 - x - y
        values[i, 0, 1] = x
        values[i, 0, 2] = y

    size = 3

    return values, size
