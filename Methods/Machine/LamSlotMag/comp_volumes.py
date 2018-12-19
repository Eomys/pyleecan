# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotMag.comp_volumes
Lamination with magnets computation of all volumes method
@date Created on Mon Jan 12 17:09:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi
from pyleecan.Classes.LamSlot import LamSlot


def comp_volumes(self):
    """Compute the Lamination volumes (Vlam, Vvent, Vslot, Vmag)

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

    Returns
    -------
    V_dict: dict
        Lamination surface dictionnary (Vlam, Vvent, Vslot, Vmag) [m**3]

    """

    V_dict = LamSlot.comp_volumes(self)
    Vmag = 0
    for magnet in self.slot.magnet:
        Vmag += magnet.comp_volume()

    V_dict["Vmag"] = Vmag

    return V_dict
