# -*- coding: utf-8 -*-

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

    if self.H3 + self.H2 > self.H0:
        raise S62_WindHError("You must have H3+H2 < H0")

    if self.W0 == 0:
        raise S62_W0Error("You must have W0 > 0")

    if self.W1 == 0:
        raise S62_W1Error("You must have W1 > 0")

    if self.H1 == 0:
        raise S62_H1Error("You must have H1 > 0")

    if self.W2 == 0:
        raise S62_W2Error("You must have W2 > 0")

    if self.H2 == 0:
        raise S62_H2Error("You must have H2 > 0")
