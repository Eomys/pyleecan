def get_param_dict(self):
    """Get the parameters dict for the ELUT of PMSM at the operationnal temperature and frequency
    Parameters
    ----------
    self : ELUT
        an ELUT_PMSM object

    Returns
    ----------
    param_dict : dict
        a Dict object
    """

    # getting parameters of the abstract class ELUT (stator parameters)
    param_dict = super(type(self), self).get_param_dict()

    param_dict["R2"] = self.R2
    param_dict["L2"] = self.L2

    param_dict["T2_ref"] = self.T2_ref

    param_dict["Phi_m"] = self.Phi_m

    param_dict["I_m"] = self.I_m

    return param_dict
