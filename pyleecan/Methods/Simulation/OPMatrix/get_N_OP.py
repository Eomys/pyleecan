from ....Methods.Simulation.OPMatrix import OPMatrixException


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
    elif self.Id_ref is not None:
        return len(self.Id_ref)
    elif self.Ud_ref is not None:
        return len(self.Ud_ref)
    else:
        raise OPMatrixException(
            "Unable to get the size of the Operating Matrix (call set_OP_matrix first)"
        )
