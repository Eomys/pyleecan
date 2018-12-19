# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlot.check
Check that the Lamination is correct
@date Created on Thu Jan 22 17:30:32 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
@todo Check that the Slot don't colide (use width tooth)
"""

from pyleecan.Methods.Machine.Lamination.check import LaminationCheckError


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

    Wt = self.slot.comp_tooth_widths()["WTooth_min"]

    if Wt < 0:
        raise LSC_OverlappingSlot("The Lamination has overlapping slot")


class Lam_SlotCheckError(LaminationCheckError):
    """ """

    pass


class LSC_OutSlotInLam(Lam_SlotCheckError):
    """ """

    pass


class LSC_InSlotOutLam(Lam_SlotCheckError):
    """ """

    pass


class LSC_SlotTooLong(Lam_SlotCheckError):
    """ """

    pass


class LSC_OverlappingSlot(Lam_SlotCheckError):
    """ """

    pass
