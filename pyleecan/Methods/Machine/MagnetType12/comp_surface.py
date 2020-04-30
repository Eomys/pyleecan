# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the Magnet surface (by numerical computation)

    Parameters
    ----------
    self : MagnetType12
        A MagnetType12 object

    Returns
    -------
    S: float
        Magnet surface [m**2]

    """

    surf = self.build_geometry()

    return surf[0].comp_surface()
