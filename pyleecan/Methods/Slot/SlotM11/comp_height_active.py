# -*- coding: utf-8 -*-

from numpy import abs as np_abs


def comp_height_active(self):
    """Compute the height of the active area

    Parameters
    ----------
    self : SlotM11
        A SlotM11 object

    Returns
    -------
    Hwind: float
        Height of the active area [m]

    """

    return self.H1
