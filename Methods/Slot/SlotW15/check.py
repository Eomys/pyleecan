# -*- coding: utf-8 -*-
"""@package

@date Created on Mon Nov 27 12:19:16 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from pyleecan.Methods.Slot.SlotW15 import S15InnerError


def check(self):
    """Check that the SlotW15 object is correct

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    None

    Raises
    -------
    S15InnerError
        Slot Type 15 can't be used on inner lamination
    """

    if not self.is_outwards():
        raise S15InnerError("Slot Type 15 can't be used on inner lamination")
