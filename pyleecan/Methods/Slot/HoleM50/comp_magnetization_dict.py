from numpy import pi
from ....Classes.Segment import Segment


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

    mag_dict = dict()
    S0 = Segment(point_dict["Z5"], point_dict["Z4"])
    mag_dict["magnet_0"] = S0.comp_normal()
    S1 = Segment(point_dict["Z4s"], point_dict["Z5s"])
    mag_dict["magnet_1"] = S1.comp_normal()

    if self.magnetization_dict_offset is not None:
        for key, value in self.magnetization_dict_offset:
            mag_dict[key] += value

    if not is_north:
        mag_dict["magnet_0"] += pi
        mag_dict["magnet_1"] += pi

    return mag_dict
