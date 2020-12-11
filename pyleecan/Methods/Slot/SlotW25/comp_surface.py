# -*- coding: utf-8 -*-

from numpy import pi, arcsin, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = self._comp_point_coordinate()

    if self.is_outwards():
        Rint = abs(Z1)
        Rext = abs(Z2)
    else:
        Rint = abs(Z2)
        Rext = abs(Z1)

    # Surface of a slot pitch
    Sring = (pi * Rext ** 2 - pi * Rint ** 2) * 1 / self.Zs

    Swind = self.comp_surface_wind()
    # Tooth surface
    St = self.H1 * self.W4

    alpha_bore = 2 * arcsin(self.W4 / (2 * Rint))
    Sarc_bore = (Rint ** 2.0) / 2.0 * (alpha_bore - sin(alpha_bore))

    alpha_yoke = 2 * arcsin(self.W4 / (2 * Rext))
    Sarc_yoke = (Rext ** 2.0) / 2.0 * (alpha_yoke - sin(alpha_yoke))

    return Swind + Sring - (St + Sarc_yoke - Sarc_bore)
