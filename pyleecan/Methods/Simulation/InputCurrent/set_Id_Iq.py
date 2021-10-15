from numpy import cos, sin


def set_Id_Iq(self, I0, Phi0):
    """Set Id_ref and Iq_ref according to I0, Phi0

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    I0 : float
        Current amplitude [Arms]
    Phi0 : float
        Current phase [rad]
    """

    self.OP.Id_ref = I0 * cos(Phi0)
    self.OP.Iq_ref = I0 * sin(Phi0)
    if abs(self.OP.Id_ref) < 1e-10:
        self.OP.Id_ref = 0
    if abs(self.OP.Iq_ref) < 1e-10:
        self.OP.Iq_ref = 0
