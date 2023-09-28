from numpy import cos, sin


def set_Ud_Uq(self, U0, Phi0):
    """Set Ud_ref and Uq_ref according to U0, Phi0

    Parameters
    ----------
    self : InputVoltage
        An InputVoltage object
    U0 : float
        Voltage amplitude [Arms]
    Phi0 : float
        Voltage phase [rad]
    """

    self.OP.Ud_ref = U0 * cos(Phi0)
    self.OP.Uq_ref = U0 * sin(Phi0)
    if abs(self.OP.Ud_ref) < 1e-10:
        self.OP.Ud_ref = 0
    if abs(self.OP.Uq_ref) < 1e-10:
        self.OP.Uq_ref = 0
