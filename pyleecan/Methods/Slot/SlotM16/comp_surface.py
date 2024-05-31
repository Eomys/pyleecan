# -*- coding: utf-8 -*-

from numpy import sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotM16
        A SlotM16 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    Rbo = self.get_Rbo()

    S0 = self.H0 * self.W0
    S1 = self.H1 * self.W1

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo**2.0) / 2.0 * (alpha - sin(alpha))

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S0 + S1 - Sarc
    else:
        return S0 + S1 + Sarc
