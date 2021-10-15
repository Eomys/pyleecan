# -*- coding: utf-8 -*-


def comp_power(self, out_dict, machine):
    """Compute the electrical average power

    Parameters
    ----------
    self : Electrical
        an Electrical object
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_parameters of EEC
    """

    qs = machine.stator.winding.qs
    Id, Iq = out_dict["Id"], out_dict["Iq"]
    Ud, Uq = out_dict["Ud"], out_dict["Uq"]

    # All quantities are in RMS
    Pem_av_ref = qs * (Ud * Id + Uq * Iq)

    out_dict["Pem_av_ref"] = Pem_av_ref
