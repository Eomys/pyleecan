# -*- coding: utf-8 -*-


def comp_parameters(self, output):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance
    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """
    # for now do nothing, only direct user input

    pass

    """
    # Parameters to compute only once
    if "R20" not in self.parameters:
        self.parameters["R20"] = output.simu.machine.stator.comp_resistance_wind()
    if "phi" not in self.parameters:
        self.parameters["phi"] = self.fluxlink.comp_fluxlinkage(output)

    # Parameters which vary for each simulation
    self.parameters["Id"] = output.elec.Id_ref
    self.parameters["Iq"] = output.elec.Iq_ref
    (phid, phiq) = self.indmag.comp_inductance(output)
    if self.parameters["Id"] != 0:
        self.parameters["Ld"] = (phid - self.parameters["phi"]) / self.parameters["Id"]
    if self.parameters["Iq"] != 0:
        self.parameters["Lq"] = phiq / self.parameters["Iq"]
    self.parameters["Phid"] = phid
    self.parameters["Phiq"] = self.parameters["Lq"] * self.parameters["Iq"]
    """
