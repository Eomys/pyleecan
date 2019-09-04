# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot19.check
Check that the Slot19 is correct
@date Created on Mon Jun 29 15:28:55 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the Slot19 object is correct

    Parameters
    ----------
    self : Slot19
        A Slot19 object

    Returns
    -------
    None

    Raises
    -------
    S19_H2CheckError
        H1 must be > 0

    S19_W1CheckError
        W1 must be > 0
    """
    if self.W1 < 0:
        raise S19_W1CheckError("W1 must be larger than zero")


class S19_H2CheckError(SlotCheckError):
    """ """

    pass


class S19_W1CheckError(SlotCheckError):
    """ """

    pass
