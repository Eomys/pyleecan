from numpy import angle


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

    if Id == 0 and Iq == 0:
        self.I0_ref = 0
        self.IPhi0_ref = 0
    else:
        Z = Id + 1j * Iq
        self.I0_ref = abs(Z)
        self.IPhi0_ref = angle(Z)
