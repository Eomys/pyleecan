# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType21.comp_width
Conductor Type 2_1 width computation method
@date Created on Tue Jan 20 15:24:57 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_width(self):
    """Compute the width of the conductor

    Parameters
    ----------
    self : CondType21
        A CondType21 object

    Returns
    -------
    W: float
        Width of the conductor (with insulation) [m]

    """

    return self.Wbar + 2 * self.Wins
