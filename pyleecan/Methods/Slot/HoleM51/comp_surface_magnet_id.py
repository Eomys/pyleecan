# -*- coding: utf-8 -*-


def comp_surface_magnet_id(self, index):
    """Compute the surface of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object
    index : int
        Index of the magnet to compute the surface

    Returns
    -------
    Smag: float
        Surface of the Magnet [m**2]
    """

    if index == 0 and self.magnet_0:
        return self.W7 * self.H2
    if index == 1 and self.magnet_1:
        return self.W3 * self.H2
    if index == 2 and self.magnet_2:
        return self.W5 * self.H2
    return 0
