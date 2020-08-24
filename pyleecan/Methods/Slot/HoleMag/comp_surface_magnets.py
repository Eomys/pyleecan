# -*- coding: utf-8 -*-


def comp_surface_magnets(self):
    """Compute the surface of all the magnet(s)

    Parameters
    ----------
    self : HoleMag
        A HoleMag object

    Returns
    -------
    Smag: float
        Surface of all the Magnet(s) [m**2]
    """

    mag_list = self.get_magnet_list()
    for ii in range(len(mag_list)):
        Smag += self.comp_surface_magnet_id(ii)
    return Smag
