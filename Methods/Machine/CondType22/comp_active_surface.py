# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType22.comp_active_surface
Conductor Type 2_2 comp_active_surface method
@date Created on Thu Jul 30 15:07:56 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_active_surface(self):
    """Compute the active surface of the conductor

    Parameters
    ----------
    self : CondType22
        A CondType22 object

    Returns
    -------
    Sact: float
        Surface without insulation [m**2]

    """

    return self.Sbar
