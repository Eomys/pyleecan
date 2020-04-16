# -*- coding: utf-8 -*-


def comp_volume_magnets(self):
    """Compute the volume of the magnet (if any)

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    Vmag: float
        Volume of the magnet [m**3]

    """
    if self.magnet_0:
        return self.W0 * self.H1 * self.magnet_0.Lmag
    else:
        return 0
