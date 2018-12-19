# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType22.comp_surface
Conductor Type 2_2 comp_surface method
@date Created on Thu Jul 30 13:52:07 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface(self):
    """Compute the surface of the conductor

    Parameters
    ----------
    self : CondType22
        A CondType22 object

    Returns
    -------
    S: float
        Surface of the conductor (with insulation) [m**2]

    """

    return self.Sbar
