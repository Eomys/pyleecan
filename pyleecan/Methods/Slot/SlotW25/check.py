# -*- coding: utf-8 -*-

from numpy import arcsin, pi

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW25 import *


def check(self):
    """Check that the SlotW25 object is correct

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    None

    Raises
    -------
    S25_W4CheckError
        The teeth are too wide, reduce Zs or W4
    S25_HWCheckError
        The teeth are too wide, reduce Zs, H2 or W3

    """
    Rbo = self.get_Rbo()

    if 2 * arcsin(self.W4 / (2 * Rbo)) > 2 * pi / self.Zs:
        raise S25_W4CheckError("The teeth are too wide, reduce Zs or W4")

    if (
        not self.is_outwards()
        and 2 * arcsin(self.W3 / (2 * Rbo - self.H2 - self.H1)) > 2 * pi / self.Zs
    ):
        raise S25_HWCheckError("The teeth are too wide, reduce Zs, H2 or W3")
