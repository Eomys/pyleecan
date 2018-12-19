# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW22.comp_height
SlotW22 Computation of height method
@date Created on Tue Dec 09 16:12:46 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    return self.H0 + self.H2
