from numpy import unique


def get_all_mag_obj(self):
    """Return all the magnet object for all the layers

    Parameters
    ----------
    self : LamSlotMagNS
        A LamSlotMagNS object

    Returns
    -------
    mag_list : [Magnet]
        List of magnet object to define
    """

    if self.mur_lin_matrix is None and self.Brm20_matrix is None:
        if len(self.magnet_north.compare(self.magnet_south)) > 0:
            return [self.magnet_north, self.magnet_south]
        else:
            return [self.magnet_north]
    else:
        raise NotImplementedError(
            "Error, Magnet matrix is not available yet for uneven North/South machines"
        )
