# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot.check import SlotCheckError
from numpy import pi


def check(self):
    """Check that the HoleM51 object is correct

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    None
    """

    Rbo = self.get_Rbo()
    alpha = self.comp_alpha()

    if self.W0 < (self.W2 + self.W3):
        raise S51_WCheckError("You must have W2+W3 < W0")

    if Rbo < self.H0 + self.H2:
        raise S51_RHCheckError("You must have H0+H2 < Rbo")

    if alpha > pi / 2:
        raise S51_AlphaCheckError("You must have alpha < pi/2")


class S51_WCheckError(SlotCheckError):
    """ """

    pass


class S51_RHCheckError(SlotCheckError):
    """ """

    pass


class S51_AlphaCheckError(SlotCheckError):
    """ """

    pass
