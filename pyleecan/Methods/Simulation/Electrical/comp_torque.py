from numpy import pi


def comp_torque(self, out_dict, N0):
    """Compute the electrical average torque

    Parameters
    ----------
    self : Electrical
        an Electrical object
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_parameters of EEC
    """

    omega = 2 * pi * N0 / 60

    P = out_dict["Pem_av"]

    Tem_av = (P - out_dict["Pj_losses"]) / omega

    out_dict["Tem_av"] = Tem_av

    return out_dict
