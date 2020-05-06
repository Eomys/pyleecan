# -*- coding: utf-8 -*-


def comp_volume_magnets(self):
    """Compute the volume of the hole magnet

    Parameters
    ----------
    self : HoleM58
        A HoleM58 object

    Returns
    -------
    Vmag: float
        Volume of the Magnet [m**3]

    """

    V = 0
    if self.magnet_0:
        V += self.H2 * self.W1 * self.magnet_0.Lmag
    return V
