def get_param_dict(self, OP=None, param_list=None, Id=None, Iq=None):
    """Get the parameters dict for the ELUT of PMSM
    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    OP : OP
        an OP object
    Id : float or ndarray
        current Id
    Iq : float or ndarray
        current Iq

    Returns
    ----------
    param_dict : dict
        a Dict object
    """

    if OP is not None:
        Id, Iq = OP.get_Id_Iq()["Id"], OP.get_Id_Iq()["Iq"]
    elif Id is None or Iq is None:
        raise Exception("Cannot get parameters dict if OP is None and Id or Iq is None")

    if param_list is None:
        param_list = ["Idqh", "Ldqh"]

    param_dict = dict()
    Phi_dqh = None

    if "Idqh" in param_list:
        param_dict["Id"] = Id
        param_dict["Iq"] = Iq

    if "Phidqh" in param_list:
        Phi_dqh = self.interp_Phi_dqh(Id=Id, Iq=Iq)
        param_dict["Phid"] = Phi_dqh[0]
        param_dict["Phiq"] = Phi_dqh[1]
        param_dict["phi"] = self.get_Phidqh_mag_mean()[0]

    if "Ldqh" in param_list:
        Ldqh = self.get_Ldqh(Id=Id, Iq=Iq, Phi_dqh=Phi_dqh)[:, 0]
        param_dict["Ld"] = Ldqh[0]
        param_dict["Lq"] = Ldqh[1]

    return param_dict
