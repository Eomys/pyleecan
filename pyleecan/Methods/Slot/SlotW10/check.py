# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW10 import *


def check(self):
    """Check that the SlotW10 object is correct

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    None

    Raises
    -------
    S10_W01CheckError
        You must have W0 <= W1
    S10_W02CheckError
        You must have W0 <= W2
    S10_H1rCheckError
        With H1 in radian, you must have H1 < pi/2
    """
    if self.W1 < self.W0:
        raise S10_W01CheckError("You must have W0 <= W1")

    if self.W2 < self.W0:
        raise S10_W02CheckError("You must have W0 <= W2")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S10_H1rCheckError("With H1 in radian, you must have H1 < pi/2")
