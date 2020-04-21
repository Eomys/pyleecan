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
        Lamination surface dictionnary (Slam, Svent, Sslot) [m**2]

    """

    S_dict = Lamination.comp_surfaces(self)
    if self.slot is None:
        Sslot = 0
    else:
        Sslot = self.get_Zs() * self.slot.comp_surface()

    S_dict["Sslot"] = Sslot
    S_dict["Slam"] -= Sslot
    return S_dict
