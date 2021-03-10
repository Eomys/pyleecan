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

    self.Id_ref = I0 * cos(Phi0)
    self.Iq_ref = I0 * sin(Phi0)
    if abs(self.Id_ref) < 1e-10:
        self.Id_ref = 0
    if abs(self.Iq_ref) < 1e-10:
        self.Iq_ref = 0
