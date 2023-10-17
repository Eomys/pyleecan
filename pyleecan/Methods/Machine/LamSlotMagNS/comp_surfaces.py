# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.LamSlot import LamSlot


def comp_surfaces(self):
    """Compute the Lamination surfaces (Slam, Svent, Sslot, Smag)

    Parameters
    ----------
    self : LamSlotMagNS
        A LamSlotMagNS object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionary (Slam, Svent, Sslot, Smag) [m**2]

    """

    S_dict = LamSlot.comp_surfaces(self)
    Smag = 0
    if self.magnet_north is not None:
        Smag += self.slot.comp_surface_active()
    if self.magnet_south is not None:
        Smag += self.slot_south.comp_surface_active()

    S_dict["Smag"] = Smag

    return S_dict
