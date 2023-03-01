# -*- coding: utf-8 -*-


def get_gauss_points(self):
    """Return the gauss points and weights for Triangle3 cell"""

    raise Exception(
        "Quadpy is not possible to use anymore, need to rewrite this method"
    )
    nb_gauss_points = self.nb_gauss_point
    scheme = quadpy.tn.grundmann_moeller(2, nb_gauss_points)
    gauss_pts = scheme.points
    weights = scheme.weights

    return gauss_pts, weights, nb_gauss_points
