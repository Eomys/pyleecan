from numpy import zeros, angle
from ..OPMatrix import OPMatrixException


def get_OP_array(self, *arg_list):
    """get the OP_matrix by identifying the columns
    Ex: get_OP_array("N0", "Iq", "Iq", "Tem")
    get_OP_array(OP_matrix) calls get_OP_array("N0", "Id", "Iq", "Tem", "Pem")

    Parameters
    ----------
    self : OP
        Operating Point object to convert to a matrix
    *arg_list : list of str
        arguments to specify the OP_matrix columns name

    Returns
    -------
    OP_matrix: ndarray
        Single line OP_matrix with the selected columns
    """

    # Extract arg_list it the function called from another script with *arg_list
    if len(arg_list) == 1 and type(arg_list[0]) == tuple:
        arg_list = arg_list[0]

    # Init OP_matrix
    OP_matrix = zeros((1, len(arg_list)))

    # Setup default argument (N0, Id, Iq, Tem, Pem)
    Idq_dict = self.get_Id_Iq()
    if len(arg_list) == 0:
        if self.N0 is not None:
            arg_list.append("N0")
        if Idq_dict["Id"] is not None:
            arg_list.append("Id")
        if Idq_dict["Iq"] is not None:
            arg_list.append("Iq")
        if self.Tem_av_ref is not None:
            arg_list.append("Tem")
        if self.Pem_av_ref is not None:
            arg_list.append("Pem")

    # Set column by column according to arg_list
    I0_dict = self.get_I0_Phi0()
    Udq_dict = self.get_Ud_Uq()
    U0_dict = self.get_U0_UPhi0()
    for ii in range(len(arg_list)):
        # N0
        if arg_list[ii].lower() in ["n0", "no", "0n", "on"]:
            OP_matrix[0, ii] = self.N0
        # Id/Iq
        elif arg_list[ii].lower() in ["id", "di", "id_ref"]:
            OP_matrix[0, ii] = Idq_dict["Id"]
        elif arg_list[ii].lower() in ["iq", "qi", "iq_ref"]:
            OP_matrix[0, ii] = Idq_dict["Iq"]
        # I0/Phi0
        elif arg_list[ii].lower() in ["i0", "0i", "i0_ref"]:
            OP_matrix[0, ii] = I0_dict["I0"]
        elif arg_list[ii].lower() in ["iphi0", "phi0", "phio"]:
            OP_matrix[0, ii] = I0_dict["Phi0"]
        # Tem
        elif arg_list[ii].lower() in ["tem", "t", "tem_av", "tem_av_ref"]:
            OP_matrix[0, ii] = self.Tem_av_ref
        # Pem
        elif arg_list[ii].lower() in ["pem", "p", "pem_av", "pem_av_ref"]:
            OP_matrix[0, ii] = self.Pem_av_ref
        # Ud/Uq
        elif arg_list[ii].lower() in ["ud", "du", "ud_ref"]:
            OP_matrix[0, ii] = Udq_dict["Ud"]
        elif arg_list[ii].lower() in ["uq", "qu", "uq_ref"]:
            OP_matrix[0, ii] = Udq_dict["Uq"]
        # U0/UPhi0
        elif arg_list[ii].lower() in ["u0", "0u", "u0_ref"]:
            OP_matrix[0, ii] = U0_dict["U0"]
        elif arg_list[ii].lower() in ["uphi0", "uphio"]:
            OP_matrix[0, ii] = U0_dict["UPhi0"]
        # If
        elif arg_list[ii].lower() in ["if", "fi"]:
            OP_matrix[0, ii] = self.If_ref
        else:
            raise OPMatrixException(
                "Error in OP_matrix.get_OP_array, unknow column name for index "
                + str(ii)
                + " in "
                + str(arg_list)
            )

    return OP_matrix
