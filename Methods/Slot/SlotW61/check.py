# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW61 object is correct

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object

    Returns
    -------
    None
    Raises
    -------
    S61_InnerCheckError
       Slot 61 is for inner lamination only
    S61_W21CheckError
        You must have W2 < W1
    S61_WindHError
        You must have W3+W4 < H2
    S61_WindWError
        You must have W3 < (W1-W2)/2
    """

    if self.is_outwards():
        raise S61_InnerCheckError("Slot 61 is for inner lamination only")

    if self.W1 <= self.W2:
        raise S61_W21CheckError("You must have W2 < W1")

    if self.H3 + self.H4 >= self.H2:
        raise S61_WindHError("You must have W3+W4 < H2")

    if self.W3 >= (self.W1 - self.W2) / 2:
        raise S61_WindWError("You must have W3 < (W1-W2)/2")


class S61_InnerCheckError(SlotCheckError):
    """ """

    pass


class S61_W21CheckError(SlotCheckError):
    """ """

    pass


class S61_RCheckError(SlotCheckError):
    """ """

    pass


class S61_WindHError(SlotCheckError):
    """ """

    pass


class S61_WindWError(SlotCheckError):
    """ """

    pass
