# -*- coding: utf-8 -*-

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

    """
    Wt = self.slot.comp_tooth_widths()["WTooth_min"]

    if Wt < 0:
        raise LSC_OverlappingSlot("The Lamination has overlapping slot")
    """


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
