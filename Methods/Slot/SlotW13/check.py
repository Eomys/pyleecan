# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW13.check
Check that the SlotW13 is correct
@date Created on Mon Jul 11 13:48:02 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import pi

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW13 object is correct

    Parameters
    ----------
    self : SlotW13
        A SlotW13 object

    Returns
    -------
    None

    Raises
    -------
    S13_W01CheckError
        You must have W0 <= W1
    S13_W12CheckError
        You must have W2 <= W1
    S13_H1rCheckError
        With H1 in radian, you must have H1 < pi/2
    """
    if self.W1 < self.W0:
        raise S13_W01CheckError("You must have W0 <= W1")

    if self.W1 < self.W2:
        raise S13_W12CheckError("You must have W2 <= W1")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S13_H1rCheckError("With H1 in radian, you must have H1 < pi/2")


class S13_W01CheckError(SlotCheckError):
    """ """

    pass


class S13_W12CheckError(SlotCheckError):
    """ """

    pass


class S13_H1rCheckError(SlotCheckError):
    """ """

    pass
