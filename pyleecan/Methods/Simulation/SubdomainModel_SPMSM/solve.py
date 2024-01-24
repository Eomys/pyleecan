from numpy import zeros
from numpy.linalg import solve as np_solve

from ..Subdomain.comp_polynoms import E, P


def solve(self, angle, angle_rotor):
    """Method description

    Parameters
    ----------
    self: SubdomainModel_SPMSM
        a SubdomainModel_SPMSM object

    Returns
    ----------
    var: type
        var description
    """

    # Init topological matrix and source vector
    Nmat = sum(self.csts_number)
    self.mat = zeros((Nmat, Nmat))
    self.vect = zeros((Nmat, angle_rotor.size))

    # Build interface conditions between rotor and airgap
    self.rotor_magnet_surface.comp_interface_airgap(angle_rotor)

    # Build interface conditions between stator and airgap
    self.stator_slot.comp_interface_airgap()

    # Solve linear system
    Csts = np_solve(self.mat, self.vect)

    cp = self.csts_position

    # Airgap constants
    self.airgap.A = Csts[cp[0], :]
    self.airgap.C = Csts[cp[1], :]
    self.airgap.B = Csts[cp[2], :]
    self.airgap.D = Csts[cp[3], :]

    # Stator slots constants
    self.stator_slot.A = Csts[cp[4], :]
    self.stator_slot.B = Csts[cp[5], :]

    # Rebuild rotor surface magnet constants
    R_3 = self.airgap.Rrbo
    R_4 = self.airgap.Rsbo
    nt = self.airgap.k[:, None]
    P_nt_R3_R4, E_nt_R3_R4 = P(nt, R_3, R_4), E(nt, R_3, R_4)

    self.rotor_magnet_surface.A = R_3 * P_nt_R3_R4 * self.airgap.A / (
        nt * E_nt_R3_R4
    ) - 2 * R_4 * self.airgap.B / (nt * E_nt_R3_R4)

    self.rotor_magnet_surface.B = R_3 * P_nt_R3_R4 * self.airgap.C / (
        nt * E_nt_R3_R4
    ) - 2 * R_4 * self.airgap.D / (nt * E_nt_R3_R4)

    import numpy as np

    r = (R_3 + R_4) / 2

    n = self.airgap.k[:, None]
    P_n_r_R4 = (r / R_4) ** n + (R_4 / r) ** n
    P_n_r_R3 = (r / R_3) ** n + (R_3 / r) ** n
    E_n_r_R4 = (r / R_4) ** n - (R_4 / r) ** n
    E_n_r_R3 = (r / R_3) ** n - (R_3 / r) ** n
    E_n_R3_R4 = -((R_4 / R_3) ** n) + (R_3 / R_4) ** n

    cosn = np.cos(n * angle[None, :])
    sinn = np.sin(n * angle[None, :])

    # Fourier series of radial flux density
    Brg_sin = -(
        R_3 / r * self.airgap.A * P_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.airgap.B * P_n_r_R3 / E_n_R3_R4
    )
    Brg_cos = (
        R_3 / r * self.airgap.C * P_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.airgap.D * P_n_r_R3 / E_n_R3_R4
    )

    # Fourier series of tangential flux density
    Bthetag_cos = -(
        R_3 / r * self.airgap.A * E_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.airgap.B * E_n_r_R3 / E_n_R3_R4
    )
    Bthetag_sin = -(
        R_3 / r * self.airgap.C * E_n_r_R4 / E_n_R3_R4
        - R_4 / r * self.airgap.D * E_n_r_R3 / E_n_R3_R4
    )

    Bthetag = np.matmul(Bthetag_cos.T, cosn) + np.matmul(Bthetag_sin.T, sinn)

    Brg = np.matmul(Brg_cos.T, cosn) + np.matmul(Brg_sin.T, sinn)

    # import matplotlib.pyplot as plt

    # plt.figure()
    # plt.plot(angle, Brg[0, :], "k")
    # plt.plot(angle, Bthetag[0, :], "r")
    # plt.show()
