# -*- coding: utf-8 -*-


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    (alpha_0, alpha_2) = self.comp_alphas()
    return alpha_0
