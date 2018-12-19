# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW24.comp_surface
SlotW24 Computation of surface method
@date Created on Mon Jul 06 11:40:07 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    return self.comp_surface_wind()
