def get_OP_list(self, type_OP=0):
    """Return the list of Operating Point defined by the matrix

    Parameters
    ----------
    self : OPMatrix
        An OPMatrix object
    type_OP : int
        0 OPdq, 1 OPslip

    Returns
    -------
    OP_list : [OP]
        List of OP objects
    """

    N_OP = self.get_N_OP()

    OP_list = list()
    for ii in range(N_OP):
        OP_list.append(self.get_OP(ii, type_OP=type_OP))

    return OP_list
