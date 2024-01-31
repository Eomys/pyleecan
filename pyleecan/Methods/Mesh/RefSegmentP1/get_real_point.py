# -*- coding: utf-8 -*-

import numpy as np


def get_real_point(
    self, element_coordinate: np.ndarray, ref_pt: np.ndarray, nb_ref_pt: int = 1
) -> np.ndarray:
    """Return the coordinates in the element of a point in the reference element.

    Parameters
    ----------
    self : RefElement
         an RefElement object
    element_coordinate : ndarray
        coordinates of the element
    ref_pt : ndarray
        ref point(s)
    nb_ref_pt : int
        nb of ref points

    Returns
    -------
    real_points : ndarray
        points coordinate

    """

    real_points = np.zeros((nb_ref_pt, 2))

    for ii in range(nb_ref_pt):
        if nb_ref_pt == 1:
            s = ref_pt[0]
        else:
            s = ref_pt[ii, 0]

        length = 2
        s = (s + 1) / length
        real_points[ii, :] = element_coordinate[0, :] + s * (
            element_coordinate[1, :] - element_coordinate[0, :]
        )

    return real_points
