import numpy as np

from ..SubdomainModel.comp_interface_integrals import I_ckni, I_skni


def comp_interface_airgap_slot(self):
    """Method description

    Parameters
    ----------
    self: SdmSPMSM
        d SdmSPMSM object

    Returns
    ----------
    var: type
        var description
    """

    v = self.stator_slot.k
    theta_i = self.stator_slot.periodicity
    n = self.airgap.k
    d = self.stator_slot.angular_width
    R_3 = self.stator.

    N, V, Zs = n.size, v.size, i.size

    # Grid
    vni, niv, theta_ivn = np.meshgrid(v, n, theta_i)

    vni = np.reshape(vni, (N, V * Zs))
    niv = np.reshape(niv, (N, V * Zs))
    theta_ivn = np.reshape(theta_ivn, (N, V * Zs))

    # Interface integrals
    I_cosvcosni = I_ckni(d, niv, vni, theta_ivn)
    I_cosvsinni = I_skni(d, niv, vni, theta_ivn)

       
    # M31 = -2*R_3/d*I_cosni./(ni.*E_ni_R3_R4) ;
    # M32 = -2*R_3/d*I_sinni./(ni.*E_ni_R3_R4) ;
    # M33 = R_4/d*I_cosni.*P_ni_R3_R4./(ni.*E_ni_R3_R4) ;
    # M34 = R_4/d*I_sinni.*P_ni_R3_R4./(ni.*E_ni_R3_R4) ;
    
    # M41 = -4*R_3/d*I_cosvcosni./(niv.*E_niv_R3_R4) ;
    # M42 = -4*R_3/d*I_cosvsinni./(niv.*E_niv_R3_R4) ;
    # M43 = 2*R_4/d*I_cosvcosni.*P_niv_R3_R4./(niv.*E_niv_R3_R4)  ;
    # M44 = 2*R_4/d*I_cosvsinni.*P_niv_R3_R4./(niv.*E_niv_R3_R4) ;
    
    # if is_openingS == 0 %If there is no stator slot opening
    #     M16 = -gcd0/(R_4*d)*I_cosvcosni_a.*vni.*E_vni_R4_R5./P_vni_R4_R5 ;
    #     M26 = -gcd0/(R_4*d)*I_cosvsinni_a.*vni.*E_vni_R4_R5./P_vni_R4_R5 ;
    #     MatS = [zeros(N, N)  zeros(N, N)  eye(N, N)  zeros(N, N)  zeros(N, Zs0)  M16   ; ...
    #         zeros(N, N)  zeros(N, N)  zeros(N, N)  eye(N, N)  zeros(N, Zs0)  M26   ; ...
    #         M31'  M32'  M33'  M34'  eye(Zs0, Zs0)  zeros(Zs0, V*Zs0)   ; ...
    #         M41'  M42'  M43'  M44'  zeros(V*Zs0, Zs0)  eye(V*Zs0, V*Zs0)   ] ;
