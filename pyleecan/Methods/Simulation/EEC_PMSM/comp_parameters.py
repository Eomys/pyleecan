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

    # Parameters to compute only once
    if "R20" not in self.parameters:
        self.parameters["R20"] = output.simu.machine.stator.comp_resistance_wind()
    if "phi" not in self.parameters:
        self.parameters["phi"] = self.fluxlink.comp_fluxlinkage(output)

    # Parameters which may vary for each simulation
    is_comp_ind = False
    # check for complete parameter set 
    # (there may be some redundancy here but it seems simplier to implement)
    if not all (k in self.parameters for k in ("Phid", "Phiq", "Ld", "Lq")):
        is_comp_ind = True
    
    # check for d- and q-current (change)
    if "Id" not in self.parameters or self.parameters["Id"] != output.elec.Id_ref:
        self.parameters["Id"] = output.elec.Id_ref
        is_comp_ind = True

    if "Iq" not in self.parameters or self.parameters["Iq"] != output.elec.Iq_ref:
        self.parameters["Iq"] = output.elec.Iq_ref
        is_comp_ind = True

    # compute inductance if nessessary
    if is_comp_ind:
        (phid, phiq) = self.indmag.comp_inductance(output)
        if self.parameters["Id"] != 0:
            self.parameters["Ld"] = (phid - self.parameters["phi"]) / self.parameters[
                "Id"
            ]
        else:
            self.parameters["Ld"] = None # to have the parameters complete though
        
        if self.parameters["Iq"] != 0:
            self.parameters["Lq"] = phiq / self.parameters["Iq"]
        else:
            self.parameters["Lq"] = None # to have the parameters complete though
        
        self.parameters["Phid"] = phid
        self.parameters["Phiq"] = phiq
