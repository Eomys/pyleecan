from numpy import reshape, meshgrid, pi, repmat, zeros

from ..Subdomain.comp_polynoms import E, P
from ..SubdomainModel.comp_interface_integrals import I_cni, I_sni, I_ckni, I_skni


def comp_interface_airgap(self, airgap, mat, vect, per_a, is_antiper_a):
    """Method description

    Parameters
    ----------
    self: Subdomain_Slot
        a Subdomain_Slot object

    Returns
    ----------
    var: type
        var description
    """

    v = self.k
    theta_i = self.center_angle
    n = airgap.k
    d = self.angular_width
    R_3 = airgap.Rrbo
    R_4 = airgap.Rsbo
    R_5 = self.Ryoke

    N, V, Zs0 = n.size, v.size, theta_i.size

    # Grid
    ni, theta_in = meshgrid(n, theta_i)
    vni, niv, theta_ivn = meshgrid(v, n, theta_i)
    vni = reshape(vni, (N, V * Zs0))
    niv = reshape(niv, (N, V * Zs0))
    theta_ivn = reshape(theta_ivn, (N, V * Zs0))

    # Interface integrals
    I_cosni = I_cni(d, ni, theta_in, per_a, is_antiper_a)
    I_sinni = I_sni(d, ni, theta_in, per_a, is_antiper_a)
    I_cosvcosni, I_cosvcosni_a = I_ckni(d, niv, vni, theta_ivn, per_a, is_antiper_a)
    I_cosvsinni, I_cosvsinni_a = I_skni(d, niv, vni, theta_ivn, per_a, is_antiper_a)

    E_ni_R3_R4, P_ni_R3_R4 = E(ni, R_3, R_4), P(ni, R_3, R_4)
    E_niv_R3_R4, P_niv_R3_R4 = E(niv, R_3, R_4), P(niv, R_3, R_4)
    E_vni_R4_R5, P_vni_R4_R5 = E(vni * pi / d, R_4, R_5), P(vni * pi / d, R_4, R_5)

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
    Ji = self.Ji
    X_R5, dX_R5, Xv_R5, dXv_R5 = self.comp_current_solution_SDM2D(r=R_4)

    V1 = per_a / pi * dX_R5 * Ji * I_cosni
    V2 = per_a / pi * dX_R5 * Ji * I_sinni

    if self.Jik is not None:
        # If it is a concentrated winding
        # Harmonic component of stator slot current density
        Jiv = self.Jiv
        dX_vni_R5 = repmat(dXv_R5, [N, Zs0])
        V1 = V1 + per_a / pi * Jiv * (dX_vni_R5 * I_cosvcosni)
        V2 = V2 + per_a / pi * Jiv * (dX_vni_R5 * I_cosvsinni)

    # Vect = [zeros(ntt, nblR) V1 V2 V3 zeros(ntt, Zs0*V)]
