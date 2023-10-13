# -*- coding: utf-8 -*-

from ....Classes.LamSlotM import LamSlotM
from ....Classes.LamSlotWind import LamSlotWind
from ....Methods.Machine import MachineCheckError


def check(self):
    """Check that the Machine object is correct

    Parameters
    ----------
    self : MachineSIPMSM
        A MachineSIPMSM object

    Returns
    -------
    None

    Raises
    _______
    M2C_WrongRotor
        The Rotor of a Machine_Type_2 must be a LamSlotM
    M2C_WrongStator
        The Stator of a Machine_Type_2 must be a LamSlotWind
    M2C_PError
        The stator and the rotor must have the same value for p
    M2C_MagnetTooLarge
        The airgap is too small for the magnet
    """

    super(type(self), self).check()

    if not isinstance(self.rotor, LamSlotM):
        raise M2C_WrongRotor("The Rotor of a Machine_Type_2 must be a " "LamSlotM")
    if not isinstance(self.stator, LamSlotWind):
        raise M2C_WrongStator("The Stator of a Machine_Type_2 must be a " "LamSlotWind")

    if self.rotor.get_pole_pair_number() != self.stator.get_pole_pair_number():
        raise M2C_PError("The stator and the rotor must have the same value " "for p")

    if self.rotor.is_internal and (
        self.rotor.w_slot.comp_radius_mid_active(self.rotor.Rext)
        + self.rotor.Hscr / 2.0
        > self.stator.Rint
    ):
        raise M2C_MagnetTooLarge("The airgap is too small for the magnet")


class M2C_WrongRotor(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    Magnet


    """

    pass


class M2C_WrongStator(MachineCheckError):
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


class M2C_PError(MachineCheckError):
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


class M2C_MagnetTooLarge(MachineCheckError):
    """ """

    pass
