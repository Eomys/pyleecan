# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW13 import *


def check(self):
    """Check that the SlotW13 object is correct

    Parameters
    ----------
    self : SlotW13
        A SlotW13 object

    Returns
    -------
    None

    Raises
    -------
    S13_W01CheckError
        You must have W0 <= W1
    S13_W12CheckError
        You must have W2 <= W1
    S13_H1rCheckError
        With H1 in radian, you must have H1 < pi/2
    """
    if self.W1 < self.W0:
        raise S13_W01CheckError("You must have W0 <= W1")

    if self.W1 < self.W2:
        raise S13_W12CheckError("You must have W2 <= W1")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S13_H1rCheckError("With H1 in radian, you must have H1 < pi/2")
