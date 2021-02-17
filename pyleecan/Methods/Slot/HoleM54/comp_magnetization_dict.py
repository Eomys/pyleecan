# -*- coding: utf-8 -*-

from numpy import pi
from pyleecan.Classes.Segment import Segment


def comp_magnetization_dict(self, is_north=True, return_type=2):
    """Compute the dictionary of the magnetization direction of the magnets (key=magnet_X, value=angle[rad])
    Mangetization angle with Hole centered on Ox axis

    Parameters
    ----------
    self : HoleM54
        a HoleM54 object
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

    mag_dict = dict()

    return mag_dict
