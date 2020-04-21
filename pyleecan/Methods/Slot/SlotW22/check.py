# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW22 object is correct

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    None

    Raises
    -------
    S22_A02CheckError
        You must have W0 <= W2
    S22_SpCheckError
        You must have W2 < 2*pi/Zs
    """
    if self.W2 < self.W0:
        raise S22_A02CheckError("You must have W0 <= W2")

    if 2 * pi / self.Zs <= self.W2:
        raise S22_SpCheckError("You must have W2 < 2*pi/Zs")


class S22_A02CheckError(SlotCheckError):
    """ """

    pass


class S22_SpCheckError(SlotCheckError):
    """ """

    pass
