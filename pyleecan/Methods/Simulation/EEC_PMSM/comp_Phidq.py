def comp_Phidq(self, OP_ref=None):
    """Compute the stator winding flux for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    OP_ref : OP
        reference OP object

    """

    if OP_ref is None:
        OP_ref = self.OP
    Phi_dqh_mean = self.indmag.comp_inductance(
        machine=self.get_machine_from_parent(), OP_ref=OP_ref
    )

    Phid = Phi_dqh_mean[0]  # * self.Xke_skinS
    Phiq = Phi_dqh_mean[1]  # * self.Xke_skinS
    if Phid.size == 1:
        Phid = float(Phid)
        Phiq = float(Phiq)

    self.Phid = Phid
    self.Phiq = Phiq
