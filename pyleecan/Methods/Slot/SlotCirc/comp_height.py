# -*- coding: utf-8 -*-

from numpy import cos, tan


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the top of the Slot is an Arc

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    Htot: float
        Height of the slot [m]
    """

    return self.comp_height_wind()
