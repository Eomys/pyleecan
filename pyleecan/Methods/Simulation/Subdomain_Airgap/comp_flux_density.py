from numpy import cos, sin, matmul

from ....Functions.SubdomainModel.E import E
from ....Functions.SubdomainModel.P import P


def comp_flux_density(self, r, angle):
    """Method description

    Parameters
    ----------
    self: Subdomain_Airgap
        a Subdomain_Airgap object
    r : float/array
        Radius/Radii at which flux density is calculated
    angle : array
        Angular values at which flux density is calculated

    Returns
    ----------
    Brg: ndarray
        Radial airgap flux density
    Bthetag: ndarray
        Circumferential airgap flux density
    """

    R_3 = self.Rrbo
    R_4 = self.Rsbo

    n = self.k[:, None]
    P_n_r_R4, P_n_r_R3 = P(n, r, R_4), P(n, r, R_3)
    E_n_r_R4, E_n_r_R3 = E(n, r, R_4), E(n, r, R_3)
    E_n_R3_R4 = E(n, R_3, R_4)

    cosn = cos(n * angle[None, :])
    sinn = sin(n * angle[None, :])

    # Fourier series of radial flux density
    Brg_sin = -(
        R_3 / r * self.A * P_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.B * P_n_r_R3 / E_n_R3_R4
    )
    Brg_cos = (
        R_3 / r * self.C * P_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.D * P_n_r_R3 / E_n_R3_R4
    )

    # Fourier series of tangential flux density
    Bthetag_cos = -(
        R_3 / r * self.A * E_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.B * E_n_r_R3 / E_n_R3_R4
    )
    Bthetag_sin = -(
        R_3 / r * self.C * E_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.D * E_n_r_R3 / E_n_R3_R4
    )

    Bthetag = matmul(Bthetag_cos.T, cosn) + matmul(Bthetag_sin.T, sinn)

    Brg = matmul(Brg_cos.T, cosn) + matmul(Brg_sin.T, sinn)

    return Brg, Bthetag
