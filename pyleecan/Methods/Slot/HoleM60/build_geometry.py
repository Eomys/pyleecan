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
    # Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    # Z6 = point_dict["Z6"]
    Z1s = point_dict["Z1s"]
    Z2s = point_dict["Z2s"]
    # Z3s = point_dict["Z3s"]
    Z4s = point_dict["Z4s"]
    Z5s = point_dict["Z5s"]
    # Z6s = point_dict["Z6s"]
    ZM1 = point_dict["ZM1"]
    ZM2 = point_dict["ZM2"]
    ZM3 = point_dict["ZM3"]
    ZM4 = point_dict["ZM4"]
    ZM1s = point_dict["ZM1s"]
    ZM2s = point_dict["ZM2s"]
    ZM3s = point_dict["ZM3s"]
    ZM4s = point_dict["ZM4s"]

    surf_list = list()
    # Create all the surfaces for all the cases
    # Upper surface without magnet_1
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Arc3(begin=Z2, end=Z4, is_trigo_direction=True))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Arc3(begin=Z5, end=Z1, is_trigo_direction=True))
    point_ref = (Z1 + Z4) / 2
    S1 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Lower surface without magnet_0
    curve_list = list()
    curve_list.append(Arc3(begin=Z1s, end=Z5s, is_trigo_direction=True))
    curve_list.append(Segment(Z5s, Z4s))
    curve_list.append(Arc3(begin=Z4s, end=Z2s, is_trigo_direction=True))
    curve_list.append(Segment(Z2s, Z1s))
    point_ref = (Z1s + Z4s) / 2
    S0 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface 1 with magnet_1
    curve_list = list()
    curve_list.append(Segment(Z1, ZM1))
    curve_list.append(Segment(ZM1, ZM4))
    curve_list.append(Segment(ZM4, Z5))
    curve_list.append(Arc3(begin=Z5, end=Z1, is_trigo_direction=True))
    point_ref = (ZM1 + Z5) / 2
    SM11 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface 2 with magnet_1
    curve_list = list()
    curve_list.append(Segment(ZM2, Z2))
    curve_list.append(Arc3(begin=Z2, end=Z4, is_trigo_direction=True))
    curve_list.append(Segment(Z4, ZM3))
    curve_list.append(Segment(ZM3, ZM2))
    point_ref = (Z2 + ZM3) / 2
    SM12 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Magnet_1 surface
    curve_list = list()
    curve_list.append(Segment(ZM1, ZM2))
    curve_list.append(Segment(ZM2, ZM3))
    curve_list.append(Segment(ZM3, ZM4))
    curve_list.append(Segment(ZM4, ZM1))
    point_ref = (ZM1 + ZM3) / 2
    SM1 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface 1 with magnet_0
    curve_list = list()
    curve_list.append(Segment(Z1s, ZM1s))
    curve_list.append(Segment(ZM1s, ZM4s))
    curve_list.append(Segment(ZM4s, Z5s))
    curve_list.append(Arc3(begin=Z5s, end=Z1s, is_trigo_direction=False))
    point_ref = (ZM1s + Z5s) / 2
    SM01 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface 2 with magnet_0
    curve_list = list()
    curve_list.append(Segment(ZM2s, Z2s))
    curve_list.append(Arc3(begin=Z2s, end=Z4s, is_trigo_direction=False))
    curve_list.append(Segment(Z4s, ZM3s))
    curve_list.append(Segment(ZM3s, ZM2s))
    point_ref = (Z2s + ZM3s) / 2
    SM02 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Magnet_0 surface
    curve_list = list()
    curve_list.append(Segment(ZM1s, ZM4s))
    curve_list.append(Segment(ZM4s, ZM3s))
    curve_list.append(Segment(ZM3s, ZM2s))
    curve_list.append(Segment(ZM2s, ZM1s))
    point_ref = (ZM1s + ZM3s) / 2
    SM0 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    surf_list = list()
    if self.magnet_0:
        SM01.label = vent_label + "T0-S0"
        SM0.label = mag_label + "T0-S0"
        SM02.label = vent_label + "T1-S0"
        surf_list += [SM0, SM01, SM02]
        if self.magnet_1:
            SM11.label = vent_label + "T2-S0"
            SM1.label = mag_label + "T1-S0"
            SM12.label = vent_label + "T3-S0"
            surf_list += [SM1, SM11, SM12]
        else:
            S1.label = vent_label + "T2-S0"
            surf_list += [S1]
    else:
        S0.label = vent_label + "T0-S0"
        surf_list += [S0]
        if self.magnet_1:
            SM11.label = vent_label + "T1-S0"
            SM1.label = mag_label + "T1-S0"
            SM12.label = vent_label + "T2-S0"
            surf_list += [SM1, SM11, SM12]
        else:
            S1.label = vent_label + "T1-S0"
            surf_list += [S1]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
