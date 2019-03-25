# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType11.comp_active_surface
Conductor Type 1_1 comp_active_surface method
@date Created on Mon Jan 12 17:20:56 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface_active(self):
    """Compute the active surface of the conductor

    Parameters
    ----------
    self : CondType11
        A CondType11 object

    Returns
    -------
    Sact: float
        Surface without insulation [m**2]

    """

    Sact = self.Hwire * self.Wwire * self.Nwppc_tan * self.Nwppc_rad

    return Sact
