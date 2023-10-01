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
    label = "magnet_" + str(index)

    if index in [1, 2] and getattr(self, label) is not None:
        return self.W1 * self.H1
    if index in [0, 3] and getattr(self, label) is not None:
        return self.W2 * self.H1
    if index not in [0, 1, 2, 3]:
        raise Exception("Error index isn't equal at 0, 1, 2 or 3")
    return 0
