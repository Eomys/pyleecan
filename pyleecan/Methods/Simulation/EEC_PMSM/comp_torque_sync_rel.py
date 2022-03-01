def comp_torque_sync_rel(self, eec_param, qs, p, machine=None):
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

    Id = eec_param["Id"]
    Iq = eec_param["Iq"]
    Phid = eec_param["Phid"]
    Phiq = eec_param["Phiq"]

    if "Phid_mag" not in eec_param:
        # Recalculate dqh flux due to permanent magnets
        Phi_dqh_mag = self.fluxlink.comp_fluxlinkage(machine)
        eec_param["Phid_mag"] = float(Phi_dqh_mag[0])
        eec_param["Phiq_mag"] = float(Phi_dqh_mag[1])

    Phid_mag = eec_param["Phid_mag"]

    Tem_sync = qs * p * Phid_mag * Iq

    Tem_rel = qs * p * ((Phid - Phid_mag) * Iq - Phiq * Id)

    return Tem_sync, Tem_rel
