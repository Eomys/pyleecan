# -*- coding: utf-8 -*-

from ....Classes.LamHole import LamHole
from ....Classes.LamSlotWind import LamSlotWind
from ....Methods.Machine import MachineCheckError


def check(self):
    """Check that the Machine object is correct

    Parameters
    ----------
    self : MachineLSPM
        The machine object to check

    Returns
    -------
    None


    Raises
    _______
    M3C_WrongRotor
        The Rotor of a Machine_Type_3 must be a LamHole
    M3C_WrongStator
        The Stator of a Machine_Type_3 must be a LamSlotWind
    M3C_PError
        The stator and the rotor must have the same value for p

    """

    super(type(self), self).check()

    if self.rotor.get_pole_pair_number() != self.stator.get_pole_pair_number():
        raise MachineCheckError(
            "The stator and the rotor must have the same value for p"
        )
