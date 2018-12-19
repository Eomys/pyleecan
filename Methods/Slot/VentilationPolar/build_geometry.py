# -*- coding: utf-8 -*-
"""@package Methods.Machine.Ventilation_Polar.build_geometry
Ventilation_Polar build_geometry method
@date Created on Tue Mar 08 11:38:33 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import exp, pi

from pyleecan.Classes.PolarArc import PolarArc


def build_geometry(self, sym=1, alpha=0, delta=0, is_stator=True):
    """Compute the curve needed to plot the ventilations

    Parameters
    ----------
    self : VentilationPolar
        A VentilationPolar object
    sym : int
        Symetry to apply 2 = half the machine (Default value = 1 => full machine)
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : complex
        Complex for translation (Default value = 0)
    is_stator : bool
        True if ventilation is on the stator and 0 on the rotor (Default value = True)

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

    if is_stator:
        st = "Stator"
    else:
        st = "Rotor"

    # checking if the param have good type
    if not (isinstance(sym, int)) or sym <= 0:
        raise PolarArcBuildGeometryError("The parameter 'sym' must be an integer > 0")
    if type(alpha) not in [int, float]:
        raise PolarArcBuildGeometryError(
            "The parameter 'alpha' must be an int or float"
        )
    if type(delta) not in [complex, int, float]:
        raise PolarArcBuildGeometryError(
            "The parameter 'delta' must be a complex or float or int number"
        )

    surf_list = list()
    assert self.Zh % sym == 0
    Zh = self.Zh // sym
    # For every PolarArc
    for ii in range(Zh):
        Zc = (self.H0 + (self.D0 / 2)) * exp(
            1j * (self.Alpha0 + ii * 2 * pi / self.Zh + (pi / self.Zh + alpha))
        )
        Zc += delta
        surf_list.append(
            PolarArc(
                point_ref=Zc,
                label="Ventilation_" + st + "_" + str(ii),
                angle=self.W1,
                height=self.D0,
            )
        )

    return surf_list


class PolarArcBuildGeometryError(Exception):
    """ """

    pass
