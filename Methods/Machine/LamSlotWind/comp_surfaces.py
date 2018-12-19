# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotWind.comp_surfaces
Lamination with winding computation of all surfaces method
@date Created on Mon Jan 12 17:09:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi
from pyleecan.Classes.LamSlot import LamSlot


def comp_surfaces(self):
    """Compute the Lamination surfaces (Slam, Svent, Sslot, Swind)

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionnary (Slam, Svent, Sslot, Swind) [m**2]

    """

    S_dict = LamSlot.comp_surfaces(self)

    S_dict["Swind"] = self.slot.Zs * self.slot.comp_surface_wind()

    return S_dict
