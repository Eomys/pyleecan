# -*- coding: utf-8 -*-
from numpy import sinh, cosh, sin, cos


def comp_phi_skin(self, u):
    """phi_skin for skin effect computation

    Parameters
    ----------
    self : Conductor
        An Conductor object

    Returns
    -------
    None
    """

    y = (
        u * (sinh(2 * u) + sin(2 * u)) / (cosh(2 * u) - cos(2 * u))
    )  # Trickey model cf 5.26 p271 Pyrhonen
    # y[u==0]=1

    return y
