# -*- coding: utf-8 -*-

from numpy import pi
from pyleecan.Classes.Segment import Segment


def comp_magnetization_dict(self, is_north=True, return_type=2):
    """Compute the dictionary of the magnetization direction of the magnets (key=magnet_X, value=angle[rad])
    Mangetization angle with Hole centered on Ox axis

    Parameters
    ----------
    self : HoleM51
        a HoleM51 object
    is_north: True
        True: comp north magnetization, else add pi [rad]
    return_type : int
        0: Normal as tuple of complex
        1: Z2 - Z1 (with Z1 and Z2 the points from return_type 0)
        2: the angle of the vector of return_type 1 according to Ox [rad]

    Returns
    -------
    mag_dict: dict
        magnetization dictionary (key=magnet_X, value=angle[rad])
    """

    # Comp magnet
    point_dict = self._comp_point_coordinate()

    mag_dict = dict()
    S0 = Segment(point_dict["Z18"], point_dict["Z19"])
    mag_dict["magnet_0"] = S0.comp_normal(return_type=return_type)
    S1 = Segment(point_dict["Z13"], point_dict["Z14"])
    mag_dict["magnet_1"] = S1.comp_normal(return_type=return_type)
    S2 = Segment(point_dict["Z8"], point_dict["Z9"])
    mag_dict["magnet_2"] = S2.comp_normal(return_type=return_type)

    if not is_north and return_type == 2:
        mag_dict["magnet_0"] += pi
        mag_dict["magnet_1"] += pi
        mag_dict["magnet_2"] += pi

    if self.magnetization_dict_enforced is not None:
        mag_dict.update(self.magnetization_dict_enforced)

    return mag_dict
