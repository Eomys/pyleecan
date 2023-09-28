from numpy import pi
from ....Classes.Segment import Segment


def comp_magnetization_dict(self, is_north=True):
    """Compute the dictionary of the magnetization direction of the magnets (key=magnet_X, value=angle[rad])
    Mangetization angle with Hole centered on Ox axis

    Parameters
    ----------
    self : HoleM61
        a HoleM61 object
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
    S0 = Segment(point_dict["ZM7"], point_dict["ZM8"])
    mag_dict["magnet_0"] = S0.comp_normal()
    S1 = Segment(point_dict["ZM4"], point_dict["ZM1"])
    mag_dict["magnet_1"] = S1.comp_normal()
    S2 = Segment(point_dict["ZM9"], point_dict["ZM12"])
    mag_dict["magnet_2"] = S2.comp_normal()
    S3 = Segment(point_dict["ZM16"], point_dict["ZM15"])
    mag_dict["magnet_3"] = S3.comp_normal()

    if not is_north:
        mag_dict["magnet_0"] += pi
        mag_dict["magnet_1"] += pi
        mag_dict["magnet_2"] += pi
        mag_dict["magnet_3"] += pi

    if self.magnetization_dict_offset is not None:
        for key, value in self.magnetization_dict_offset:
            mag_dict[key] += value

    return mag_dict
