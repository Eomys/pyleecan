from numpy import linspace, zeros

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1


def get_surface_active(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """

    # get the name of the lamination
    st = self.get_name_lam()

    # get the bore radius
    Rbo = self.get_Rbo()

    # Create reference point
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]
    point_ref = Z1 + Z2 + Z3 + Z4 + Z5 + Z6 + Z7 + Z8 / 8

    # Create curve list
    curve_list = self.build_geometry()
    curve_list.append(Arc1(Z8, Z1, -Rbo, is_trigo_direction=False))

    surface = SurfLine(
        line_list=curve_list, label="Wind_" + st + "_R0_T0_S0", point_ref=point_ref
    )

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
