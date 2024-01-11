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
        You must have W0 <= W1

    S29_W12CheckError
        You must have W1 <= W2

    S29_H2CheckError
        You must have H2 > 0

    """
    if self.W1 < self.W0:
        raise S29_W01CheckError("You must have W0 <= W1")

    elif self.H2 == 0:
        raise S29_H2CheckError("You must have H2 > 0")
