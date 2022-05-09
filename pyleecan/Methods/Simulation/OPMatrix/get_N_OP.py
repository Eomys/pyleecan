def get_N_OP(self):
    """return the number of Operating point in the matrix

    Parameters
    ----------
    self : OPMatrix
        An OPMatrix object

    Returns
    -------
    N_OP : int
        Number of operating point in the OP_matrix
    """

    if self.N0 is not None:
        return len(self.N0)
    else:
        return len(self.Id)
