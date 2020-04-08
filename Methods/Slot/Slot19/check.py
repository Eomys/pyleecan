# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the Slot19 object is correct

    Parameters
    ----------
    self : Slot19
        A Slot19 object

    Returns
    -------
    None

    Raises
    -------
    S19_H2CheckError
        H1 must be > 0

    S19_W1CheckError
        W1 must be > 0
    """
    if self.W1 < 0:
        raise S19_W1CheckError("W1 must be larger than zero")


class S19_H2CheckError(SlotCheckError):
    """ """

    pass


class S19_W1CheckError(SlotCheckError):
    """ """

    pass
