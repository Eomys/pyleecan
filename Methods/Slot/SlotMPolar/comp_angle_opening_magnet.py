# -*- coding: utf-8 -*-


def comp_angle_opening_magnet(self):
    """Compute the average opening angle of a single magnet

    Parameters
    ----------
    self : SlotMPolar
        A SlotMPolar object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    return self.W0
