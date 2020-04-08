# -*- coding: utf-8 -*-

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Methods.Machine import MachineCheckError


def check(self):
    """Check that the Machine object is correct

    Parameters
    ----------
    self : MachineSyRM
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

    if not isinstance(self.rotor, LamHole):
        raise MSy_WrongRotor("The Rotor of a MachineSyRM must be a " "LamHole")
    if not isinstance(self.stator, LamSlotWind):
        raise MSy_WrongStator("The Stator of a MachineSyRM must be a " "LamSlotWind")

    if self.rotor.get_pole_pair_number() != self.stator.get_pole_pair_number():
        raise MSy_PError("The stator and the rotor must have the same " "value for p")


class MSy_WrongRotor(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    with
        Magnet

    """

    pass


class MSy_WrongStator(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    with
        Winding

    """

    pass


class MSy_PError(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    values
        

    """

    pass
