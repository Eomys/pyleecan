# -*- coding: utf-8 -*-


def comp_surface_magnet_id(self, index):
    """Compute the surface of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object
    index : int
        Index of the magnet to compute the surface

    Returns
    -------
    Smag: float
        Surface of the Magnet [m**2]
    """

    if index == 0 and self.magnet_0:
        return self.W0 * self.H1
    return 0
