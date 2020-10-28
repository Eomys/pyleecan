# -*- coding: utf-8 -*-

from numpy import sin, arctan


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    Rbo = self.get_Rbo()

    # make sure W0 is in [m]
    W0 = self.comp_W0m()

    if self.is_outwards():
        # R2 is the slot limit radius at the bottom of the slot
        R2 = W0 / (2 * sin(arctan(W0 / (2 * (Rbo + self.H1 + self.H0)))))
        return R2 - Rbo
    else:
        R2 = W0 / (2 * sin(arctan(W0 / (2 * (Rbo - self.H1 - self.H0)))))
        return Rbo - R2
