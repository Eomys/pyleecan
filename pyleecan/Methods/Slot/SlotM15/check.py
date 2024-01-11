# -*- coding: utf-8 -*-

from numpy import sin, cos

from ....Methods.Slot.Slot import SlotCheckError


def check(self):
    """Check that the SlotM13 object is correct

    Parameters
    ----------
    self : SlotM15
        A SlotM15 object

    Returns
    -------
    None
    """
    Rbo = self.get_Rbo()

    # conversion W0 rad -> m
    W0_m = 2 * (Rbo - self.H0) * sin(self.W0 / 2)

    if W0_m < self.W1:
        raise SlotCheckError("You must have W1 <= W0")
    if 2 * self.Rtopm < self.W1:
        raise SlotCheckError("You must have W1 <= 2*Rtopm")
