from numpy import interp


def get_param_dict(self, OP):
    """Get the parameters dict for the ELUT of PMSM
    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    OP : OP
        an OP object

    Returns
    ----------
    param_dict : dict
        a Dict object
    """

    param_dict = dict()
    Id, Iq = OP.get_Id_Iq()["Id"], OP.get_Id_Iq()["Iq"]
    param_dict["Ld"] = self.get_Ld(Id=Id, Iq=Iq)
    param_dict["Lq"] = self.get_Lq(Id=Id, Iq=Iq)
    param_dict["Id"] = Id
    param_dict["Iq"] = Iq

    return param_dict
