# -*- coding: utf-8 -*-


def comp_mass(self):
    """Compute the Magnet mass (by analytical computation)

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    M: float
        Magnet mass [kg]

    """

    return self.comp_volume() * self.mat_type.struct.rho
