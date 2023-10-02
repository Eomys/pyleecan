# -*- coding: utf-8 -*-

from ....Methods.Machine.LamSlotMag import LMC_SlotTooLong


def check(self):
    """Check that the Lamination object is correct

    Parameters
    ----------
    self : LamSlotMagNS
        A LamSlotMagNS object

    Returns
    -------
    None

    Raises
    _______
    LMC_SlotTooLong
        The Slot is too long for the lamination (HYoke <0)
    """
    super(type(self), self).check()

    self.slot.check()
    self.slot_south.check()

    if self.comp_height_yoke() < 0:
        raise LMC_SlotTooLong("The Slot is too long for the lamination " "(HYoke <0)")
