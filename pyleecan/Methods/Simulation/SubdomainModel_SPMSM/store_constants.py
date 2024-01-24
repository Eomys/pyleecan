from ....Functions.SubdomainModel.E import E
from ....Functions.SubdomainModel.P import P


def store_constants(self, Csts):
    """Method description

    Parameters
    ----------
    self: SubdomainModel_SPMSM
        a SubdomainModel_SPMSM object
    Csts: ndarray
        Array containing integration constants values over time

    """

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
