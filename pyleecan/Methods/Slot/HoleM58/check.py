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
    # Check that everything is set
    if self.W0 is None:
        raise S58_NoneError("You must set W0 !")
    elif self.W1 is None:
        raise S58_NoneError("You must set W1 !")
    elif self.W2 is None:
        raise S58_NoneError("You must set W2 !")
    elif self.W3 is None:
        raise S58_NoneError("You must set W3 !")
    elif self.R0 is None:
        raise S58_NoneError("You must set R0 !")
    elif self.H0 is None:
        raise S58_NoneError("You must set H0 !")
    elif self.H1 is None:
        raise S58_NoneError("You must set H1 !")
    elif self.H2 is None:
        raise S58_NoneError("You must set H2 !")

    Rbo = self.get_Rbo()

    if self.W0 < self.W1 + self.W2:
        raise S58_WCheckError("You must have W1+W2 <= W0")


class S58_NoneError(SlotCheckError):
    """Raised when a propery of HoleM58 is None"""

    pass


class S58_WCheckError(SlotCheckError):
    """ """

    pass
