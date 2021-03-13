from numpy import pi


def comp_magnetization_dict(self, is_north=True):
    """Compute the dictionary of the magnetization direction of the magnets (key=magnet_X, value=angle[rad])
    Mangetization angle with Hole centered on Ox axis

    Parameters
    ----------
    self : Hole
        a Hole object
    is_north: True
        True: comp north magnetization, else add pi [rad]

    Returns
    -------
    mag_dict: dict
        magnetization dictionary (key=magnet_X, value=angle[rad])
    """

    if self.magnetization_dict_offset is not None:
        mag_dict = self.magnetization_dict_offset.copy()
        if not is_north:
            for key in mag_dict.keys():
                mag_dict[key] += pi
        return mag_dict
    else:
        return dict()
