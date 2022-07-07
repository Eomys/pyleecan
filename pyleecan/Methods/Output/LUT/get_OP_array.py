def get_OP_array(self, *arg_list):
    """Get the Operating Point array

    Parameters
    ----------
    self : LUT
        a LUT object

    Returns
    ----------
    OP_array : ndarray
        Operating Point Matrix object
    """

    OPM = self.get_OP_matrix_obj()
    return OPM.get_OP_array(*arg_list)
