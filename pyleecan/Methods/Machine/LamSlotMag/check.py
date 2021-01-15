# -*- coding: utf-8 -*-

from ....Methods.Machine.Lamination.check import LaminationCheckError


def check(self):
    """Check that the Lamination object is correct

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

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

    if self.comp_height_yoke() < 0:
        raise LMC_SlotTooLong("The Slot is too long for the lamination " "(HYoke <0)")


class LMC_SlotTooLong(LaminationCheckError):
    """ """

    pass
