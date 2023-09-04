from numpy import unique


def get_all_mag_obj(self):
    """Return all the magnet object for all the layers

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

    Returns
    -------
    mag_list : [Magnet]
        List of magnet object to define
    """

    mag_list = list()
    if self.mur_lin_matrix is None and self.Brm20_matrix is None:
        return [self.magnet]
    elif self.mur_lin_matrix is not None:
        _, index_unique = unique(self.mur_lin_matrix, return_index=True)
        for ii, flat_index in enumerate(index_unique):
            mag_list.append(self.magnet.copy())
            mag_list[-1].mat_type.name = "Magnet_" + str(ii + 1)
            mag_list[-1].mat_type.mag.mur_lin = self.mur_lin_matrix.flat[flat_index]
            # Assume that if a magnet has a different mur_lin, it has a different Brm20
            # So unique is applied only on mur (no cross unique check)
            if self.Brm20_matrix is not None:
                mag_list[-1].mat_type.mag.Brm20 = self.Brm20_matrix.flat[flat_index]
    else:  # Only change Brm20
        Brm20_val = unique(self.Brm20_matrix)
        for ii, Brm20 in enumerate(Brm20_val):
            mag_list.append(self.magnet.copy())
            mag_list[-1].mat_type.mag.Brm20 = Brm20
            mag_list[-1].mat_type.name = "Magnet_" + str(ii + 1)
            name_index += 1

    return mag_list
