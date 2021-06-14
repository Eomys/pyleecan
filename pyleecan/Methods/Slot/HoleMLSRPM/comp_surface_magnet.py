# -*- coding: utf-8 -*-
from numpy import exp, arcsin, tan, cos, sqrt, sin


def comp_surface_magnet(self):
    """Compute the surface of the Hole

    Parameters
    ----------
    self : HoleMLSRPM
        A HoleMLSRPM object

    Returns
    -------
    S: float
        Surface of the Magnet. [m**2]

    """

    point_dict = self._comp_point_coordinate()
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]


    # symmetry

    x3 = Z3.real
    y3 = Z3.imag
    x4 = Z4.real
    y4 = Z4.imag

    x7 = Z7.real
    y7 = Z7.imag
    x8 = Z8.real
    y8 = Z8.imag

    S_magnet_1 = x3 * y4 + x4 * y7 + x7 * y8 + x8 * y3
    S_magnet_2 = x3 * y8 + x4 * y3 + x7 * y4 + x8 * y7

    S_magnet = 0.5 * abs(S_magnet_1 - S_magnet_2)

    return S_magnet
