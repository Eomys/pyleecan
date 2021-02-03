# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError


def check(self):
    """Check that the SlotM10 object is correct

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object

    Returns
    -------
    None
    """
    if self.W0 < self.Wmag:
        raise SlotCheckError("You must have Wmag <= W0")
