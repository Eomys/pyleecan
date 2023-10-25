from numpy import diag, eye, cos, sin, meshgrid

from ..Subdomain.comp_polynoms import E, P


def comp_interface_airgap_magnet(self, airgap, mat, vect, angle_rotor):
    """Method description

    Parameters
    ----------
    self: Subdomain_MagnetSurface
        a Subdomain_MagnetSurface object

    """

    mur = self.permeability_relative

    R_2 = self.Ryoke
    R_3 = airgap.Rrbo
    R_4 = airgap.Rsbo

    n = self.k

    E_n_R2_R3, P_n_R2_R3 = E(n, R_2, R_3), P(n, R_2, R_3)
    E_n_R3_R4, P_n_R3_R4 = E(n, R_3, R_4), P(n, R_3, R_4)

    M11 = eye(n.size) + 1 / mur * diag(P_n_R3_R4 * E_n_R2_R3 / (P_n_R2_R3 * E_n_R3_R4))
    M13 = -2 * R_4 / (R_3 * mur) * diag(E_n_R2_R3 / (P_n_R2_R3 * E_n_R3_R4))

    # Mat = [M11  zeros(N, N)  M13  zeros(N, N)   ; ...
    #    zeros(N, N)  M11  zeros(N, N)  M13   ] ;

    # Magnetization particular solution
    dX_n_r, dY_n_r = self.comp_magnet_solution(n, R_3, R_2, R_3)

    dZ_n_r = dX_n_r * self.Mrn + (dY_n_r - 1) * self.Mtn

    nt, tn = meshgrid(n, angle_rotor)
    ndelta = nt * tn

    V1 = 1 / mur * dZ_n_r[None, :] * sin(ndelta)
    V2 = -1 / mur * dZ_n_r[None, :] * cos(ndelta)

    # Vect = [V1 V2 zeros(ntt,nblS) ]' ; %Source vector
