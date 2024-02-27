# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW11 import *


def check(self):
    """Check that the SlotW11 object is correct

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    None

    Raises
    -------
    S11_W01CheckError
        You must have W0 <= W1
    S11_RWCheckError
        You must have 2*R1 <= W2
    S11_RHCheckError
        You must have R1 <= H2
    S11_H1rCheckError
        With H1 in radian, you must have H1 < pi/2"""

    if self.W0 is None:
        return "You must set W0 !"
    if self.W1 is None and not self.is_cstt_tooth:
        return "You must set W1 !"
    if self.W2 is None and not self.is_cstt_tooth:
        return "You must set W2 !"
    elif self.H0 is None:
        return "You must set H0 !"
    elif self.H1 is None:
        return "You must set H1 !"
    elif self.H2 is None:
        return "You must set H2 !"
    elif self.R1 is None:
        return "You must set R1 !"
    elif self.is_cstt_tooth and self.W3 is None:
        return "In constant tooth mode, you must set W3 !"

    if self.R1 <= 0:
        raise S11_R1CheckError("You must have R1 > 0")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S11_H1rCheckError("With H1 in radian, you must have H1 < pi/2")
        # return "With H1 in radian, you must have H1 < pi/2"

    if self.W1 is None or self.W0 is None:
        pass
    else:
        if self.W1 < self.W0:
            raise S11_W01CheckError("You must have W0 <= W1")

    if not self.W1 is None or not self.W2 is None:
        if 2 * self.R1 > self.W2 and (not self.W2 is None or not self.R1 is None):
            raise S11_RWCheckError("You must have 2*R1 <= W2")

    if self.R1 > self.H2:
        raise S11_RHCheckError("You must have R1 <= H2")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S11_H1rCheckError("With H1 in radian, you must have H1 < pi/2")
