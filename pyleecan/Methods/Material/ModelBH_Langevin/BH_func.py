# -*- coding: utf-8 -*-
from numpy import cosh, sinh, ndarray, argwhere, isnan as np_isnan


from math import isnan


def BH_func(self, H, Bs, a):
    """
    Return the B from H according to Langevin model.

    Parameters
    ----------
    self : ModelBH_Langevin
        a ModelBH_Langevin object

    Returns
    -------
    B: numpy.ndarray
        B(H) values

    """
    B = Bs * (cosh(H / a) / sinh(H / a) - a / H)

    if isinstance(B, ndarray):
        B[argwhere(np_isnan(B))] = Bs
        B[argwhere(H == 0)] = 0
    elif isnan(B):
        if H == 0:
            B = 0
        else:
            B = Bs

    return B
