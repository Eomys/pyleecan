# -*- coding: utf-8 -*-

from numpy import sin, tan


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    Rbo = self.get_Rbo()

    S1 = self.H0 * self.W0
    if self.H1_is_rad:  # H1 in rad
        H1 = (self.W1 - self.W0) / 2.0 * tan(self.H1)  # H1 in m
    else:  # H1 in m
        H1 = self.H1
    S2 = 0.5 * (self.W0 + self.W1) * H1
    Swind = self.comp_surface_wind()

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S1 + S2 + Swind - Sarc
    else:
        return S1 + S2 + Swind + Sarc
