# -*- coding: utf-8 -*-

from numpy import cos, tan


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    Rbo = self.get_Rbo()

    if self.H1_is_rad:  # H1 in rad
        H1 = (self.W1 - self.W0) / 2.0 * tan(self.H1)  # convertion to m
    else:  # H1 in m
        H1 = self.H1

    # Computation of the arc height
    alpha = self.comp_angle_opening() / 2
    Harc = float(Rbo * (1 - cos(alpha)))

    if self.is_outwards():
        return abs(Rbo - Harc + self.H0 + H1 + self.H2 + 1j * self.W2 / 2.0) - Rbo
    else:
        return self.H0 + H1 + self.H2 + Harc
