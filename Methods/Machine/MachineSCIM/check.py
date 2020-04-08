# -*- coding: utf-8 -*-

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Methods.Machine import MachineCheckError


def check(self):
    """Check that the Machine object is correct

    Parameters
    ----------
    self : MachineSCIM
        A MachineSCIM object

    Returns
    -------
    None

    Raises
    _______
    M1C_WrongRotor
        The Rotor of a MachineSCIM must be a LamSquirrelCage
    M1C_WrongStator
        The Stator of a MachineSCIM must be a LamSlotWind
    M1C_SquirrelCagePError
        The stator and the rotor winding must have the same value for p
    M1C_RingTooLarge
        The Ring is larger than the stator internal radius
    """
    # Call Machine check, skip MachineDFIM check
    self.__class__.__bases__[0].__bases__[0].check(self)

    if not isinstance(self.rotor, LamSquirrelCage):
        raise M1C_WrongRotor("The Rotor of a MachineSCIM must be a " "LamSquirrelCage")
    if not isinstance(self.stator, LamSlotWind):
        raise M1C_WrongStator("The Stator of a MachineSCIM must be a " "LamSlotWind")
    if self.rotor.winding.p != self.stator.winding.p:
        raise M1C_SquirrelCagePError(
            "The stator and the rotor winding must " "have the same value for p"
        )
    if self.rotor.is_internal and (
        self.rotor.slot.comp_radius_mid_wind() + self.rotor.Hscr / 2.0
        > self.stator.Rint
    ):
        raise M1C_RingTooLarge("The Ring is larger than the stator internal " "radius")


class M1C_WrongRotor(MachineCheckError):
    """ """

    pass


class M1C_WrongStator(MachineCheckError):
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


class M1C_SquirrelCagePError(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    winding
        have a different p value as the rotor one

    """

    pass


class M1C_RingTooLarge(MachineCheckError):
    """ """

    pass
