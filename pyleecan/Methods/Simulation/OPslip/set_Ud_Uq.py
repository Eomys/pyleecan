from numpy import angle


def set_Ud_Uq(self, Ud, Uq):
    """Set the value for Ud and Uq

    Parameters
    ----------
    self : OPdq
        An OPdq object
    Ud : float
        Ud value to set [Arms]
    Uq : float
        Uq value to set [Arms]
    """

    if Ud == 0 and Uq == 0:
        self.I0_ref = 0
        self.IPhi0_ref = 0
    else:
        Z = Ud + 1j * Uq
        self.I0_ref = abs(Z)
        self.IPhi0_ref = angle(Z)
