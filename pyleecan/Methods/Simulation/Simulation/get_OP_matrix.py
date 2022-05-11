def get_OP_matrix(self, *arg_list):
    """Return the OP matrix of the simulation
    Single speed simulation return a single line matrix

    Parameters
    ----------
    self : Simulation
        A Simulation object

    Returns
    -------
    OP_matrix : ndarray
        Operating Points matrix
    """

    var_load = self.get_var_load()
    if var_load is None:  # Single speed
        return self.input.OP.get_OP_matrix(arg_list)
    else:
        return var_load.get_OP_matrix(arg_list)
