# -*- coding: utf-8 -*-


def get_height_magnet(self):
    """get the height of the hole magnets

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    Hmag: float
        height of the 2 Magnets [m]

    """

    # magnet_0 and magnet_1 have the same height
    Hmag = self.H2

    return Hmag
