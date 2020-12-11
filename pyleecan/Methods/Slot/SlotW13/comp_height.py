# -*- coding: utf-8 -*-

from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW13
        A SlotW13 object

    Returns
    -------
    Htot: Height of the slot [m]

    """

    Rbo = self.get_Rbo()

    H1 = self.get_H1()

    # Computation of the arc height
    alpha = self.comp_angle_opening() / 2
    Harc = float(Rbo * (1 - cos(alpha)))

    if self.is_outwards():
        return abs(Rbo - Harc + self.H0 + H1 + self.H2 + 1j * self.W3 / 2.0) - Rbo
    else:
        return self.H0 + H1 + self.H2 + Harc
