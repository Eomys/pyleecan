# -*- coding: utf-8 -*-

from ....Methods.Slot.SlotW30 import S30_W0Error
from ....Methods.Slot.SlotW30 import S30_W3Error


def check(self):
    """Check that the SlotW30 object is correct

    Parameters
    ----------
    self : SlotW30
        A SlotW30 object

    Returns
    -------
    None

    Raises
    -------
    S30_W0Error
        S
    """
    Rbo = self.get_Rbo()

    if self.W0 * 0.5 / Rbo >= 1:
        raise S30_W0Error("You must have W0/2 < Rbo")

    if self.is_outwards():
        R1 = Rbo + self.H0 + self.R1
    else:
        R1 = Rbo - self.H0 - self.R1

    if self.W3 * 0.5 / R1 >= 1:
        raise S30_W3Error(
            "W3 is too high comparing to the lamination bore radius (Rbo)"
        )
