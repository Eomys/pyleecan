# -*- coding: utf-8 -*-


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotMFlat2
        A SlotMFlat2 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    alpha0 = self.comp_angle_opening_slot()
    alpha3 = self.W3

    Nmag = len(self.magnet)
    if Nmag > 0:
        return alpha0 * Nmag + alpha3 * (Nmag - 1)
    else:
        return 0
