from numpy import diag, cos, sin

from ....Functions.SubdomainModel.E import E
from ....Functions.SubdomainModel.P import P


def comp_interface_airgap(self, angle_rotor):
    """Method description

    Parameters
    ----------
    self: Subdomain_MagnetSurface
        a Subdomain_MagnetSurface object

    """

    sdm = self.parent

    if sdm is None:
        raise Exception(
            "Cannot compute interface with airgap if MagnetSurface is not in a SubdomainModel"
        )

    cp = sdm.csts_position
    airgap = sdm.airgap

    mur = self.permeability_relative

    R_2 = self.Ryoke

    R_3 = airgap.Rrbo
    R_4 = airgap.Rsbo

    n = self.k

    E_n_R2_R3, P_n_R2_R3 = E(n, R_2, R_3), P(n, R_2, R_3)
    E_n_R3_R4, P_n_R3_R4 = E(n, R_3, R_4), P(n, R_3, R_4)

    # Fill topological matrix
    # Mat = [M1  zeros(N, N)  M2  zeros(N, N)   ; ...
    #    zeros(N, N)  M1  zeros(N, N)  M2   ] ;

    M1 = diag(1 + 1 / mur * P_n_R3_R4 * E_n_R2_R3 / (P_n_R2_R3 * E_n_R3_R4))
    M2 = diag(-2 * R_4 / (R_3 * mur) * E_n_R2_R3 / (P_n_R2_R3 * E_n_R3_R4))

    sdm.mat[cp[0], cp[0]] = M1
    sdm.mat[cp[0], cp[2]] = M2
    sdm.mat[cp[1], cp[1]] = M1
    sdm.mat[cp[1], cp[3]] = M2

    # Fill source vector
    # Vect = [V1 V2 zeros(ntt,nblS) ]'

    # Magnetization particular solution
    _, _, dX_n_R3, dY_n_R3 = self.comp_magnet_solution(R_3)

    dZ_n_R3 = dX_n_R3 * self.Mrn + (dY_n_R3 - 1) * self.Mtn

    ndelta = n[:, None] * angle_rotor[None, :]

    sdm.vect[cp[0], :] = 1 / mur * dZ_n_R3[:, None] * sin(ndelta)
    sdm.vect[cp[1], :] = -1 / mur * dZ_n_R3[:, None] * cos(ndelta)
