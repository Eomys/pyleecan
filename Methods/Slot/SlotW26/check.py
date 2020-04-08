# -*- coding: utf-8 -*-

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW26 object is correct

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    None

    Raises
    -------
    S26_WCheckError
        You must have W0 < 2*R1
    """
    if self.R1 * 2 <= self.W0:
        raise S26_WCheckError("You must have W0 < 2*R1")


class S26_WCheckError(SlotCheckError):
    """ """

    pass
