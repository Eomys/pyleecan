from ....Methods.Slot.VentilationCirc import *
from numpy import int32


def check(self):
    """Make sure that the ventilation parameters are correctly set

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object

    Returns
    -------
    None

    Raises
    _______
    VentilationCircInstanceError
        Zh must be an integer
        H0 must be a float ot int
        D0 must be a float or int
        Alpha0 must be a float ot int
    """

    if not isinstance(self.Zh, (int, int32)):
        raise VentilationCircInstanceError("Zh must be an integer")
    if not isinstance(self.H0, (float, int)):
        raise VentilationCircInstanceError("H0 must be a float ot int ")
    if not isinstance(self.D0, (float, int)):
        raise VentilationCircInstanceError("D0 must be a float or int ")
    if not isinstance(self.Alpha0, (float, int)):
        raise VentilationCircInstanceError("Alpha0 must be a float ot int")
