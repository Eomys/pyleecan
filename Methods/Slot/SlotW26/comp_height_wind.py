# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW26.comp_height_wind
Slot Type_2_6 computation of the height of the winding area method
@date Created on Mon Feb 22 12:06:14 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

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

    return self.H1 + 2 * self.R1 - Harc2
