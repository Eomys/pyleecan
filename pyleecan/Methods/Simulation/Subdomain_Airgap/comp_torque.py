from numpy import pi, sum as np_sum

from ....Functions.SubdomainModel.E import E
from ....Functions.SubdomainModel.P import P


def comp_torque(self):
    """Method description

    Parameters
    ----------
    self: Subdomain_Airgap
        a Subdomain_Airgap object

    Returns
    ----------
    var: type
        var description
    """

    mu0 = 4 * pi * 1e-7

    R_3 = self.Rrbo
    R_4 = self.Rsbo

    L = self.parent.machine_polar_eq.rotor.L1

    r = (R_3 + R_4) / 2

    n = self.k[:, None]
    P_n_r_R4, P_n_r_R3 = P(n, r, R_4), P(n, r, R_3)
    E_n_r_R4, E_n_r_R3 = E(n, r, R_4), E(n, r, R_3)
    E_n_R3_R4 = E(n, R_3, R_4)

    W_n = (
        -R_3 / r * self.A * P_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.B * P_n_r_R3 / E_n_R3_R4
    )

    X_n = (
        -R_3 / r * self.C * E_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.D * E_n_r_R3 / E_n_R3_R4
    )

    Y_n = (
        R_3 / r * self.C * P_n_r_R4 / E_n_R3_R4
        + R_4 / r * self.D * P_n_r_R3 / E_n_R3_R4
    )

    Z_n = (
        -R_3 / r * self.A * E_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.B * E_n_r_R3 / E_n_R3_R4
    )

    Tem = pi * L * r**2 / mu0 * np_sum(W_n * X_n + Y_n * Z_n, axis=0)

    return Tem
