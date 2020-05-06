# -*- coding: utf-8 -*-


def comp_mass_magnets(self):
    """Compute the mass of the hole magnets

    Parameters
    ----------
    self : HoleM58
        A HoleM58 object

    Returns
    -------
    Mmag: float
        mass of the Magnets [kg]

    """

    M = 0
    if self.magnet_0:
        M += self.H2 * self.W1 * self.magnet_0.Lmag * self.magnet_0.mat_type.struct.rho
    return M
