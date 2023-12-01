# -*- coding: utf-8 -*-

import numpy as np


def get_normal(self, element_coordinate: np.ndarray) -> np.ndarray:
    """Return the normal vector.

    Parameters
    ----------
    self : RefSegmentP1
        a RefSegmentP1 object
    element_coordinate : ndarray
        coordinates of the element

    Returns
    -------
    normal: ndarray
        Normal coordinate
    """

    t = element_coordinate[0, :] - element_coordinate[1, :]
    n = np.cross([t[0], t[1], 0], [0, 0, 1])[0:2]
    n = n / np.linalg.norm(n)

    return n
