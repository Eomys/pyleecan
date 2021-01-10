# -*- coding: utf-8 -*-

import numpy as np


def get_normal(self, vertice):
    """Return the array of the normals coordinates.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)
    loc : str
        localization of the normals ("center" or "point")

    Returns
    -------
    normals: ndarray
        Normals coordinates
    """

    # u1 = vertice[1, :] - vertice[0, :]
    # u2 = vertice[2, :] - vertice[0, :]
    # n = np.cross(u1, u2)
    # n = n / np.linalg.norm(n)

    return None
