def comp_Phidq_mag(self, OP_ref=None):
    """Compute the stator winding flux in open-circuit for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    OP_ref : OP
        reference OP object

    """

    if OP_ref is None:
        OP_ref = self.OP
    Phi_dqh_mag_mean = self.fluxlink.comp_fluxlinkage(
        machine=self.get_machine_from_parent()
    )

    self.Phid_mag = float(Phi_dqh_mag_mean[0])
    self.Phiq_mag = float(Phi_dqh_mag_mean[1])
