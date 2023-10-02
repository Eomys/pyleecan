def get_dim_active(self):
    """Return the dimension of the active part of the lamination (Nrad, Ntan)

    Parameters
    ----------
    self : LamSlotM
        A LamSlotM object

    Returns
    -------
    (Nrad, Ntan): tuple
        Number of layer in radial and tangential direction
    """

    if self.mur_lin_matrix is None and self.Brm20_matrix is None:
        return (1, 1)  # Default case

    # Get number of layer from enforced property matrix
    if self.mur_lin_matrix is None and self.Brm20_matrix is not None:
        mat = self.Brm20_matrix
        mat_name = "Brm20_matrix"
    elif self.mur_lin_matrix is not None and self.Brm20_matrix is None:
        mat = self.mur_lin_matrix
        mat_name = "mur_lin_matrix"
    else:
        if self.mur_lin_matrix.shape != self.Brm20_matrix.shape:
            raise Exception("Error mur_lin_matrix and Brm20_matrix shape must match")
        mat = self.mur_lin_matrix
        mat_name = "Brm20_matrix and mur_lin_matrix"
    # Check matrix shape
    if len(mat.shape) != 3 or mat.shape[2] != self.slot.Zs:
        raise Exception("Error " + mat_name + " shape must be [Nrad, Ntan, Zs]!")

    return mat.shape[0:2]
