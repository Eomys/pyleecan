import numpy as np

from ..Subdomain.comp_polynoms import E, P
from ..SubdomainModel.comp_interface_integrals import I_cni, I_sni, I_ckni, I_skni


def comp_interface_airgap(self, mat, vect):
    """Method description

    Parameters
    ----------
    self: Subdomain_Slot
        d Subdomain_Slot object

    Returns
    ----------
    var: type
        var description
    """

    per_a = self.per_a
    is_antiper_a = self.is_antiper_a
    v = self.stator_slot.k
    theta_i = self.stator_slot.center_angle
    n = self.airgap.k
    d = self.stator_slot.angular_width
    R_3 = self.airgap.Rrbo
    R_4 = self.airgap.Rsbo
    R_5 = self.stator_slot.Ryoke

    N, V, Zs0 = n.size, v.size, theta_i.size

    # Grid
    ni, theta_in = np.meshgrid(n, theta_i)
    vni, niv, theta_ivn = np.meshgrid(v, n, theta_i)
    vni = np.reshape(vni, (N, V * Zs0))
    niv = np.reshape(niv, (N, V * Zs0))
    theta_ivn = np.reshape(theta_ivn, (N, V * Zs0))

    # Interface integrals
    I_cosni = I_cni(d, ni, theta_in, is_antiper_a, per_a)
    I_sinni = I_sni(d, ni, theta_in, is_antiper_a, per_a)
    I_cosvcosni, I_cosvcosni_a = I_ckni(d, niv, vni, theta_ivn, is_antiper_a, per_a)
    I_cosvsinni, I_cosvsinni_a = I_skni(d, niv, vni, theta_ivn, is_antiper_a, per_a)

    E_ni_R3_R4, P_ni_R3_R4 = E(ni, R_3, R_4), P(ni, R_3, R_4)
    E_niv_R3_R4, P_niv_R3_R4 = E(niv, R_3, R_4), P(niv, R_3, R_4)
    E_vni_R4_R5, P_vni_R4_R5 = E(vni * np.pi / d, R_4, R_5), P(
        vni * np.pi / d, R_4, R_5
    )

    # Topological matrix
    M31 = -2 * R_3 / d * I_cosni / (ni * E_ni_R3_R4)
    M32 = -2 * R_3 / d * I_sinni / (ni * E_ni_R3_R4)
    M33 = R_4 / d * I_cosni * P_ni_R3_R4 / (ni * E_ni_R3_R4)
    M34 = R_4 / d * I_sinni * P_ni_R3_R4 / (ni * E_ni_R3_R4)

    M41 = -4 * R_3 / d * I_cosvcosni / (niv * E_niv_R3_R4)
    M42 = -4 * R_3 / d * I_cosvsinni / (niv * E_niv_R3_R4)
    M43 = 2 * R_4 / d * I_cosvcosni * P_niv_R3_R4 / (niv * E_niv_R3_R4)
    M44 = 2 * R_4 / d * I_cosvsinni * P_niv_R3_R4 / (niv * E_niv_R3_R4)

    M16 = -per_a / (R_4 * d) * I_cosvcosni_a * vni * E_vni_R4_R5 / P_vni_R4_R5
    M26 = -per_a / (R_4 * d) * I_cosvsinni_a * vni * E_vni_R4_R5 / P_vni_R4_R5

    #     MatS = [zeros(N, N)  zeros(N, N)  eye(N, N)  zeros(N, N)  zeros(N, Zs0)  M16   ; ...
    #         zeros(N, N)  zeros(N, N)  zeros(N, N)  eye(N, N)  zeros(N, Zs0)  M26   ; ...
    #         M31'  M32'  M33'  M34'  eye(Zs0, Zs0)  zeros(Zs0, V*Zs0)   ; ...
    #         M41'  M42'  M43'  M44'  zeros(V*Zs0, Zs0)  eye(V*Zs0, V*Zs0)   ] ;

    # Source vector

    # [X_R5, dX_R5, ~, dXv_R5] = comp_current_solution_SDM2D(sdm, v, R_5, R_5, R_6, d) ;

    # V1 = gcd0/pi*dX_R5*Ji*I_cosni' ;
    # V2 = gcd0/pi*dX_R5*Ji*I_sinni' ;

    # if Nlay_tan1 == 2 %If it is a concentrated winding
    #     Jiv = sdm.Jiv ; % Harmonic component of stator slot current density
    #     if is_antisyma
    #         I_cosvcosni = sdm_temp.I_cosvcosni_a ;
    #         I_cosvsinni = sdm_temp.I_cosvsinni_a ;
    #     else
    #         I_cosvcosni = sdm_temp.I_cosvcosni ;
    #         I_cosvsinni = sdm_temp.I_cosvsinni ;

    #     dX_vni_R5 = repmat(dXv_R5, [N, Zs0]) ;
    #     V1 = V1 + gcd0/pi*Jiv*(dX_vni_R5.*I_cosvcosni)' ;
    #     V2 = V2 + gcd0/pi*Jiv*(dX_vni_R5.*I_cosvsinni)' ;
