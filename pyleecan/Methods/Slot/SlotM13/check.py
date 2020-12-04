# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot.check import SlotCheckError


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
    if self.W0 < self.Wmag:
        raise SlotCheckError("You must have Wmag <= W0")
    if 2 * self.Rtopm < self.Wmag:
        raise SlotCheckError("You must have Wmag <= 2*Rtopm")
