from numpy import diag, eye

from ..Subdomain.comp_polynoms import E, P


def comp_interface_airgap_magnet(self, mat, vect):
    """Method description

    Parameters
    ----------
    self: Subdomain_MagnetSurface
        a Subdomain_MagnetSurface object

    """

    mur = self.permeability_relative

    R_3 = self.airgap.Rrbo
    R_4 = self.airgap.Rsbo

    n = self.k

    E_n_R2_R3, P_n_R2_R3 = E(n, R_3, R_4), P(n, R_3, R_4)
    E_n_R3_R4, P_n_R3_R4 = E(n, R_3, R_4), P(n, R_3, R_4)

    M11 = eye(n.size) + 1 / mur * diag(P_n_R3_R4 * E_n_R2_R3 / (P_n_R2_R3 * E_n_R3_R4))
    M13 = -2 * R_4 / (R_3 * mur) * diag(E_n_R2_R3 / (P_n_R2_R3 * E_n_R3_R4))

    # Mat = [M11  zeros(N, N)  M13  zeros(N, N)   ; ...
    #    zeros(N, N)  M11  zeros(N, N)  M13   ] ;
