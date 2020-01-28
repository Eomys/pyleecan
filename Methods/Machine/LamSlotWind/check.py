# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotWind.check
Check that the Lamination is correct
@date Created on Thu Jan 22 16:47:24 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
@todo check winding
@todo check tooth widths
"""

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Methods.Machine.Lamination.check import LaminationCheckError


def check(self):
    """Check that the Lamination object is correct

    Parameters
    ----------
    self :
        A LamSlotWind object

    Returns
    -------
    None

    Raises
    _______
    LWC_SlotTooLong
        The Slot is too long for the lamination (HYoke <0)
    LWC_MismatchPhase
        The Winding and the Converter don't have the same number of phase
    LWC_OverlappingSlot
        The Lamination has overlapping slot
    """

    Lamination.check(self)

    self.winding.conductor.check()
    self.slot.check()

    if self.comp_height_yoke() < 0:
        raise LWC_SlotTooLong("The Slot is too long for the lamination " "(HYoke <0)")

    """
    Wt = self.slot.comp_tooth_widths()["WTooth_min"]

    if Wt < 0:
        raise LWC_OverlappingSlot("The Lamination has overlapping slot")
    """


class Lam_WindCheckError(LaminationCheckError):
    """ """

    pass


class LWC_OutSlotInLam(Lam_WindCheckError):
    """ """

    pass


class LWC_InSlotOutLam(Lam_WindCheckError):
    """ """

    pass


class LWC_SlotTooLong(Lam_WindCheckError):
    """ """

    pass


class LWC_OverlappingSlot(Lam_WindCheckError):
    """ """

    pass
