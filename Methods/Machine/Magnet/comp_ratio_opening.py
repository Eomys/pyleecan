# -*- coding: utf-8 -*-

from numpy import pi


def comp_ratio_opening(self, p):
    """Compute the magnet pole arc width to pole width ratio

    Parameters
    ----------
    self : Magnet
        A Magnet object
    p : int
        Pole pair number

    Returns
    -------
    taum: float
        Ratio magnet pole arc width to pole width []

    """

    return self.comp_angle_opening() / (2 * pi / (2 * p))
