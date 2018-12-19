# -*- coding: utf-8 -*-
"""@package Methods.Machine.Machine_Type_3.check
Check that the machine is correct
@date Created on Mon Jan 18 09:41:54 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Methods.Machine import MachineCheckError


def check(self):
    """Check that the Machine object is correct

    Parameters
    ----------
    self : MachineIPMSM
        A MachineIPMSM object

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
        raise M3C_WrongRotor("The Rotor of a Machine_Type_3 must be a " "LamHole")
    if not isinstance(self.stator, LamSlotWind):
        raise M3C_WrongStator("The Stator of a Machine_Type_3 must be a " "LamSlotWind")

    if self.rotor.get_pole_pair_number() != self.stator.get_pole_pair_number():
        raise M3C_PError("The stator and the rotor must have the same " "value for p")


class M3C_WrongRotor(MachineCheckError):
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


class M3C_WrongStator(MachineCheckError):
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


class M3C_PError(MachineCheckError):
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
