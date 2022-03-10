def get_OP_matrix(self):
    """Get the Operating Point Matrix

    Parameters
    ----------
    self : LUT
        a LUT object

    Returns
    ----------
    OP_matrix : ndarray
        Operating Point Matrix
    """

    if self.simu is None:
        return None
    var_load = self.simu.get_var_load()
    if var_load is None:
        return None
    return var_load.OP_matrix
