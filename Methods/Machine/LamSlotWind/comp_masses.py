# -*- coding: utf-8 -*-

from pyleecan.Classes.LamSlot import LamSlot


def comp_masses(self):
    """Compute the Lamination masses

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionnary (Mtot, Mlam, Mwind) [kg]

    """

    M_dict = LamSlot.comp_masses(self)
    V_dict = self.comp_volumes()
    if self.winding is not None:
        Mwind = V_dict["Vwind"] * self.winding.mat_type.struct.rho
    else:
        Mwind = 0

    M_dict["Mtot"] += Mwind
    M_dict["Mwind"] = Mwind

    return M_dict
