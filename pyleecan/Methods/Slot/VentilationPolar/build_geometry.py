# -*- coding: utf-8 -*-

from numpy import exp, pi

from ....Classes.PolarArc import PolarArc
from ....Methods.Slot.VentilationPolar import *
from ....Functions.labels import VENT_LAB


def build_geometry(self, alpha=0, delta=0):
    """Compute the curve needed to plot the ventilations

    Parameters
    ----------
    self : VentilationPolar
        A VentilationPolar object
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : complex
        Complex for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        A list of PolarArc

    Raises
    _______
    PolarArcBuildGeometryError
        The parameter 'sym' must be an integer > 0
        The parameter 'alpha' must be an int or float
        The parameter 'delta' must be a complex or float or int number
    """

    lam_label = self.parent.get_label()
    RTS_id = "R" + str(self.parent.axial_vent.index(self)) + "-T0-S0"
    vent_label = lam_label + "_" + VENT_LAB + "_" + RTS_id

    # checking if the param have good type
    if type(alpha) not in [int, float]:
        raise PolarArcBuildGeometryError(
            "The parameter 'alpha' must be an int or float"
        )
    if type(delta) not in [complex, int, float]:
        raise PolarArcBuildGeometryError(
            "The parameter 'delta' must be a complex or float or int number"
        )

    surf_list = list()
    # Modulo on Alpha for sym
    Alpha0 = self.Alpha0 % (2 * pi / self.Zh)
    Zc = (self.H0 + (self.D0 / 2)) * exp(1j * Alpha0)
    surf_list.append(
        PolarArc(
            point_ref=Zc,
            label=vent_label,
            angle=self.W1,
            height=self.D0,
        )
    )

    return surf_list
