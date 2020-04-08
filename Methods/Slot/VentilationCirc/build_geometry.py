# -*- coding: utf-8 -*-


from pyleecan.Classes.Circle import Circle
from numpy import exp, pi


def build_geometry(self, sym=1, alpha=0, delta=0, is_stator=True):
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
    is_stator : bool
        True if ventilation is on the stator and 0 on the rotor (Default value = True)

    Returns
    -------
    surf_list: list
        A list of Circle

    """
    if is_stator:
        st = "Stator"
    else:
        st = "Rotor"

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
                label="Ventilation_" + st + "_" + str(ii),
                radius=R,
                center=Zc,
            )
        )

    return surf_list


class CircleBuildGeometryError(Exception):
    """ """

    pass


class SymmetryError(Exception):
    """ """

    pass
