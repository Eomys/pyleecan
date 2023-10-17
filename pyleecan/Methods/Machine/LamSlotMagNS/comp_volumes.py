# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.LamSlot import LamSlot


def comp_volumes(self):
    """Compute the Lamination volumes (Vlam, Vvent, Vslot, Vmag)

    Parameters
    ----------
    self : LamSlotMagNS
        A LamSlotMagNS object

    Returns
    -------
    V_dict: dict
        Lamination surface dictionary (Vlam, Vvent, Vslot, Vmag) [m**3]

    """

    V_dict = LamSlot.comp_volumes(self)
    Vmag = 0
    if self.magnet_north is not None:
        Vmag += self.slot.comp_surface_active() * self.magnet_north.Lmag
    if self.magnet_south is not None:
        Vmag += self.slot_south.comp_surface_active() * self.magnet_south.Lmag

    V_dict["Vmag"] = Vmag

    return V_dict
