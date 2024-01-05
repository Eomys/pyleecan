# -*- coding: utf-8 -*-

import numpy as np


def get_real_point(
    self, element_coordinate: np.ndarray, ref_pt: np.ndarray, nb_ref_pt: int = 1
) -> np.ndarray:
    """Return the coordinates in the element of a point in the reference element.

    Parameters
    ----------
    self : RefTriangle3
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

    vert = element_coordinate[:, 0:2]
    real_points = np.zeros((nb_ref_pt, 2))

    for ii in range(nb_ref_pt):
        if nb_ref_pt == 1:
            pt = ref_pt
        else:
            pt = ref_pt[ii, :]

        [jacob, detJ] = self.jacobian(pt, vert)
        real_points[ii, :] = np.array(vert[0, :] + np.dot(pt, jacob), dtype=float)

    return real_points
