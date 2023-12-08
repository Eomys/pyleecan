# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW62 import *


def check(self):
    """Check that the SlotW62 object is correct

    Parameters
    ----------
    self : SlotW62
        A SlotW62 object

    Returns
    -------
    None
    Raises
    -------
    S62_InnerCheckError
        Slot 62 is for inner lamination only

    """
    if self.is_outwards():
        raise S62_InnerCheckError("Slot 62 is for inner lamination only")

    if self.H3 + self.H2 >= self.H0:
        raise S62_WindHError("You must have H3+H2 < H0")
