# -*- coding: utf-8 -*-

from numpy import arcsin, pi

from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the HoleM50 object is correct

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object

    Returns
    -------
    None

    Raises
    _______
    S50_W01CheckError
        You must have W1 < W0
    S50_H23CheckError
        You must have H2 < H3
    S50_H01CheckError
        You must have H1 < H0
    S50_W5CheckError
        You must have W5 >=0
    S50_SpCheckError
        Slot pitch too small for the slot, reduce Zh, W3 or W0
    """
    Rbo = self.get_Rbo()

    if self.W0 <= self.W1:
        raise S50_W01CheckError("You must have W1 < W0")

    if self.H3 <= self.H2:
        raise S50_H23CheckError("You must have H2 < H3")

    if self.H0 <= self.H1:
        raise S50_H01CheckError("You must have H1 < H0")

    if self.comp_W5() < 0:
        raise S50_W5CheckError("You must have W5 >=0")

    alpha_0 = 2 * arcsin(self.W0 / (2 * (Rbo - self.H1)))  # W0 in rad
    alpha_3 = 2 * arcsin(self.W3 / (2 * (Rbo - self.H1)))  # W3 in rad
    if alpha_0 + alpha_3 > 2 * pi / self.Zh:
        raise S50_SpCheckError("Slot pitch too small for the slot, reduce Zh, W3 or W0")


class S50_W01CheckError(SlotCheckError):
    """ """

    pass


class S50_H23CheckError(SlotCheckError):
    """ """

    pass


class S50_H01CheckError(SlotCheckError):
    """ """

    pass


class S50_W5CheckError(SlotCheckError):
    """ """

    pass


class S50_SpCheckError(SlotCheckError):
    """ """

    pass
