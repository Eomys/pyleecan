# -*- coding: utf-8 -*-


def get_height_magnet_id(self, index):
    """Get the height of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleM52R
        A HoleM52R object
    index : int
        Index of the magnet to get the height

    Returns
    -------
    Hmag: float
        Height of the Magnet [m]
    """

    if index == 0 and self.magnet_0:
        return self.H1
    return 0
