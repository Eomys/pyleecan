# -*- coding: utf-8 -*-

from ....Methods.Slot.SlotW63 import *


def check(self):
    """Check that the SlotW63 object is correct

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object

    Returns
    -------
    None
    Raises
    -------
    S63_InnerCheckError
        Slot 63 is for inner lamination only

    """
    if self.is_outwards():
        raise S63_InnerCheckError("Slot 63 is for inner lamination only")

    if self.W0 >= self.W1:
        raise S63_W0CheckError("You must have W1 > W0")

    if self.H0 == 0:
        raise S63_H0CheckError("You must have H0 > 0")

    if self.W0 == 0:
        raise S63_W0CheckError("You must have W0 > 0")
