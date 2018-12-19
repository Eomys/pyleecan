# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType11.comp_surface
Conductor Type 1_1 comp_surface method
@date Created on Wed Jan 21 13:52:07 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_surface(self):
    """Compute the surface of the conductor

    Parameters
    ----------
    self : CondType11
        A CondType11 object

    Returns
    -------
    S: float
        Surface of the conductor (with insulation) [m**2]

    """

    S = self.comp_height() * self.comp_width()

    return S
