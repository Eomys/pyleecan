# -*- coding: utf-8 -*-


def comp_surface_magnet_id(self, index):
    """Compute the surface of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleM60
        A HoleM60 object
    index : int
        Index of the magnet to compute the surface

    Returns
    -------
    Smag: float
        Surface of the Magnet [m**2]
    """

    # all magnet has the same surface
    label = "magnet_" + str(index)
    if index in [0, 1] and getattr(self, label) is not None:
        return self.W1 * self.H0
    return 0
