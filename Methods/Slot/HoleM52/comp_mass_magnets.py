# -*- coding: utf-8 -*-


def comp_mass_magnets(self):
    """Compute the mass of the magnet (if any)

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    Mmag: float
        mass of the magnet [kg]

    """
    if self.magnet_0:
        return (
            self.W0 * self.H1 * self.magnet_0.Lmag * self.magnet_0.mat_type.struct.rho
        )
    else:
        return 0
