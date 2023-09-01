# -*- coding: utf-8 -*-

from numpy import abs as np_abs
from numpy import sqrt


def comp_height_active(self):
    """Compute the height of the active area

    Parameters
    ----------
    self : SlotM19
        A SlotM19 object

    Returns
    -------
    Hwind: float
        Height of the active area [m]

    """
    return self.comp_height()
