def comp_mass_magnets(self):
    """Compute the mass of the hole magnets (some of them may be missing)

    Parameters
    ----------
    self : HoleMag
        A HoleMag object

    Returns
    -------
    Mmag: float
        mass of the magnets [kg]
    """

    M = 0
    mag_list = self.get_magnet_list()
    for ii, mag in enumerate(mag_list):
        if mag is not None:
            Smag = self.comp_surface_magnet_id(ii)
            if mag.Lmag is None:
                Lmag = self.parent.L1
            else:
                Lmag = mag.Lmag
            # Check material definition
            if mag.mat_type.struct.rho is None:
                raise Exception(
                    "Error: For magnet material "
                    + str(mag.mat_type.name)
                    + " struct.rho is not set"
                )
            M += Smag * Lmag * mag.mat_type.struct.rho

    return M
