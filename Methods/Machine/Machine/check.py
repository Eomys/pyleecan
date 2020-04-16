# -*- coding: utf-8 -*-

from ....Methods.Machine import MachineCheckError


def check(self):
    """Check that the Machine object is correct

    Parameters
    ----------
    self :
        A Machine object

    Returns
    -------
    None

    Raises
    _______
    MC_AbstractError
        Machine is an abstract class
    MC_StatorNotStator
        self.stator.is_stator must be True
    MC_RotorIsStator
        self.rotor.is_stator must be False
    MC_BothInternal
        self.rotor.is_internal and self.rotor.is_internal can't be both True
    MC_BothExternal
        self.rotor.is_internal and self.rotor.is_internal can't be both False
    MC_RotorDontFit
        The Rotor is too big to fit in the Stator
    MC_ShaftTooBig
        The Shaft is too big to fit in the Rotor
    MC_ShaftTooSmall
        The Shaft is too small to fit in the Rotor
    MC_MecAirgapError
        The Stator and the rotor don't fit because of magnet or short circuit ring
    """

    if type(self).__name__ == "Machine":
        raise MC_AbstractError("Machine is an abstract class")

    if not self.stator.is_stator:
        raise MC_StatorNotStator("self.stator.is_stator must be True")

    if self.rotor.is_stator:
        raise MC_RotorIsStator("self.rotor.is_stator must be False")

    if self.rotor.is_internal and self.stator.is_internal:
        raise MC_BothInternal(
            "self.rotor.is_internal and " "self.rotor.is_internal can't be both True"
        )

    if (not self.rotor.is_internal) and (not self.stator.is_internal):
        raise MC_BothExternal(
            "self.rotor.is_internal and " "self.rotor.is_internal can't be both False"
        )

    if self.rotor.is_internal:
        if self.rotor.Rext > self.stator.Rint:
            raise MC_RotorDontFit("The Rotor is too big to fit in the Stator")
        if self.shaft.Drsh / 2.0 > self.rotor.Rint:
            raise MC_ShaftTooBig("The Shaft is too big to fit in the Rotor")
        if self.shaft.Drsh / 2.0 < self.rotor.Rint:
            raise MC_ShaftTooSmall("The Shaft is too small to fit in the " "Rotor")
    else:
        if self.stator.Rext > self.rotor.Rint:
            raise MC_StatorDontFit("The Stator is too big to fit in the Rotor")

    if self.comp_width_airgap_mec() <= 0:
        raise MC_MecAirgapError(
            "The Stator and the rotor don't fit because "
            "of magnet or short circuit ring"
        )

    self.rotor.check()
    self.stator.check()


class MC_AbstractError(MachineCheckError):
    """ """

    pass


class MC_StatorNotStator(MachineCheckError):
    """ """

    pass


class MC_RotorIsStator(MachineCheckError):
    """ """

    pass


class MC_BothInternal(MachineCheckError):
    """ """

    pass


class MC_BothExternal(MachineCheckError):
    """ """

    pass


class MC_RotorDontFit(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    stator
        

    """

    pass


class MC_StatorDontFit(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    rotor
        

    """

    pass


class MC_ShaftTooBig(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    rotor
        

    """

    pass


class MC_ShaftTooSmall(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    rotor
        

    """

    pass


class MC_MecAirgapError(MachineCheckError):
    """ """

    pass
