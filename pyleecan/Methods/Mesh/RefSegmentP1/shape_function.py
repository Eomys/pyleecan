# -*- coding: utf-8 -*-

from typing import Tuple

import numpy as np


def shape_function(self, points: np.ndarray) -> Tuple[np.ndarray, int]:
    """Return the values of linear shape functions in reference 2 node segment for a given point

    Parameters
    ----------
    self : RefSegmentP1
         an RefElement object
    points : ndarray
        ref points

    Returns
    -------
    value: array
        interpolated field

    """

    if points.ndim == 1:
        points = points.reshape(1, -1)

    nb_func = 2
    values = np.zeros([points.shape[0], 1, nb_func], dtype=float)
    # the "1" dimension is important for scalar product calculations

    for i, (x, y) in enumerate(points[:, :2]):
        if (x >= -1) and (x <= 1):
            values[i, 0, 0] = (1 - 1 * x) / 2
            values[i, 0, 1] = (x + 1) / 2
        # ! The shape function should be zero outside the element
        # elif x < -1:
        #     values[i, 0, 0] = (3 + x) / 2
        #     values[i, 0, 1] = -(1 + x) / 2
        # elif x > 1:
        #     values[i, 0, 0] = -(1 - x) / 2
        #     values[i, 0, 1] = (3 - x) / 2
    return values, nb_func
