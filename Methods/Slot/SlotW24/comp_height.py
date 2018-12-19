# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW24.comp_height
SlotW24 Computation of height method
@date Created on Mon Jul 06 11:40:07 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    return self.H2
