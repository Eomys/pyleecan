from numpy import zeros, angle
from . import OPMatrixException


def get_OP_array(self, *arg_list):
    """get the OP_matrix by identifying the columns
    Ex: get_OP_array("N0", "Iq", "Iq", "Tem")
    get_OP_array() calls get_OP_array("N0", "Id", "Iq", "Tem", "Pem")

    Parameters
    ----------
    self : OPMatrix
        OPMatrix object to update
    *arg_list : list of str
        arguments to select the OP_matrix columns name

    Returns
    -------
    OP_matrix : ndarray
        Operating point matrix with the selected columns (Array (N_OP, len(arg_list)))
    """

    # Extract arg_list it the function called from another script with *arg_list
    if len(arg_list) == 1 and type(arg_list[0]) == tuple:
        arg_list = arg_list[0]
    arg_list = list(arg_list)

    # "all" returns all the columns set by the latest set_OP_array
    if len(arg_list) == 1 and arg_list[0].lower() in ["all", "al", "a"]:
        if self.col_names is not None and len(self.col_names) > 0:
            arg_list = self.col_names
        else:
            arg_list = list()
            if self.N0 is not None:
                arg_list.append("N0")
            if self.Id_ref is not None:
                arg_list.append("Id")
            if self.Iq_ref is not None:
                arg_list.append("Iq_ref")
            if self.Tem_av_ref is not None:
                arg_list.append("Tem")
            if self.Pem_av_ref is not None:
                arg_list.append("Pem")

    # Init OP_matrix
    N_OP = self.get_N_OP()
    OP_matrix = zeros((N_OP, len(arg_list)))

    # Setup default argument (N0, Id, Iq, Tem, Pem)
    if len(arg_list) == 0:
        if self.N0 is not None:
            arg_list.append("N0")
        if self.Id_ref is not None:
            arg_list.append("Id")
        if self.Iq_ref is not None:
            arg_list.append("Iq")
        if self.Tem_av_ref is not None:
            arg_list.append("Tem")
        if self.Pem_av_ref is not None:
            arg_list.append("Pem")

    arg_list_lower = [arg.lower() for arg in arg_list]
    # Convertion I0/Phi0 to Id/Iq will be done later
    is_convert_I0 = False
    if "i0" in arg_list_lower and (
        "phi0" in arg_list_lower or "iphi0" in arg_list_lower
    ):
        I0_index = arg_list_lower.index("i0")
        if "phi0" in arg_list_lower:
            Phi0_index = arg_list_lower.index("phi0")
        else:
            Phi0_index = arg_list_lower.index("iphi0")
        is_convert_I0 = True
        arg_list[I0_index] = "Id"
        arg_list[Phi0_index] = "Iq"
    # Convertion U0/UPhi0 to Ud/Uq
    is_convert_U0 = False
    if "u0" in arg_list_lower and "uphi0" in arg_list_lower:
        U0_index, UPhi0_index = (
            arg_list_lower.index("u0"),
            arg_list_lower.index("uphi0"),
        )
        U0 = OP_matrix[:, U0_index]
        UPhi0 = OP_matrix[:, UPhi0_index]
        is_convert_U0 = True
        arg_list[U0_index] = "Ud"
        arg_list[UPhi0_index] = "Uq"

    # Set column by column according to arg_list
    for ii in range(len(arg_list)):
        if arg_list[ii].lower() in ["n0", "no", "0n", "on"]:
            OP_matrix[:, ii] = self.N0[:]
        elif arg_list[ii].lower() in ["id", "di", "id_ref"]:
            OP_matrix[:, ii] = self.Id_ref[:]
        elif arg_list[ii].lower() in ["iq", "qi", "iq_ref"]:
            OP_matrix[:, ii] = self.Iq_ref[:]
        elif arg_list[ii].lower() in ["tem", "t", "tem_av", "tem_av_ref"]:
            OP_matrix[:, ii] = self.Tem_av_ref[:]
        elif arg_list[ii].lower() in ["pem", "p", "pem_av", "pem_av_ref"]:
            OP_matrix[:, ii] = self.Pem_av_ref[:]
        elif arg_list[ii].lower() in ["ud", "du", "ud_ref"]:
            OP_matrix[:, ii] = self.Ud_ref[:]
        elif arg_list[ii].lower() in ["uq", "qu", "uq_ref"]:
            OP_matrix[:, ii] = self.Uq_ref[:]
        elif arg_list[ii].lower() in ["if", "fi"]:
            OP_matrix[:, ii] = self.If_ref[:]
        else:
            raise OPMatrixException(
                "Error in OP_matrix.get_OP_array, unknow column name for index "
                + str(ii)
                + " in "
                + str(arg_list)
            )

    # Convertion
    if is_convert_I0:
        Z = OP_matrix[:, I0_index] + 1j * OP_matrix[:, Phi0_index]
        OP_matrix[:, I0_index] = abs(Z)
        OP_matrix[:, Phi0_index] = angle(Z)
    if is_convert_U0:
        Z = OP_matrix[:, U0_index] + 1j * OP_matrix[:, UPhi0_index]
        OP_matrix[:, U0_index] = abs(Z)
        OP_matrix[:, UPhi0_index] = angle(Z)
    return OP_matrix
