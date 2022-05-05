def get_OP_list(self, type_OP=0):
    """Return the list of Operating Point defined by the matrix

    Parameters
    ----------
    self : OP_matrix
        An OP_matrix object
    type_OP : int
        0 OPdq, 1 OPslip

    Returns
    -------
    OP_list : [OP]
        List of OP objects
    """

    if self.N0 is not None:
        N = len(self.N0)
    else:
        N = len(self.Id)

    OP_list = list()
    for ii in range(N):
        OP_list.append(self.get_OP(ii, type_OP=type_OP))

    return OP_list
