# -*- coding: utf-8 -*-
from numpy import sinh, cosh, sin, cos


def comp_phip_skin(self, u):
    """phip_skin for skin effect computation

    Parameters
    ----------
    self : Conductor
        An Conductor object

    Returns
    -------
    None
    """

    y = (
        (3 / (2 * u)) * (sinh(2 * u) - sin(2 * u)) / (cosh(2 * u) - cos(2 * u))
    )  # p257 Pyrhonen
    # y[u==0]=1

    return y
