# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW12 import *


def check(self):
    """Check that the SlotW12 object is correct

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    None

    Raises
    -------
    S12_R20CheckError
        You must have R2 > 0
    S12_RboCheckError
        You must have R2 < Rbo
    """

    Rbo = self.get_Rbo()

    if self.R2 <= 0:
        raise S12_R20CheckError("You must have R2 > 0")

    if self.R2 / Rbo >= 1:
        raise S12_RboCheckError("You must have R2 < Rbo")
