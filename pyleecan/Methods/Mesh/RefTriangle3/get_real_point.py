# -*- coding: utf-8 -*-

import numpy as np


def get_real_point(self, vertice, ref_pt, nb_ref_pt=1):
    """Return the coordinates in the cell of a point in the reference cell.

    Parameters
    ----------
    self : RefTriangle3
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

    vert = vertice[:, 0:2]
    real_points = np.zeros((nb_ref_pt, 2))

    for ii in range(nb_ref_pt):
        if nb_ref_pt == 1:
            pt = ref_pt
        else:
            pt = ref_pt[ii, :]

        [jacob, detJ] = self.jacobian(pt, vert)
        real_points[ii, :] = np.array(vert[0, :] + np.dot(pt, jacob), dtype=float)

    return real_points
