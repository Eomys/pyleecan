# -*- coding: utf-8 -*-
import numpy as np


def get_normal(self, element_coordinate: np.ndarray) -> np.ndarray:
    """Return the array of the normals coordinates.

    Parameters
    ----------
    element_coordinate : ndarray
        Coordinate of the element

    Returns
    -------
    normal : ndarray
        Normal vectors

    Raises
    ------
    NotImplementedError
        RefTriangle3.get_normal is not implemented.
    """

    # u1 = element_coordinate[1, :] - element_coordinate[0, :]
    # u2 = element_coordinate[2, :] - element_coordinate[0, :]
    # n = np.cross(u1, u2)
    # n = n / np.linalg.norm(n)
    raise NotImplementedError("RefTriangle3.get_normal is not implemented.")
