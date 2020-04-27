# -*- coding: utf-8 -*-

from numpy import pi, arcsin


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    slot_pitch = 2 * pi / self.Zs
    tooth_angle = float(2 * arcsin(self.W0 / (2 * self.get_Rbo())))

    return slot_pitch - tooth_angle
