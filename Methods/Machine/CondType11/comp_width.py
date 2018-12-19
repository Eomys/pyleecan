# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType11.comp_width
Conductor Type 1_1 width computation method
@date Created on Tue Jan 20 15:24:57 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_width(self):
    """Compute the width of the conductor

    Parameters
    ----------
    self : CondType11
        A CondType11 object

    Returns
    -------
    W: float
        Width of the conductor [m]

    """

    return (2 * self.Wins_wire + self.Wwire) * self.Nwppc_tan
