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

    # Check that everything is set
    if self.W0 is None:
        raise S50_NoneError("You must set W0 !")
    elif self.W1 is None:
        raise S50_NoneError("You must set W1 !")
    elif self.W2 is None:
        raise S50_NoneError("You must set W2 !")
    elif self.W3 is None:
        raise S50_NoneError("You must set W3 !")
    elif self.W4 is None:
        raise S50_NoneError("You must set W4 !")
    elif self.H0 is None:
        raise S50_NoneError("You must set H0 !")
    elif self.H1 is None:
        raise S50_NoneError("You must set H1 !")
    elif self.H2 is None:
        raise S50_NoneError("You must set H2 !")
    elif self.H3 is None:
        raise S50_NoneError("You must set H3 !")
    elif self.H4 is None:
        raise S50_NoneError("You must set H4 !")

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


class S50_NoneError(SlotCheckError):
    """Raised when a propery of HoleM50 is None"""

    pass


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
