# -*- coding: utf-8 -*-

from ....Methods.Machine.LamSlot import *


def check(self):
    """Check that the Lamination object is correct

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    None

    Raises
    _______
    LSC_SlotTooLong
        The Slot is too long for the lamination (HYoke <0)

    LSC_OverlappingSlot
        The Lamination has overlapping slot

    """

    super(type(self), self).check()

    self.slot.check()

    if self.comp_height_yoke() < 0:
        raise LSC_SlotTooLong("The Slot is too long for the lamination " "(HYoke <0)")

    """
    Wt = self.slot.comp_tooth_widths()["WTooth_min"]

    if Wt < 0:
        raise LSC_OverlappingSlot("The Lamination has overlapping slot")
    """
