# -*- coding: utf-8 -*-


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotMPolar
        A SlotMPolar object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    Nmag = len(self.magnet)
    return self.W0 * Nmag + self.W3 * (Nmag - 1)
