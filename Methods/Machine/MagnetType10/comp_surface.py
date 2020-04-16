# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the Magnet surface (by analytical computation)

    Parameters
    ----------
    self : MagnetType10
        A MagnetType10 object

    Returns
    -------
    S: float
        Magnet surface [m**2]

    """

    return self.Hmag * self.Wmag
