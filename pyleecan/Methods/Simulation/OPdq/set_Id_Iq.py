def set_Id_Iq(self, Id, Iq):
    """Set the value for Id and Iq

    Parameters
    ----------
    self : OPdq
        An OPdq object
    Id : float
        Id value to set [Arms]
    Iq : float
        Iq value to set [Arms]
    """

    self.Id_ref = Id
    self.Iq_ref = Iq
