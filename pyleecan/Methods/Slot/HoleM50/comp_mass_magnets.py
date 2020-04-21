# -*- coding: utf-8 -*-


def comp_mass_magnets(self):
    """Compute the mass of the hole magnets

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object

    Returns
    -------
    Mmag: float
        mass of the 2 Magnets [kg]

    """

    M = 0
    # magnet_0 and magnet_1 can have different materials
    if self.magnet_0:
        M += self.H3 * self.W4 * self.magnet_0.Lmag * self.magnet_0.mat_type.struct.rho
    if self.magnet_1:
        M += self.H3 * self.W4 * self.magnet_1.Lmag * self.magnet_1.mat_type.struct.rho
    return M
