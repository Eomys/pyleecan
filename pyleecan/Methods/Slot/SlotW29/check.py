# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW29 import *


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

    """
    if self.W1 <= self.W0:
        raise S29_W01CheckError("You must have W0 < W1")
