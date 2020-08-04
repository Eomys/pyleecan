from ....Functions.Electrical.coordinate_transformation import ab2dq
from numpy import pi, sin, linspace, zeros, mean


def set_Id_Iq(self, I0, Phi0):
    """Set Id_ref and Iq_ref according to I0, Phi0
    """

    time = linspace(0, 1, 100)
    Iab = zeros((100, 3))
    Iab[:, 0] = I0 * sin(time + Phi0)
    Iab[:, 1] = I0 * sin(time + Phi0 + 2 * pi / 3)
    Iab[:, 2] = I0 * sin(time + Phi0 + 4 * pi / 3)
    Idq = ab2dq(Iab, linspace(0, 2 * pi, 2048))
    self.Id_ref = mean(Idq[:, 0])
    self.Iq_ref = mean(Idq[:, 1])
