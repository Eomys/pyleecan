# -*- coding: utf-8 -*-


def comp_mass_magnets(self):
    """Compute the mass of the hole magnets

    Parameters
    ----------
    self : HoleM57
        A HoleM57 object

    Returns
    -------
    Mmag: float
        mass of the 2 Magnets [kg]

    """

    M = 0
    # magnet_0 and magnet_1 can have different materials
    if self.magnet_0:
        M += (
            self.H2
            * self.W4
            * self.magnet_0.Lmag
            * self.magnet_0.mat_type.mechanics.rho
        )
    if self.magnet_1:
        M += (
            self.H2
            * self.W4
            * self.magnet_1.Lmag
            * self.magnet_1.mat_type.mechanics.rho
        )
    return M
