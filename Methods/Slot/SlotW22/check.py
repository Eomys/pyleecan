# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW22.check
Check that the SlotW22 is correct
@date Created on Wed Feb 04 13:01:47 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW22 object is correct

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    None

    Raises
    -------
    S22_A02CheckError
        You must have W0 <= W2
    S22_SpCheckError
        You must have W2 < 2*pi/Zs
    """
    if self.W2 < self.W0:
        raise S22_A02CheckError("You must have W0 <= W2")

    if 2 * pi / self.Zs <= self.W2:
        raise S22_SpCheckError("You must have W2 < 2*pi/Zs")


class S22_A02CheckError(SlotCheckError):
    """ """

    pass


class S22_SpCheckError(SlotCheckError):
    """ """

    pass
