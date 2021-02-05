# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW27 import *


def check(self):
    """Check that the SlotW27 object is correct

    Parameters
    ----------
    self : SlotW27
        A SlotW27 object

    Returns
    -------
    None

    Raises
    -------
    S27_W01CheckError
        You must have W0 <= W1
    S27_W12CheckError
        You must have W1 <= W2
    S27_W03CheckError
        You must have W0 <= W3

    """
    if self.W1 < self.W0:
        raise S27_W01CheckError("You must have W0 <= W1")

    if self.W2 < self.W1:
        raise S27_W12CheckError("You must have W1 <= W2")

    if self.W3 < self.W0:
        raise S27_W03CheckError("You must have W0 <= W3")
