# -*- coding: utf-8 -*-

from numpy import exp, pi

from ....Classes.Trapeze import Trapeze
from ....Methods.Slot.VentilationTrap import *
from ....Functions.labels import VENT_LAB


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Compute the curve needed to plot the ventilations

    Parameters
    ----------
    self : VentilationTrap
        A VentilationTrap object
    sym : int
        Symetry to apply 2 = half the machine (Default value = 1 => full machine)
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
    RTS_id = "R" + str(self.parent.axial_vent.index(self)) + "-T0-S"
    vent_label = lam_label + "_" + VENT_LAB + "_" + RTS_id

    # checking if the param have good type
    if not (isinstance(sym, int)) or sym <= 0:
        raise TrapezeBuildGeometryError("The parameter 'sym' must be an integer > 0")
    if type(alpha) not in [int, float]:
        raise TrapezeBuildGeometryError("The parameter 'alpha' must be an int or float")
    if type(delta) not in [complex, int, float]:
        raise TrapezeBuildGeometryError(
            "The parameter 'delta' must be a complex or float or int number"
        )

    surf_list = list()
    assert self.Zh % sym == 0
    Zh = self.Zh // sym
    # For every Trapeze
    for ii in range(Zh):
        Zc = (self.H0 + (self.D0 / 2)) * exp(
            1j * ((self.Alpha0 + ii * 2 * pi / self.Zh) + (pi / self.Zh + alpha))
        )
        Zc += delta
        surf_list.append(
            Trapeze(
                point_ref=Zc,
                label=vent_label + str(ii),
                height=self.D0,
                W1=self.W1,
                W2=self.W2,
            )
        )
    return surf_list
