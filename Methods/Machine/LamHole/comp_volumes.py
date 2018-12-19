# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamHole.comp_volumes
Lamination with Buried Magnets computation of all volumes method
@date Created on Mon Jan 12 17:09:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi
from pyleecan.Classes.Lamination import Lamination


def comp_volumes(self):
    """Compute the Lamination volumes

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    V_dict: dict
        Lamination volume dictionnary (Vlam, Vvent, Vmag, Vhole) [m**3]

    """

    V_dict = Lamination.comp_volumes(self)
    Lt = self.comp_length()

    Vhole = 0
    Vmag = 0
    for hole in self.hole:
        Vhole += hole.Zh * hole.comp_surface() * Lt
        if hole.has_magnet():
            Vmag += hole.Zh * hole.comp_volume_magnets()

    V_dict["Vmag"] = Vmag
    V_dict["Vhole"] = Vhole

    return V_dict
