def comp_joule_losses(self, out_dict, machine):
    """Compute the electrical Joule losses

    Parameters
    ----------
    self : Electrical
        an Electrical object
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_parameters of EEC
    machine : Machine
        a Machine object

    Returns
    ------
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in EEC
    """

    # TODO utilize loss models instead here
    # compute stator joule losses
    qs = machine.stator.winding.qs

    P_joule_s = qs * out_dict["eec_param"]["R1"] * abs(out_dict["eec_param"]["I1"]) ** 2

    P_joule_r = qs * out_dict["eec_param"]["R2"] * abs(out_dict["eec_param"]["I2"]) ** 2

    out_dict["Pj_losses"] = P_joule_s + P_joule_r

    return out_dict
