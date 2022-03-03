from numpy import exp


def set_U0_UPhi0(self, U0, UPhi0):
    """Set the value for U0 and UPhi0
    Parameters
    ----------
    self : OPdq
        An OPdq object
    U0 : float
        U0 value to set [Arms]
    UPhi0 : float
        UPhi0 value to set [rad]
    """

    if U0 == 0:
        self.Ud_ref = 0
        self.Uq_ref = 0
    else:
        Z = U0 * exp(1j * UPhi0)
        self.Ud_ref = Z.real
        self.Uq_ref = Z.imag
