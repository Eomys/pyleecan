# -*- coding: utf-8 -*-
from numpy import sinh, cosh, sin, cos


def comp_psi_skin(self, u):
    """psi_skin for skin effect computation

    Parameters
    ----------
    self : Conductor
        An Conductor object

    Returns
    -------
    None
    """

    y = (
        2 * u * (sinh(u) - sin(u)) / (cosh(u) + cos(u))
    )  # Trickey model cf 5.26 p271 Pyrhonen
    # y[u==0]=1

    return y
