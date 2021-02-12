# -*- coding: utf-8 -*-

from numpy import pi


def comp_magnetization_dict(self, is_north=True):
    """Compute the dictionary of the magnetization direction of the magnets (key=magnet_X, value=angle[rad])
    Mangetization angle with Hole centered on Ox axis

    Parameters
    ----------
    self : HoleM50
        a HoleM50 object
    is_north: True
        True: comp north magnetization, else add pi [rad]

    Returns
    -------
    mag_dict: dict
        magnetization dictionary (key=magnet_X, value=angle[rad])
    """

    # Comp magnet
    point_dict = self._comp_point_coordinate()

    alpha = 0
    if not is_north:
        alpha = pi

    mag_dict = dict()
    S0 = Segment(point_dict["Z5"], point_dict["Z4"])
    mag_dict["magnet_0"] = S0.comp_normal + alpha
    S1 = Segment(point_dict["Z5s"], point_dict["Z4s"])
    mag_dict["magnet_1"] = S1.comp_normal + alpha

    if self.magnetization_dict_enforced is not None:
        mag_dict.update(self.magnetization_dict_enforced)

    return mag_dict
