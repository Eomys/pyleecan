from numpy import pi
from ....Classes.Segment import Segment


def comp_magnetization_dict(self, is_north=True):
    """Compute the dictionary of the magnetization direction of the magnets (key=magnet_X, value=angle[rad])
    Mangetization angle with Hole centered on Ox axis

    Parameters
    ----------
    self : HoleMLSRPM
        a HoleMLSRPM object
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
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]

    Zch = (Z3 + Z4) / 2
    Zcl = (Z7 + Z8) / 2
    S0 = Segment(Zch, Zcl)
    mag_dict["magnet_0"] = S0.comp_normal()

    ####Comp_normal direction?

    if not is_north:
        mag_dict["magnet_0"] += pi

    if self.magnetization_dict_offset is not None:
        for key, value in self.magnetization_dict_offset:
            mag_dict[key] += value

    return mag_dict
