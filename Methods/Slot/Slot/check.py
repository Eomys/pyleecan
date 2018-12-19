# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot.check
Check that the Slot is correct
@date Created on Wed Feb 04 12:47:19 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Methods.Machine.Lamination.check import LaminationCheckError


def check(self):
    """Check that the Slot object is correct

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    None
    """
    pass


class SlotCheckError(LaminationCheckError):
    """ """

    pass
