# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW21 import *


def check(self):
    """Check that the SlotW21 object is correct

    Parameters
    ----------
    self : SlotW21
        A SlotW21 object

    Returns
    -------
    None

    Raises
    -------
    S21_W01CheckError
        You must have W0 <= W1
    S21_H1rCheckError
        With H1 in radian, you must have H1 < pi/2
    """
    if self.W1 < self.W0:
        raise S21_W01CheckError("You must have W0 <= W1")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S21_H1rCheckError("With H1 in radian, you must have H1 < pi/2")
