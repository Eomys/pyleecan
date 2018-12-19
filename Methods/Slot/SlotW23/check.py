# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW23.check
Check that the SlotW23 is correct
@date Created on Mon Jun 29 15:28:55 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW23 object is correct

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    None

    Raises
    -------
    S23_W01CheckError
        You must have W0 <= W1
    S23_H1rCheckError
        With H1 in radian, you must have H1 < pi/2

    """
    if self.W1 is not None and self.W1 < self.W0:
        raise S23_W01CheckError("You must have W0 <= W1")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S23_H1rCheckError("With H1 in radian, you must have H1 < pi/2")


class S23_W01CheckError(SlotCheckError):
    """ """

    pass


class S23_H1rCheckError(SlotCheckError):
    """ """

    pass
