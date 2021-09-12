# -*- coding: utf-8 -*-

import numpy as np


def get_gauss_points(self):
    """Return the gauss points and weights for Segments"""

    nb_gauss_points = self.nb_gauss_point
    gauss_pts = np.zeros([nb_gauss_points, 2], dtype=float)

    gauss_pts[:, 0] = np.polynomial.legendre.leggauss(nb_gauss_points)[0]

    weights = np.polynomial.legendre.leggauss(nb_gauss_points)[1]

    return gauss_pts, weights, nb_gauss_points
