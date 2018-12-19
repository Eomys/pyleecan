# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType21.comp_height
Conductor Type 2_1 height computation method
@date Created on Tue Jan 20 12:14:57 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height(self):
    """Compute the height of the conductor

    Parameters
    ----------
    self : CondType21
        A CondType21 object

    Returns
    -------
    H: float
        Height of the conductor (with insulation) [m]

    """

    return self.Hbar + 2 * self.Wins
