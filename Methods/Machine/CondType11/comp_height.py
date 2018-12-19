# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType11.comp_height
Conductor Type 1_1 height computation method
@date Created on Tue Jan 20 12:14:57 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height(self):
    """Compute the height of the conductor

    Parameters
    ----------
    self : CondType11
        A CondType11 object

    Returns
    -------
    H: float
        Height of the conductor [m]

    """

    return (2 * self.Wins_wire + self.Hwire) * self.Nwppc_rad
