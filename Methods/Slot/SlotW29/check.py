# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW29.check
Check that the SlotW29 is correct
@date Created on Thu Feb 23 10:36:36 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW29 object is correct

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object

    Returns
    -------
    None

    Raises
    -------
    S29_W01CheckError
        You must have W0 < W1
    S29_W12CheckError
        You must have W1 < W2

    """
    if self.W1 <= self.W0:
        raise S29_W01CheckError("You must have W0 < W1")

    if self.W2 <= self.W1:
        raise S29_W12CheckError("You must have W1 < W2")


class S29_W01CheckError(SlotCheckError):
    """ """

    pass


class S29_W12CheckError(SlotCheckError):
    """ """

    pass
