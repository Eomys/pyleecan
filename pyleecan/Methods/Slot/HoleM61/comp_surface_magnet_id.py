# -*- coding: utf-8 -*-


def comp_surface_magnet_id(self, index):
    """Compute the surface of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleM61
        A HoleM61 object
    index : int
        Index of the magnet to compute the surface

    Returns
    -------
    Smag: float
        Surface of the Magnet [m**2]
    """
    # define sum all surface
    sum = 0
    label = "magnet_" + str(index)

    if index in [1, 2] and getattr(self, label) is not None:
        sum += self.W1 * self.H1
    if index in [0, 3] and getattr(self, label) is not None:
        sum += self.W2 * self.H1

    return sum
