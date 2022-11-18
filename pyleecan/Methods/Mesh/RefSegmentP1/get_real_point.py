# -*- coding: utf-8 -*-

import numpy as np


def get_real_point(self, vertice, ref_pt, nb_ref_pt=1):
    """Return the coordinates in the cell of a point in the reference cell.

    Parameters
    ----------
    self : RefCell
         an RefCell object
    vertice : ndarray
        vertices of the cell
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
        real_points[ii, :] = vertice[0, :] + s * (vertice[1, :] - vertice[0, :])

    return real_points
