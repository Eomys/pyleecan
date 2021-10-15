# -*- coding: utf-8 -*-


def comp_joule_losses(self, out_dict, machine):
    """Compute the electrical Joule losses

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_parameters of EEC
    """

    qs = machine.stator.winding.qs
    Id, Iq = out_dict["Id"], out_dict["Iq"]
    R = self.parameters["R20"]

    # Id and Iq are in RMS
    Pj_losses = qs * R * (Id ** 2 + Iq ** 2)

    out_dict["Pj_losses"] = Pj_losses

    return out_dict
