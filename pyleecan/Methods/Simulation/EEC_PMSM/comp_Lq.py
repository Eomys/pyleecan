def comp_Lq(self, OP_ref=None):
    """Compute the stator winding inductance along q-axis for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    OP_ref : OP
        reference OP object

    """

    if OP_ref is None:
        OP_ref = self.OP

    Iq = OP_ref.get_Id_Iq()["Iq"]
    if Iq not in [None, 0]:
        if self.Phiq is None:
            self.comp_Phidq()
        if self.Phiq_mag is None:
            self.comp_Phidq_mag()
        self.Lq = (self.Phiq - self.Phiq_mag) / Iq
    else:
        self.Lq = None
