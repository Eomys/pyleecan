# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot19.comp_height
Slot19 Computation of height method
@date Created on Mon Jun 29 15:28:55 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo check and unittest
"""


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : Slot19
        A Slot19 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    return self.H0
