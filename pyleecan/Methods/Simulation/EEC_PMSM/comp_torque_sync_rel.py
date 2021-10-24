def comp_torque_sync_rel(self, qs, p, machine=None):
    """Calculate synchronous and reluctant torque

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    qs: int
        Number of stator winding phase
    p: int
        Number of pole pairs

    Returns
    ------
    Tem_sync : float or ndarray
        Synchronous torque [N.m]
    Tem_rel : float or ndarray
        Reluctant torque [N.m]
    """

    Id = self.parameters["Id"]
    Iq = self.parameters["Iq"]
    Phid = self.parameters["Phid"]
    Phiq = self.parameters["Phiq"]
    if "phi" not in self.parameters:
        self.parameters["phi"] = self.fluxlink.comp_fluxlinkage(machine)
    phi_mag = self.parameters["phi"]

    Tem_sync = qs * p * phi_mag * Iq

    Tem_rel = qs * p * ((Phid - phi_mag) * Iq - Phiq * Id)

    return Tem_sync, Tem_rel
