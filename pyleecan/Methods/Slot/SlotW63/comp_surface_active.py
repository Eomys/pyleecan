# -*- coding: utf-8 -*-
from numpy import arcsin, sin


def comp_surface_active(self):
    """Compute the Slot inner surface for winding

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """
    Rbo = self.get_Rbo()
    surface = self.comp_surface()

    point_dict = self._comp_point_coordinate()
    Zw1 = point_dict["Zw1"]
    Zw2 = point_dict["Zw2"]
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]

    s_bottom = abs(Zw1 - Zw2) * self.W2

    # top cercle
    D81 = abs(Z8 - Z1)
    alpha = 2 * arcsin(D81 / (2 * Rbo))
    Sarc_top = (Rbo**2.0) / 2.0 * (alpha - sin(alpha))

    D72 = abs(Z7 - Z2)

    Striangle = (Z8.real - Z7.real) * (Z8.imag - Z7.imag)

    Srect = D72 * (Z8.real - Z7.real)

    return surface - s_bottom - Sarc_top - Striangle - Srect
