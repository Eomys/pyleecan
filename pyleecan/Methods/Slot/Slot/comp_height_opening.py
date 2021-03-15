# -*- coding: utf-8 -*-
from numpy import array


def comp_height_opening(self, Ndisc=200):
    """Compute the height of the opening area (Hslot - Hactive)

    Parameters
    ----------
    self : Slot
        A Slot object
    Ndisc : int
        Number of point to discretize the lines

    Returns
    -------
    Hwind: float
        Height of the opening area [m]

    """

    return self.comp_height(Ndisc=Ndisc) - self.comp_height_active(Ndisc=Ndisc)
