# -*- coding: utf-8 -*-

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW60 object is correct

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

    Returns
    -------
    None

    Raises
    -------
    S60_InnerCheckError
       Slot 60 is for inner lamination only
    S60_W21CheckError
        You must have W2 < W1
    S60_RCheckError
        You must have R1 <= Rbo
    S60_WindHError
        You must have W3+W4 < H2
    S60_WindWError
        You must have W3 < (W1-W2)/2

    """

    if self.is_outwards():
        raise S60_InnerCheckError("Slot 60 is for inner lamination only")

    if self.W1 <= self.W2:
        raise S60_W21CheckError("You must have W2 < W1")

    if self.R1 > self.get_Rbo():
        raise S60_RCheckError("You must have R1 <= Rbo")

    if self.H3 + self.H4 >= self.H2:
        raise S60_WindHError("You must have W3+W4 < H2")

    if self.W3 >= (self.W1 - self.W2) / 2:
        raise S60_WindWError("You must have W3 < (W1-W2)/2")


class S60_InnerCheckError(SlotCheckError):
    """ """

    pass


class S60_W21CheckError(SlotCheckError):
    """ """

    pass


class S60_RCheckError(SlotCheckError):
    """ """

    pass


class S60_WindHError(SlotCheckError):
    """ """

    pass


class S60_WindWError(SlotCheckError):
    """ """

    pass
