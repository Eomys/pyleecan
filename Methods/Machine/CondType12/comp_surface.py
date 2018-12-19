# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType12.comp_surface
Conductor Type 1_2 comp_surface method
@date Created on Wed Jan 21 13:52:19 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi


def comp_surface(self):
    """Compute the surface of the conductor

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    S: float
        Surface of the conductor (with insulation) [m**2]

    """

    return pi * ((self.Wins_cond / 2.0) ** 2)
