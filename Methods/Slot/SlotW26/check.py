# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW26.check
Check that the SlotW26 is correct
@date Created on Mon Feb 22 11:48:55 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW26 object is correct

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    None

    Raises
    -------
    S26_WCheckError
        You must have W0 < 2*R1
    """
    if self.R1 * 2 <= self.W0:
        raise S26_WCheckError("You must have W0 < 2*R1")


class S26_WCheckError(SlotCheckError):
    """ """

    pass
