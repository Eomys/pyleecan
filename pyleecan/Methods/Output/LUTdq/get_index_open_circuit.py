def get_index_open_circuit(self):
    """Get index of open circuit point in output list

    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    -------
    index : int
        Index of open circuit point in output list

    """

    # Find Id=Iq=0
    OP_list = self.get_OP_matrix()[:, 1:3].tolist()
    if [0, 0] in OP_list:
        index = OP_list.index([0, 0])
    else:
        index = None

    return index
