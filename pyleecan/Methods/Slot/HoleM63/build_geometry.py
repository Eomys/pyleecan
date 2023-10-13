from numpy import pi

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.labels import HOLEV_LAB, HOLEM_LAB


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM63
        A HoleM63 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
        True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the HoleM63

    """
    Rbo = self.get_Rbo()

    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id, surf_type = self.get_R_id()
    mag_label = f"{lam_label}_{HOLEM_LAB}_R{R_id}-"
    vent_label = f"{lam_label}_{surf_type}_R{R_id}-"
    point_dict = self._comp_point_coordinate()

    surf_list = list()
    # Create all the surfaces for all the case

    # Get all the points
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]

    # surface
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    if self.top_flat:
        curve_list.append(Segment(Z2, Z3))
    else:
        curve_list.append(
            Arc1(
                begin=Z2,
                end=Z3,
                radius=(Rbo - self.H1),
                is_trigo_direction=True,
            )
        )
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z1))

    point_ref = (Z3 + Z1) / 2
    S1 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    surf_list = list()
    if self.magnet_0 is None:
        S1.label = vent_label + "T0-S0"
        surf_list = [S1]
    else:
        S1.label = mag_label + "T0-S0"
        surf_list = [S1]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
