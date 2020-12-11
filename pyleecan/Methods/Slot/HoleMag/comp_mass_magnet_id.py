# -*- coding: utf-8 -*-


def comp_mass_magnet_id(self, index):
    """Compute the mass of the hole magnet of the corresponding index

    Parameters
    ----------
    self : HoleMag
        A HoleMag object
    index : int
        Index of the magnet to compute the surface

    Returns
    -------
    Mmag: float
        Mass of the Magnet [m**2]
    """

    mag_list = self.get_magnet_list()
    if mag_list[index] is None:
        return 0
    else:
        return self.comp_surface_magnet_id(index) * mag_list[index].Lmag
