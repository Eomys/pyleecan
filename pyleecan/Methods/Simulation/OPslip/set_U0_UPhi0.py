def set_U0_UPhi0(self, U0, UPhi0):
    """Set the value for I0 and IPhi0

    Parameters
    ----------
    self : OPslip
        An OPslip object
    U0 : float
        U0 value to set [Arms]
    UPhi0 : float
        UPhi0 value to set [rad]
    """

    self.U0_ref = U0
    self.UPhi0_ref = UPhi0
