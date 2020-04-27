# -*- coding: utf-8 -*-

from numpy import sin

from ....Classes.MagnetType10 import MagnetType10
from ....Classes.MagnetType11 import MagnetType11
from ....Classes.MagnetType13 import MagnetType13
from ....Classes.SlotMFlat import SlotMFlat
from ....Classes.SlotMPolar import SlotMPolar
from ....Classes.SlotMFlat import SlotMFlat
from ....Classes.SlotMPolar import SlotMPolar
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
    LMC_OverlappingSlot
        The Lamination has overlapping slot
    LMC_MagnetShape
        You can't put a rounded bottom magnet in a flat bottom slot
    LMC_MagnetTooLarge
        The magnet is larger than the slot
    LMC_MagnetShape
        You can't put a flat bottom magnet in a rounded bottom slot
    """
    super(type(self), self).check()

    self.slot.check()

    if self.comp_height_yoke() < 0:
        raise LMC_SlotTooLong("The Slot is too long for the lamination " "(HYoke <0)")

    """
    Wt = self.slot.comp_tooth_widths()["WTooth_min"]

    if Wt < 0:
        raise LMC_OverlappingSlot("The Lamination has overlapping slot")
    """

    # Magnet check
    if isinstance(self.slot, SlotMFlat):
        if isinstance(self.magnet, MagnetType11):
            raise LMC_MagnetShape(
                "You can't put a rounded bottom magnet in " "a flat bottom slot"
            )
        if self.slot.W0_unit:  # W0 in rad
            W0 = self.Rext * sin(self.slot.W0) * 2
        else:  # W0 in [m]
            W0 = self.slot.W0
        if self.magnet.Wmag > W0:
            raise LMC_MagnetTooLarge("The magnet is larger than the slot")
    elif type(self.slot) in [SlotMPolar, SlotMPolar]:
        if type(self.magnet) in [MagnetType10, MagnetType13]:
            raise LMC_MagnetShape(
                "You can't put a flat bottom magnet in a " "rounded bottom slot"
            )
        if self.magnet.Wmag > self.slot.W0:
            raise LMC_MagnetTooLarge("The magnet is larger than the slot")
    elif isinstance(self.slot, SlotMFlat):
        if isinstance(self.magnet, MagnetType11):
            raise LMC_MagnetShape(
                "You can't put a rounded bottom magnet in " "a flat bottom slot"
            )
        if self.magnet.Wmag > self.slot.W0:
            raise LMC_MagnetTooLarge("The magnet is larger than the slot")
    else:  # Only is a new slot_mag type is added
        raise TypeError("Unknow Slot type")


class Lam_MagCheckError(LaminationCheckError):
    """ """

    pass


class LMC_OutSlotInLam(Lam_MagCheckError):
    """ """

    pass


class LMC_InSlotOutLam(Lam_MagCheckError):
    """ """

    pass


class LMC_SlotTooLong(Lam_MagCheckError):
    """ """

    pass


class LMC_OverlappingSlot(Lam_MagCheckError):
    """ """

    pass


class LMC_MagnetShape(Lam_MagCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    the
        slot

    """

    pass


class LMC_MagnetTooLarge(Lam_MagCheckError):
    """ """

    pass
