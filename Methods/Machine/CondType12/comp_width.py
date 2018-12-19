# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType12.comp_width
Conductor Type 1_2 width computation method
@date Created on Tue Jan 20 12:19:17 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_width(self):
    """Compute the width of the conductor

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    W: float
        Width of the conductor [m]

    """

    return self.Wins_cond
