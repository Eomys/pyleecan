# -*- coding: utf-8 -*-
from numpy import sinh, cosh, sin, cos


def comp_psip_skin(self, u):
    """psip_skin for skin effect computation

    Parameters
    ----------
    self : Conductor
        An Conductor object

    Returns
    -------
    None
    """

    y = (1 / u) * (sinh(u) + sin(u)) / (cosh(u) + cos(u))  # p257 Pyrhonen
    # y[u==0]=1

    return y
