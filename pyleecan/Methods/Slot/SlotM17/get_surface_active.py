# -*- coding: utf-8 -*-

from numpy import linspace, zeros

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full active surface

    Parameters
    ----------
    self : SlotM17
        A SlotM17 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_act: Surface
        Surface corresponding to the Active Area
    """

    self.check()
    # get the name of the lamination
    st = self.get_name_lam()
    Rext = self.parent.Rext

    Z1 = -Rext * 1j
    Z2 = Rext
    Z3 = Rext * 1j
    curve_list = list()
    curve_list.append(Arc1(Z1, Z2, Rext, True))
    curve_list.append(Arc1(Z2, Z3, Rext, True))
    curve_list.append(Segment(Z3, Z1))

    surface = SurfLine(
        line_list=curve_list, label="Wind_" + st + "_R0_T0_S0", point_ref=Rext / 2
    )

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
