def comp_Ld(self, OP_ref=None):
    """Compute the stator winding inductance along d-axis for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    OP_ref : OP
        reference OP object

    """

    if OP_ref is None:
        OP_ref = self.OP

    Id = OP_ref.get_Id_Iq()["Id"]
    if Id not in [None, 0]:
        if self.Phid is None:
            self.comp_Phidq()
        if self.Phid_mag is None:
            self.comp_Phidq_mag()
        self.Ld = (self.Phid - self.Phid_mag) / Id
    else:
        self.Ld = None
