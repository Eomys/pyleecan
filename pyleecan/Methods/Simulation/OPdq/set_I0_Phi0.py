from numpy import exp


def set_I0_Phi0(self, I0, Phi0):
    """Set the value for I0 and IPhi0

    Parameters
    ----------
    self : OPdq
        An OPdq object
    I0 : float
        I0 value to set [Arms]
    Phi0 : float
        IPhi0 value to set [rad]
    """

    if I0 == 0:
        self.Id_ref = 0
        self.Iq_ref = 0
    else:
        Z = I0 * exp(1j * Phi0)
        self.Id_ref = Z.real
        self.Iq_ref = Z.imag
