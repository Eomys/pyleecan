# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW14 import *


def check(self):
    """Check that the SlotW14 object is correct

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    None

    Raises
    -------
    S14_Rbo0CheckError
        You must have W0/2 < Rbo
    S14_Rbo1CheckError
        W3 is too high comparing to the lamination bore radius (Rbo)
    """

    Rbo = self.get_Rbo()
    H1 = self.get_H1()

    if self.W0 * 0.5 / Rbo >= 1:
        raise S14_Rbo0CheckError("You must have W0/2 < Rbo")

    if self.is_outwards():
        R1 = Rbo + self.H0 + H1
    else:
        R1 = Rbo - self.H0 - H1

    if self.W3 * 0.5 / R1 >= 1:
        raise S14_Rbo1CheckError(
            "W3 is too high comparing to the lamination bore radius (Rbo)"
        )
