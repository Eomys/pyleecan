# -*- coding: utf-8 -*-

import numpy as np


def get_normal(self, vertice):
    """Return the normal vector.

    Parameters
    ----------
    self : RefSegmentP1
        a RefSegmentP1 object
    vertice : ndarray
        vertice of the element

    Returns
    -------
    normal: ndarray
        Normal coordinate
    """

    t = vertice[0, :] - vertice[1, :]
    n = np.cross([t[0], t[1], 0], [0, 0, 1])[0:2]
    n = n / np.linalg.norm(n)

    return n
