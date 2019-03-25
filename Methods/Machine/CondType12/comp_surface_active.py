# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType12.comp_active_surface
Conductor Type 1_2 comp_active_surface method
@date Created on Mon Jan 12 17:26:03 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi


def comp_surface_active(self):
    """Compute the active surface of the conductor

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    Sact: float
        Surface without insulation [m**2]

    """

    Sact = ((self.Wwire / 2.0) ** 2) * pi * self.Nwppc

    return Sact
