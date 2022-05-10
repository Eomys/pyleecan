def get_OP_list(self):
    """Return the list of Operating Point defined by the matrix

    Parameters
    ----------
    self : OPMatrix
        An OPMatrix object

    Returns
    -------
    OP_list : [OP]
        List of OP objects
    """

    N_OP = self.get_N_OP()

    OP_list = list()
    for ii in range(N_OP):
        OP_list.append(self.get_OP(ii))

    return OP_list
