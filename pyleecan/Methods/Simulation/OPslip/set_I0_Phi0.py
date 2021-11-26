from numpy import exp


def set_I0_Phi0(self, I0, Phi0):
    """Set the value for I0 and IPhi0

    Parameters
    ----------
    self : OPslip
        An OPslip object
    I0 : float
        I0 value to set [Arms]
    Phi0 : float
        IPhi0 value to set [rad]
    """

    self.I0_ref = I0
    self.IPhi0_ref = Phi0
