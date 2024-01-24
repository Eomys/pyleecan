from numpy import reshape, meshgrid, pi, eye, matmul, tile

from ..Subdomain.comp_polynoms import E, P
from ..SubdomainModel.comp_interface_integrals import I_cni, I_sni, I_ckni, I_skni


def comp_interface_airgap(self):
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

    sdm = self.parent

    if sdm is None:
        raise Exception(
            "Cannot compute interface with airgap if Slot is not in a SubdomainModel"
        )

    cp = sdm.csts_position
    per_a = sdm.per_a
    is_antiper_a = sdm.is_antiper_a
    airgap = sdm.airgap

    v = self.k
    theta_i = self.center_angle
    n = airgap.k
    d = self.slot_width
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
    I_cosni, I_cosni_a = I_cni(d, ni, theta_in, per_a, is_antiper_a)
    I_sinni, I_sinni_a = I_sni(d, ni, theta_in, per_a, is_antiper_a)
    I_cosvcosni, I_cosvcosni_a = I_ckni(d, niv, vni, theta_ivn, per_a, is_antiper_a)
    I_cosvsinni, I_cosvsinni_a = I_skni(d, niv, vni, theta_ivn, per_a, is_antiper_a)

    E_ni_R3_R4, P_ni_R3_R4 = E(ni, R_3, R_4), P(ni, R_3, R_4)
    E_niv_R3_R4, P_niv_R3_R4 = E(niv.T, R_3, R_4), P(niv.T, R_3, R_4)
    E_vni_R4_R5, P_vni_R4_R5 = E(vni * pi / d, R_4, R_5), P(vni * pi / d, R_4, R_5)

    # Topological matrix
    # [zeros(N, N)  zeros(N, N)  eye(N, N)  zeros(N, N)  zeros(N, Zs0)  M16   ; ...
    #  zeros(N, N)  zeros(N, N)  zeros(N, N)  eye(N, N)  zeros(N, Zs0)  M26   ; ...
    #  M31'  M32'  M33'  M34'  eye(Zs0, Zs0)  zeros(Zs0, V*Zs0)   ; ...
    #  M41'  M42'  M43'  M44'  zeros(V*Zs0, Zs0)  eye(V*Zs0, V*Zs0)   ] ;
    sdm.mat[cp[2], cp[2]] = eye(N)
    sdm.mat[cp[2], cp[5]] = (
        -per_a / (R_4 * d) * I_cosvcosni_a * vni * E_vni_R4_R5 / P_vni_R4_R5
    )

    sdm.mat[cp[3], cp[3]] = eye(N)
    sdm.mat[cp[3], cp[5]] = (
        -per_a / (R_4 * d) * I_cosvsinni_a * vni * E_vni_R4_R5 / P_vni_R4_R5
    )

    sdm.mat[cp[4], cp[0]] = -2 * R_3 / d * I_cosni / (ni * E_ni_R3_R4)
    sdm.mat[cp[4], cp[1]] = -2 * R_3 / d * I_sinni / (ni * E_ni_R3_R4)
    sdm.mat[cp[4], cp[2]] = R_4 / d * I_cosni * P_ni_R3_R4 / (ni * E_ni_R3_R4)
    sdm.mat[cp[4], cp[3]] = R_4 / d * I_sinni * P_ni_R3_R4 / (ni * E_ni_R3_R4)
    sdm.mat[cp[4], cp[4]] = eye(Zs0)

    sdm.mat[cp[5], cp[0]] = -4 * R_3 / d * I_cosvcosni / (niv.T * E_niv_R3_R4)
    sdm.mat[cp[5], cp[1]] = -4 * R_3 / d * I_cosvsinni / (niv.T * E_niv_R3_R4)
    sdm.mat[cp[5], cp[2]] = (
        2 * R_4 / d * I_cosvcosni * P_niv_R3_R4 / (niv.T * E_niv_R3_R4)
    )
    sdm.mat[cp[5], cp[3]] = (
        2 * R_4 / d * I_cosvsinni * P_niv_R3_R4 / (niv.T * E_niv_R3_R4)
    )
    sdm.mat[cp[5], cp[5]] = eye(V * Zs0)

    # Source vector
    # Vect = [zeros(ntt, nblR) V1 V2 V3 zeros(ntt, Zs0*V)]
    Ji = self.Ji
    _, dX_R5, _, dXv_R5 = self.comp_current_solution(r=R_4)

    sdm.vect[cp[2], :] = per_a / pi * dX_R5 * matmul(I_cosni_a, Ji)
    sdm.vect[cp[3], :] = per_a / pi * dX_R5 * matmul(I_sinni_a, Ji)

    if self.Jik is not None:
        # If it is a concentrated winding
        # Harmonic component of stator slot current density
        Jiv = self.Jik
        Jiv_dXvi_R5 = Jiv * tile(dXv_R5, Zs0)[:, None]
        sdm.vect[cp[2], :] += per_a / pi * matmul(I_cosvcosni_a, Jiv_dXvi_R5)
        sdm.vect[cp[3], :] += per_a / pi * matmul(I_cosvsinni_a, Jiv_dXvi_R5)
