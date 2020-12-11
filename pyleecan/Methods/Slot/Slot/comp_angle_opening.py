# -*- coding: utf-8 -*-

from numpy import angle


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    line_list = self.build_geometry()
    Z1 = line_list[0].get_begin()
    Z2 = line_list[-1].get_end()

    return angle(Z2) - angle(Z1)
