# -*- coding: utf-8 -*-

from numpy import sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    Rbo = self.get_Rbo()

    W0m = self.comp_W0m()
    S1 = self.H0 * W0m

    # The bottom is an arc
    alpha = self.comp_angle_opening_magnet()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    S2 = self.H1 * self.W1

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S1 + S2 - Sarc
    else:
        return S1 + S2 + Sarc
