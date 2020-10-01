# -*- coding: utf-8 -*-

from numpy import cos


def comp_H_arc(self):
    """Compute the arc between bore radius an slot opening line.

    Parameters
    ----------
    self : SlotMFlat2
        A SlotMFlat2 object

    Returns
    -------
    Harc: float
        Distance between bore radius and slot opening line [m]

    """
    Rbo = self.get_Rbo()
    alpha_slot = self.comp_angle_opening()

    Rarc = cos(alpha_slot / 2) * Rbo

    return Rbo - Rarc
