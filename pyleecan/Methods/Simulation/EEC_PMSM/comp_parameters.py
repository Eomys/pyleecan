# -*- coding: utf-8 -*-


def comp_parameters(self, output):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance and back electromotive force
    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """
    # TODO maybe set currents to small value if I is 0 to compute inductance

    PAR = self.parameters

    # Parameters to compute only once
    if "R20" not in PAR:
        PAR["R20"] = output.simu.machine.stator.comp_resistance_wind()
    if "phi" not in PAR:
        PAR["phi"] = self.fluxlink.comp_fluxlinkage(output)

    # Parameters which may vary for each simulation
    is_comp_ind = False
    # check for complete parameter set
    # (there may be some redundancy here but it seems simplier to implement)
    if not all(k in PAR for k in ("Phid", "Phiq", "Ld", "Lq")):
        is_comp_ind = True

    # check for d- and q-current (change)
    if "Id" not in PAR or PAR["Id"] != output.elec.Id_ref:
        PAR["Id"] = output.elec.Id_ref
        is_comp_ind = True

    if "Iq" not in PAR or PAR["Iq"] != output.elec.Iq_ref:
        PAR["Iq"] = output.elec.Iq_ref
        is_comp_ind = True

    # compute inductance if necessary
    if is_comp_ind:
        (phid, phiq) = self.indmag.comp_inductance(output)
        if PAR["Id"] != 0:
            PAR["Ld"] = (phid - PAR["phi"]) / PAR["Id"]
        else:
            PAR["Ld"] = None  # to have the parameters complete though

        if PAR["Iq"] != 0:
            PAR["Lq"] = phiq / PAR["Iq"]
        else:
            PAR["Lq"] = None  # to have the parameters complete though

        PAR["Phid"] = phid
        PAR["Phiq"] = phiq
