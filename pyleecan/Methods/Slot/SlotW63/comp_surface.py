# -*- coding: utf-8 -*-

from numpy import pi, arcsin, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    point_dict = self._comp_point_coordinate()
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Rext = self.get_Rbo()
    Rint = abs(Z5)

    # Surface of a slot pitch
    Sring = (pi * Rext ** 2 - pi * Rint ** 2) / self.Zs

    # Surface define by arc of circle between Z4 and Z5 with radius abs(Z5)
    # bottom is not a cercle
    D54 = abs(Z5 - Z4)
    alpha = 2 * arcsin(D54 / (2 * Rint))
    Sarc_bot2 = (Rint ** 2.0) / 2.0 * (alpha - sin(alpha))

    # Tooth surface
    H = sin(self.H1) * (self.W1 - self.W0) / 2
    St = (
        self.H0 * self.W0
        + self.H2 * self.W1
        + H * (self.W1 - self.W0) / 2
        + self.W0 * H
    )

    # Surface define by arc of circle between Z8 and Z1d with radius rbo
    alpha_top = 2 * arcsin(self.W1 / (2 * Rext))
    Sarc_top = (Rext ** 2.0) / 2.0 * (alpha_top - sin(alpha_top))

    # Surface define by arc of circle between Z5 and Z4d with radius abs(Z5)
    alpha_bot = 2 * arcsin(self.W0 / (2 * Rint))
    Sarc_bot1 = (Rint ** 2.0) / 2.0 * (alpha_bot - sin(alpha_bot))

    return Sring - (St + Sarc_top - Sarc_bot1) + Sarc_bot2
