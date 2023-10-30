# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW23 import *


def check(self):
    """Check that the SlotW23 object is correct

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    None

    Raises
    -------
    S23_W01CheckError
        You must have W0 <= W1
    S23_H1rCheckError
        With H1 in radian, you must have H1 < pi/2

    """

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S23_H1rCheckError("With H1 in radian, you must have H1 < pi/2")

    if self.W1 is not None and self.W1 < self.W0:
        raise S23_W01CheckError("You must have W0 <= W1")
