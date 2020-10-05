# -*- coding: utf-8 -*-

from numpy import linspace, zeros

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_wind(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """

    # Get the edges lines
    [Z10, Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1] = self._comp_point_coordinate()

    curve_list = list()
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z4))

    # Create the surface
    surf_wind = SurfLine(
        line_list=curve_list, label="Winding_Area", point_ref=(Z4 + Z5 + Z6 + Z7) / 4,
    )

    # Apply transformation
    surf_wind.rotate(alpha)
    surf_wind.translate(delta)

    return surf_wind
