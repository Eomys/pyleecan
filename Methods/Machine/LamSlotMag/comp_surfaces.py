# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotMag.comp_surfaces
Lamination with magnets computation of all surfaces method
@date Created on Mon Jan 12 17:09:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi
from pyleecan.Classes.LamSlot import LamSlot


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
    Smag = 0
    for magnet in self.slot.magnet:
        Smag += magnet.comp_surface()

    S_dict["Smag"] = Smag

    return S_dict
