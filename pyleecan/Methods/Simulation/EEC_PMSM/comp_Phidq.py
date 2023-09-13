def comp_Phidq(self):
    """Compute and set the stator winding flux for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object

    """
    Phid, Phiq = None, None
    Idq_dict = self.OP.get_Id_Iq()

    if Idq_dict["Id"] is not None and Idq_dict["Iq"] is not None:
        if self.Ld is not None and self.Phid_mag is not None:
            # Calculate Phid from available data
            Phid = self.Ld * Idq_dict["Id"] + self.Phid_mag

        if self.Lq is not None and self.Phiq_mag is not None:
            # Calculate Phiq from available data
            Phiq = self.Lq * Idq_dict["Iq"] + self.Phiq_mag

        if Phid is None or Phiq is None:
            # Calculate Phid and Phiq for the given Id/Iq
            Phi_dqh_mean = self.comp_fluxlinkage(OP=self.OP)[0]

        if Phid is None:
            Phid = Phi_dqh_mean[0]  # * self.Xke_skinS

        if Phiq is None:
            Phiq = Phi_dqh_mean[1]  # * self.Xke_skinS

    self.Phid = Phid
    self.Phiq = Phiq
