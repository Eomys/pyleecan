# -*- coding: utf-8 -*-

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

    P = out_dict["Pem_av_ref"]

    Tem_av_ref = (P - out_dict["Pj_losses"]) / omega

    out_dict["Tem_av_ref"] = Tem_av_ref

    return out_dict
