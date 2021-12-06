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

    if "Phid_mag" not in self.parameters:
        # Recalculate dqh flux due to permanent magnets
        Phi_dqh_mag = self.fluxlink.comp_fluxlinkage(machine)
        self.parameters["Phid_mag"] = float(Phi_dqh_mag[0])
        self.parameters["Phiq_mag"] = float(Phi_dqh_mag[1])

    Phid_mag = self.parameters["Phid_mag"]

    Tem_sync = qs * p * Phid_mag * Iq

    Tem_rel = qs * p * ((Phid - Phid_mag) * Iq - Phiq * Id)

    return Tem_sync, Tem_rel
