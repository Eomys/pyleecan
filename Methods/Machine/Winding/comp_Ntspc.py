# -*- coding: utf-8 -*-
"""@package

@date Created on Wed Apr 27 15:19:10 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""
from pyleecan.Methods.Machine.Winding import WindingError


def comp_Ntspc(self, Zs=None):
    """Compute the number of turns in series per phase

    Parameters
    ----------
    self : Winding
        A Winding object
    Zs : int
        Number of slot

    Returns
    -------
    Ntspc: float
        Number of turns in series per phase

    """
    if Zs is None:
        if self.parent is None:
            raise WindingError("ERROR: The Winding object must be in a Lamination object.")

        if self.parent.slot is None:
            raise WindingError("ERROR: The Winding object must be in a Lamination object with Slot.")

        Zs = self.parent.slot.Zs

    Ncspc = self.comp_Ncspc(Zs)

    return Ncspc * self.Ntcoil
