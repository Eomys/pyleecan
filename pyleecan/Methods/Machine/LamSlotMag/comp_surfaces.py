# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.LamSlot import LamSlot


def comp_surfaces(self):
    """Compute the Lamination surfaces (Slam, Svent, Sslot, Smag)

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionnary (Slam, Svent, Sslot, Smag) [m**2]

    """

    S_dict = LamSlot.comp_surfaces(self)
    Smag = self.slot.comp_surface_active()

    S_dict["Smag"] = Smag

    return S_dict
