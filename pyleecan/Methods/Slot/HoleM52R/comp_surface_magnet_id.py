# -*- coding: utf-8 -*-


def comp_surface_magnet_id(self, index):
    """Compute the surface of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleM52R
        A HoleM52R object
    index : int
        Index of the magnet to compute the surface

    Returns
    -------
    Smag: float
        Surface of the Magnet [m**2]
    """
    return self.W0 * self.H1 if index == 0 and self.magnet_0 else 0
