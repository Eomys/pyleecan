# -*- coding: utf-8 -*-


def comp_surface_magnets(self):
    """Compute the surface of the magnet (if any)

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    Smag: float
        Surface of the magnet [m**2]

    """
    if self.magnet_0:
        return self.W0 * self.H1
    else:
        return 0
