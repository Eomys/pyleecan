# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError


def check(self):
    """Check that the SlotM13 object is correct

    Parameters
    ----------
    self : SlotM13
        A SlotM13 object

    Returns
    -------
    None
    """
    if self.W0 < self.W1:
        raise SlotCheckError("You must have W1 <= W0")
    if 2 * self.Rtopm < self.W1:
        raise SlotCheckError("You must have W1 <= 2*Rtopm")
