# -*- coding: utf-8 -*-

from numpy import arcsin, pi

from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the HoleM58 object is correct

    Parameters
    ----------
    self : HoleM58
        A HoleM58 object

    Returns
    -------
    None

    Raises
    _______
    S58_WCheckError
        You must have W1+W2 <= W0
    """
    Rbo = self.get_Rbo()

    if self.W0 < self.W1 + self.W2:
        raise S58_WCheckError("You must have W1+W2 <= W0")


class S58_WCheckError(SlotCheckError):
    """ """

    pass
