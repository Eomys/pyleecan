def get_OP_array(self, *arg_list):
    """Return the OP matrix of the simulation
    Single speed simulation return a single line matrix

    Parameters
    ----------
    self : Simulation
        A Simulation object
    *arg_list : list of str
        arguments to select the OP_matrix columns name (N0, Id, Id, Tem...)

    Returns
    -------
    OP_matrix : ndarray
        Operating Points matrix (N_OP, len(arg_list))
    """

    var_load = self.get_var_load()
    if var_load is None:  # Single speed
        return self.input.OP.get_OP_array(arg_list)
    else:
        return var_load.get_OP_array(arg_list)
