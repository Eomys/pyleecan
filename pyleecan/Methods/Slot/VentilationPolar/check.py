# -*- coding: utf-8 -*-


def check(self):
    """Make sure that the ventilation parameters are correctly set

    Parameters
    ----------
    self : VentilationPolar
        A VentilationPolar object

    Returns
    -------
    None

    Raises
    _______
    VentilationPolarInstanceError
        Zh must be a integer
        H0 must be a float or int
        D0 must be a float or int
        Alpha0 must be a float or int
    """

    if not isinstance(self.Zh, int):
        raise VentilationPolarInstanceError("Zh must be a integer")
    if not isinstance(self.H0, float) and not isinstance(self.H0, int):
        raise VentilationPolarInstanceError("H0 must be a float or int")
    if not isinstance(self.D0, float) and not isinstance(self.D0, int):
        raise VentilationPolarInstanceError("D0 must be a float or int")
    if not isinstance(self.Alpha0, float) and not isinstance(self.Alpha0, int):
        raise VentilationPolarInstanceError("Alpha0 must be a float or int")


class VentilationPolarInstanceError(Exception):
    """ """

    pass
