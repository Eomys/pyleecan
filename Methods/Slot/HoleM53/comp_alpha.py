# -*- coding: utf-8 -*-
from numpy import pi


def comp_alpha(self):
    """Compute the magnets angle of the slot type 53

    Parameters
    ----------
    self : HoleM53
        a HoleM53 object

    Returns
    -------
    alpha: float
        magnet angle [rad]
    """
    return pi / 2 - self.W4
