# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError


def check(self):
    """Check that the SlotM12 object is correct

    Parameters
    ----------
    self : SlotM12
        A SlotM12 object

    Returns
    -------
    None
    """
    if self.W0 < self.W1:
        raise SlotCheckError("You must have W1 <= W0")
