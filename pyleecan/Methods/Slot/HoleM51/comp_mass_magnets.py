# -*- coding: utf-8 -*-


def comp_mass_magnets(self):
    """Compute the mass of the hole magnets (some of them may be missing)

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    Mmag: float
        mass of the magnets [kg]

    """

    M = 0
    if self.magnet_0:
        M += self.W7 * self.H2 * self.magnet_0.Lmag * self.magnet_0.mat_type.struct.rho
    if self.magnet_1:
        M += self.W3 * self.H2 * self.magnet_1.Lmag * self.magnet_1.mat_type.struct.rho
    if self.magnet_2:
        M += self.W5 * self.H2 * self.magnet_2.Lmag * self.magnet_2.mat_type.struct.rho
    return M
