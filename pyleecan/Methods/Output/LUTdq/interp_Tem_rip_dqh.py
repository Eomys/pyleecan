import numpy as np
import scipy.interpolate as scp_int


def interp_Tem_rip_dqh(self, Id, Iq):
    """Interpolate torque ripple in dq plane

    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    Id : float or ndarray
        current Id
    Iq : float or ndarray
        current Iq

    Returns
    ----------
    Tem_rip_pp : float or ndarray
        interpolated flux in dqh frame (3)
    """

    if self.output_list[0].mag.Tem_rip_pp is None:
        return None

    # Get torque ripple for each operating point
    Tem_rip_pp_dqh = np.array([out.mag.Tem_rip_pp for out in self.output_list])

    # Get unique Id, Iq sorted in ascending order
    OP_matrix = self.get_OP_array("N0", "Id", "Iq")
    XId, jd = np.unique(OP_matrix[:, 1], return_inverse=True)
    XIq, jq = np.unique(OP_matrix[:, 2], return_inverse=True)
    nd, nq = XId.size, XIq.size

    Tem_rip_pp_dqh_reg = np.zeros((nd, nq))
    if nd * nq == OP_matrix.shape[0]:
        # sort flux linkage matrix and reshape to (nd, nq, 2)
        is_rect_interp = True
        for ii, (m, n) in enumerate(zip(jd, jq)):
            Tem_rip_pp_dqh_reg[m, n] = Tem_rip_pp_dqh[ii]
    else:
        is_rect_interp = False

    if nd == 1:
        # 1D interpolation along q axis
        Tem_rip_interp = scp_int.interp1d(
            XIq, Tem_rip_pp_dqh_reg, kind="linear", axis=1
        )
    elif nq == 1:
        # 1D interpolation along d axis
        Tem_rip_interp = scp_int.interp1d(
            XId, Tem_rip_pp_dqh_reg, kind="linear", axis=0
        )
    elif is_rect_interp:
        # 2D regular grid interpolation
        Tem_rip_interp = scp_int.RegularGridInterpolator(
            (XId, XIq), Tem_rip_pp_dqh_reg, method="linear"
        )
    else:
        # 2D scattered interpolation
        # not working since LinearNDInterpolator is not of same class as RegularGridInterpolator
        Tem_rip_interp = scp_int.LinearNDInterpolator(
            (OP_matrix[:, 1], OP_matrix[:, 2]), Tem_rip_pp_dqh
        )

    # Init dqh flux linkage
    if np.isscalar(Id) and np.isscalar(Iq):
        n_OP = 1
    else:
        n_OP = Id.size
    Tem_rip_pp = np.zeros(n_OP)

    if nd == 1:
        Tem_rip_pp = Tem_rip_interp(Iq)
    elif nq == 1:
        Tem_rip_pp = Tem_rip_interp(Id)
    else:
        Tem_rip_pp = Tem_rip_interp((Id, Iq))

    return Tem_rip_pp
