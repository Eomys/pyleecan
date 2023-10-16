# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError


def check(self):
    """Check that the SlotM11 object is correct

    Parameters
    ----------
    self : SlotM14
        A SlotM14 object

    Returns
    -------
    None
    """
    if self.W0 < self.W1:
        raise SlotCheckError("You must have W1 <= W0")
