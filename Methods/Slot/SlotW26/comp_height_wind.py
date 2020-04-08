# -*- coding: utf-8 -*-

from numpy import arcsin, cos


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    # Height of the arc (P2,C1,P7)
    alpha2 = arcsin(self.W0 / (2.0 * self.R1))
    Harc2 = float(self.R1 * (1 - cos(alpha2)))

    return self.H1 + self.R2 + self.R1 - Harc2
