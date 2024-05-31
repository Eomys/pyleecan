# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.Lamination import Lamination


def comp_surfaces(self):
    """Compute the Lamination surfaces (Lamination, Ventilation, Slot).

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionary (Slam, Svent, Sslot, Syoke, Steeth) [m**2]

    """

    S_dict = Lamination.comp_surfaces(self)
    if self.slot is None:
        Sslot = 0
    else:
        Sslot = self.get_Zs() * self.slot.comp_surface()

    Ryoke = self.get_Ryoke()
    Hyoke = self.comp_height_yoke()
    if self.is_internal:
        S_dict["Syoke"] = pi * ((Ryoke + Hyoke) ** 2 - Ryoke**2) - S_dict["Svent"]
    else:
        S_dict["Syoke"] = pi * (Ryoke**2 - (Ryoke - Hyoke) ** 2) - S_dict["Svent"]

    S_dict["Sslot"] = Sslot
    S_dict["Slam"] -= Sslot
    S_dict["Steeth"] = S_dict["Slam"] - S_dict["Syoke"]
    return S_dict
