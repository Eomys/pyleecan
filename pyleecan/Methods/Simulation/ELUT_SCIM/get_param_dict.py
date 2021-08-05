from numpy import interp


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

    param_dict["Rr"] = self.Rr
    param_dict["Lr"] = self.Lr

    param_dict["Trot_ref"] = self.Trot_ref

    param_dict["Phi_m"] = self.Phi_m

    param_dict["I_m"] = self.I_m

    return param_dict
