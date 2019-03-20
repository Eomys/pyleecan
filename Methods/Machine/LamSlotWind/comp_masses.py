# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotWind._comp_masses
Lamination with Winding computation of all masses method
@date Created on Tue Jan 13 15:26:49 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

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
    Mwind = V_dict["Vwind"] * self.winding.mat_type.struct.rho

    M_dict["Mtot"] += Mwind
    M_dict["Mwind"] = Mwind

    return M_dict
