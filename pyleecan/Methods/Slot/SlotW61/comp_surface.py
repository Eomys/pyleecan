# -*- coding: utf-8 -*-

from numpy import pi, arcsin, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    point_dict = self._comp_point_coordinate()
    Z5 = point_dict["Z5"]
    Rext = self.get_Rbo()
    Rint = abs(Z5)

    # Surface of a slot pitch
    Sring = (pi * Rext ** 2 - pi * Rint ** 2) * 1 / self.Zs

    # Tooth surface
    St = self.H1 * self.W1 + self.H2 * self.W2 + self.H0 * (self.W0 + self.W1) / 2

    alpha_top = 2 * arcsin(self.W0 / (2 * Rext))
    Sarc_top = (Rext ** 2.0) / 2.0 * (alpha_top - sin(alpha_top))

    alpha_bot = 2 * arcsin(self.W2 / (2 * Rint))
    Sarc_bot = (Rint ** 2.0) / 2.0 * (alpha_bot - sin(alpha_bot))

    return Sring - (St + Sarc_top - Sarc_bot)
