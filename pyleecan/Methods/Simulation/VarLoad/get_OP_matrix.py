def get_OP_matrix(self, *arg_list):
    """Return the OP matrix

    Parameters
    ----------
    self : VarLoadCurrent
        A VarLoadCurrent object

    Returns
    -------
    OP_matrix : ndarray
        Operating Points matrix
    """

    return self.OP_matrix.get_OP_matrix(arg_list)
