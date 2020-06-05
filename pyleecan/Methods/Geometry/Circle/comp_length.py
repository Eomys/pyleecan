# -*- coding: utf-8 -*-
from numpy import pi


def comp_length(self):
    """Compute the length of the circle

    Parameters
    ----------
    self : Circle
        A Circle object

    Returns
    -------
    length : float
        the length of the circle [m]

    """
    # Check if the circle is correct
    self.check()

    length = self.radius * 2 * pi

    return length
