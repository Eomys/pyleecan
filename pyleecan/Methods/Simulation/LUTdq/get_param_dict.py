from numpy import interp


def get_param_dict(self):
    """Get the parameters dict for the ELUT of PMSM at the operationnal temperature and frequency
    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    param_dict : dict
        a Dict object
    """

    # getting parameters of the abstract class ELUT (stator parameters)
    param_dict = super(type(self), self).get_parameters(Tsta=Tsta, felec=felec)

    Brm20 = self.magnet_0.mat_type.mag.Brm20
    alpha_Br = self.magnet_0.mat_type.mag.alpha_Br

    # back emf [V] update with temperature
    if Tmag is None:
        E0_temp = self.E0
    else:
        Tmag_ref = self.Tmag_ref
        E0_temp = self.E0 * (1 + alpha_Br * (Tmag - Tmag_ref))

    param_dict["E0"] = E0_temp

    return param_dict
