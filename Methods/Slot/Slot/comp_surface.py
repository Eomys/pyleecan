# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot.comp_surface
Slot Computation of surface (Numerical) method
@date Created on Wed Jul 11 17:22:33 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface(self):
    """Compute the Slot total surface (by numerical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    surf = self.get_surface()
    return surf.comp_surface()
