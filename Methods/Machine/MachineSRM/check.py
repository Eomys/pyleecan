# -*- coding: utf-8 -*-

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Methods.Machine import MachineCheckError


def check(self):
    """Check that the Machine object is correct

    Parameters
    ----------
    self : MachineSRM
        The machine object to check

    Returns
    -------
    None


    Raises
    _______
    SRM_WrongRotor
        The Rotor of a MachineSRM must be a LamSlot
    SRM_WrongStator
        The Stator of a MachineSRM must be a LamSlotWind

    """

    super(type(self), self).check()

    if not isinstance(self.rotor, LamSlot):
        raise SRM_WrongRotor("The Rotor of a MachineSRM must be a " "LamSlot")
    if not isinstance(self.stator, LamSlotWind):
        raise SRM_WrongStator("The Stator of a MachineSRM must be a " "LamSlotWind")


class SRM_WrongRotor(MachineCheckError):
    pass


class SRM_WrongStator(MachineCheckError):
    pass
