def comp_torque_sync_rel(self):
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

    machine = self.get_machine_from_parent()
    qs = machine.stator.winding.qs
    p = machine.get_pole_pair_number()

    Id = self.OP.get_Id_Iq()["Id"]
    Iq = self.OP.get_Id_Iq()["Iq"]
    Phid = self.Phid
    Phiq = self.Phiq

    if self.Phid_mag is None:
        # Recalculate dqh flux due to permanent magnets
        self.comp_Phidq_mag()

    Phid_mag = self.Phid_mag

    Tem_sync = qs * p * Phid_mag * Iq

    Tem_rel = qs * p * ((Phid - Phid_mag) * Iq - Phiq * Id)

    return Tem_sync, Tem_rel
