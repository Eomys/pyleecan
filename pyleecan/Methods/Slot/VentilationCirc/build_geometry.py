# -*- coding: utf-8 -*-


from ....Classes.Circle import Circle
from numpy import exp, pi
from ....Methods.Slot.VentilationCirc import *
from ....Functions.labels import VENT_LAB


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Compute the curve needed to plot the ventilations

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object
    sym : int
        Symetry to apply 2 = half the machine (Default value = 1 => full machine)
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
    RTS_id = "R" + str(self.parent.axial_vent.index(self)) + "-T0-S"
    vent_label = lam_label + "_" + VENT_LAB + "_" + RTS_id

    # checking if the param have good type
    if not (isinstance(sym, int)) or sym <= 0:
        raise CircleBuildGeometryError("The parameter 'sym' must be an integer > 0")
    if type(alpha) not in [int, float]:
        raise CircleBuildGeometryError("The parameter 'alpha' must be an int or float")
    if type(delta) not in [complex, int, float]:
        raise CircleBuildGeometryError(
            "The parameter 'delta' must be a complex or float or int number"
        )

    surf_list = list()

    assert self.Zh % sym == 0

    Zh = self.Zh // sym
    # For every Circle
    for ii in range(Zh):
        # The center
        Zc = (
            self.H0
            * exp(1j * self.Alpha0)
            * exp(1j * (ii * 2 * pi / self.Zh))
            * exp(1j * (pi / self.Zh + alpha))
        )
        # the radius of the circle on the VentilationCirc
        R = self.D0 / 2
        Zc += delta
        surf_list.append(
            Circle(
                point_ref=Zc,
                label=vent_label + str(ii),
                radius=R,
                center=Zc,
            )
        )

    return surf_list
