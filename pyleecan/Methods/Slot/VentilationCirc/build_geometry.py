# -*- coding: utf-8 -*-


from ....Classes.Circle import Circle
from numpy import exp, pi
from ....Methods.Slot.VentilationCirc import *
from ....Functions.labels import VENT_LAB


def build_geometry(self, alpha=0, delta=0):
    """Compute the curve needed to plot the ventilations

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : complex
        Complex for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        A list of Circle

    """
    lam_label = self.parent.get_label()
    R_id, surf_type = self.get_R_id()
    RTS_id = "R" + str(R_id) + "-T0-S0"
    vent_label = lam_label + "_" + surf_type + "_" + RTS_id

    # checking if the param have good type
    if type(alpha) not in [int, float]:
        raise CircleBuildGeometryError("The parameter 'alpha' must be an int or float")
    if type(delta) not in [complex, int, float]:
        raise CircleBuildGeometryError(
            "The parameter 'delta' must be a complex or float or int number"
        )

    surf_list = list()
    # Modulo on Alpha0 for sym
    Alpha0 = self.Alpha0 % (2 * pi / self.Zh)
    # The center
    Zc = self.H0 * exp(1j * Alpha0)
    # the radius of the circle on the VentilationCirc
    R = self.D0 / 2
    surf_list.append(
        Circle(
            point_ref=Zc,
            label=vent_label,
            radius=R,
            center=Zc,
        )
    )

    return surf_list
