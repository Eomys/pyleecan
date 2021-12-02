def set_Ud_Uq(self, Ud, Uq):
    """Set the value for Ud and Uq

    Parameters
    ----------
    self : OPdq
        An OPdq object
    Ud : float
        Ud value to set [Vrms]
    Uq : float
        Uq value to set [Vrms]
    """

    self.Ud_ref = Ud
    self.Uq_ref = Uq
