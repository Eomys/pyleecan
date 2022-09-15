from numpy import ndarray
from ....Classes.OPMatrix import OPMatrix


def set_OP_array(self, OP_matrix, *arg_list, is_update_input=True, input_index=0):
    """Set the OP_matrix and update the input if needed
    (To make sure that ref simu is in the OP_matrix)
    Ex: set_OP_array(OP_matrix, "N0", "Iq", "Iq", "Tem")

    Parameters
    ----------
    self : VarLoad
        A VarLoad object
    OP_matrix : ndarray
        OP_matrix to set
    *arg_list : several str
        To specify the OP_matrix column ("N0", "Id", "Iq"...)
    is_update_input : bool
        True to update the input
    input_index : int
        Index of the OP from the OP_matrix to set in the input (if is_update_input)
    """

    if isinstance(OP_matrix, ndarray):
        self.OP_matrix = OPMatrix()
        self.OP_matrix.set_OP_array(OP_matrix, *arg_list)
    else:
        self.OP_matrix = OP_matrix

    if not is_update_input or OP_matrix is None:
        return

    # Scan parent to find the input
    Sinput = None
    if self.parent is not None and hasattr(self.parent, "input"):
        Sinput = self.parent.input
    elif (
        self.parent is not None
        and self.parent.parent is not None
        and hasattr(self.parent.parent, "input")
    ):
        Sinput = self.parent.parent.input
    if Sinput is None:
        self.get_logger().warning("Can't find input when setting OP_matrix")
        return

    # Set the input OP
    if input_index >= self.OP_matrix.get_N_OP():
        self.get_logger.warning(
            "Index "
            + str(input_index)
            + " is not in the OP_matrix with "
            + str(self.OP_matrix.get_N_OP())
            + " OP(s)"
        )
        input_index = 0
    Sinput.OP = self.OP_matrix.get_OP(input_index)
