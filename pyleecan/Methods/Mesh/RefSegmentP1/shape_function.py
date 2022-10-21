# -*- coding: utf-8 -*-

import numpy as np


def shape_function(self, g_point, nb_gpt):
    """Return the values of linear shape functions in reference 2 node segment for a given point

    Parameters
    ----------
    self : RefSegmentP1
         an RefCell object
    point : ndarray
        ref point

    Returns
    -------
    value: array
        interpolated field

    """

    nb_func = 2
    values = np.zeros(
        (nb_gpt, 1, nb_func), dtype=float
    )  # the "1" dimension is important for scalar product calculations

    for ig in range(nb_gpt):
        if nb_gpt == 1:
            [x, y] = g_point
        else:
            [x, y] = g_point[ig, :]

        if (x >= -1) and (x <= 1):
            values[ig, 0, 0] = (1 - x) / 2
            values[ig, 0, 1] = (1 + x) / 2
        elif x < -1:
            values[ig, 0, 0] = (3 + x) / 2
            values[ig, 0, 1] = -(1 + x) / 2
        elif x > 1:
            values[ig, 0, 0] = -(1 - x) / 2
            values[ig, 0, 1] = (3 - x) / 2
    return values, nb_func
