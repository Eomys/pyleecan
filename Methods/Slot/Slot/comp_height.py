# -*- coding: utf-8 -*-

from numpy import array


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    Rbo = self.get_Rbo()

    surf = self.get_surface()

    point_list = surf.discretize(200)
    point_list = array(point_list)
    if self.is_outwards():
        return max(abs(point_list)) - Rbo
    else:
        return Rbo - min(abs(point_list))
