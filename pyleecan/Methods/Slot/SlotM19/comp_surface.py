# -*- coding: utf-8 -*-
from numpy import arcsin, pi, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotM19
        A SlotM19 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    Rbo = self.get_Rbo()
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo**2.0) / 2.0 * (alpha - sin(alpha))

    S1 = abs(Z1.real - Z2.real) * (self.W1 + self.W0) / 2

    if self.is_outwards():
        return S1 - Sarc
    else:
        return S1 + Sarc
