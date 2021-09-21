# -*- coding: utf-8 -*-

from numpy import exp, pi

from ....Classes.Trapeze import Trapeze
from ....Methods.Slot.VentilationTrap import *
from ....Functions.labels import VENT_LAB


def build_geometry(self, alpha=0, delta=0):
    """Compute the curve needed to plot the ventilations

    Parameters
    ----------
    self : VentilationTrap
        A VentilationTrap object
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : complex
        Complex for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        A list of Trapeze
    """

    lam_label = self.parent.get_label()
    RTS_id = "R" + str(self.parent.axial_vent.index(self)) + "-T0-S0"
    vent_label = lam_label + "_" + VENT_LAB + "_" + RTS_id

    # checking if the param have good type
    if type(alpha) not in [int, float]:
        raise TrapezeBuildGeometryError("The parameter 'alpha' must be an int or float")
    if type(delta) not in [complex, int, float]:
        raise TrapezeBuildGeometryError(
            "The parameter 'delta' must be a complex or float or int number"
        )

    surf_list = list()
    # Modulo on Alpha for sym
    Alpha0 = self.Alpha0 % (2 * pi / self.Zh)
    Zc = (self.H0 + (self.D0 / 2)) * exp(1j * Alpha0)
    surf_list.append(
        Trapeze(point_ref=Zc, label=vent_label, height=self.D0, W1=self.W1, W2=self.W2,)
    )
    return surf_list
