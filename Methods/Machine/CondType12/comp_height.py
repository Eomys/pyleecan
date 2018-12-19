# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType12.comp_height
Conductor Type 1_2 height computation method
@date Created on Tue Jan 20 12:19:17 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height(self):
    """Compute the height of the conductor

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    H: float
        Height of the conductor [m]

    """

    return self.Wins_cond
