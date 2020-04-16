# -*- coding: utf-8 -*-


def check(self):
    """Make sure that the ventialtion parameters are correctly set

    Parameters
    ----------
    self : VentilationTrap
        A VentilationTrap object
    """

    if not isinstance(self.Zh, int):
        raise VentilationTrapInstanceError("Zh must be a integer")
    if not isinstance(self.H0, float) and not isinstance(self.H0, int):
        raise VentilationTrapInstanceError("H0 must be a float or int")
    if not isinstance(self.D0, float) and not isinstance(self.D0, int):
        raise VentilationTrapInstanceError("D0 must be a float or int")
    if not isinstance(self.Alpha0, float) and not isinstance(self.Alpha0, int):
        raise VentilationTrapInstanceError("Alpha0 must be a float or int")


class VentilationTrapInstanceError(Exception):
    """Raised when a Ventilation Trap parameter is not int or float"""

    pass
