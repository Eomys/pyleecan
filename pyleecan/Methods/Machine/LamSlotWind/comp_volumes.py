# -*- coding: utf-8 -*-

from ....Classes.LamSlot import LamSlot


def comp_volumes(self):
    """Compute the Lamination volumes (Vlam, Vvent, Vslot, Vwind)

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    V_dict: dict
        Lamination volume dictionary (Vlam, Vvent, Vslot, Vwind) [m**3]

    """

    V_dict = LamSlot.comp_volumes(self)
    Lf = self.comp_length()  # Include radial ventilation ducts
    if self.slot is None:
        V_dict["Vwind"] = 0
        V_dict["Vwedge"] = 0
    else:
        V_dict["Vwind"] = Lf * self.get_Zs() * self.slot.comp_surface_active()
        V_dict["Vwedge"] = Lf * self.get_Zs() * self.slot.comp_surface_wedges()
    return V_dict
