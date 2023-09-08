from numpy import pi

from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.labels import HOLEV_LAB, HOLEM_LAB


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM60
        A HoleM60 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
       True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the HoleM58

    """

    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id, surf_type = self.get_R_id()
    vent_label = lam_label + "_" + surf_type + "_R" + str(R_id) + "-"
    mag_label = lam_label + "_" + HOLEM_LAB + "_R" + str(R_id) + "-"

    # Get all the points
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z1s = point_dict["Z1s"]
    Z2s = point_dict["Z2s"]
    Z3s = point_dict["Z3s"]
    Z4s = point_dict["Z4s"]
    Z5s = point_dict["Z5s"]
    Z6s = point_dict["Z6s"]

    surf_list = list()
    # Create all the surfaces for all the cases
    # Upper surface without magnet
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Arc3(begin=Z2, end=Z4, is_trigo_direction=True))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Arc3(begin=Z5, end=Z1, is_trigo_direction=True))
    point_ref = (Z1 + Z4) / 2
    S1 = SurfLine(line_list=curve_list, point_ref=point_ref)
    
    # Lower surface without magnet
    curve_list = list()
    curve_list.append(Arc3(begin=Z1s, end=Z5s, is_trigo_direction=True))
    curve_list.append(Segment(Z5s, Z4s))
    curve_list.append(Arc3(begin=Z4s, end=Z2s, is_trigo_direction=True))
    curve_list.append(Segment(Z2s, Z1s))
    point_ref = (Z1s + Z4s) / 2
    S2 = SurfLine(line_list=curve_list, point_ref=point_ref)
    
    surf_list = [S1, S2]

    # # Create the surface list by selecting the correct ones
    # if self.magnet_0:
    S1.label = vent_label + "T0-S0"  # Hole
    S2.label = vent_label + "T1-S0"  # Hole
    #     surf_list = [S1, S2, S3]
    # else:
    #     S4.label = vent_label + "T0-S0"  # Hole
    #     surf_list = [S4]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
