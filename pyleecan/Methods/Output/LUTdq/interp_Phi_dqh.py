import numpy as np
import scipy.interpolate as scp_int


def interp_Phi_dqh(self, Id, Iq):
    """Interpolate stator winding dqh flux in dq plane

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
    Phi_dqh : float or ndarray
        interpolated flux in dqh frame (3)
    """

    # Calculate average value of dqh flux linkage
    Phi_dqh_mean = self.get_Phi_dqh_mean()

    # Get unique Id, Iq sorted in ascending order
    OP_matrix = self.get_OP_array("N0", "Id", "Iq")
    XId, jd = np.unique(OP_matrix[:, 1], return_inverse=True)
    XIq, jq = np.unique(OP_matrix[:, 2], return_inverse=True)
    nd, nq = XId.size, XIq.size

    Phi_dqh_mean_reg = np.zeros((nd, nq, 2))
    if nd * nq == OP_matrix.shape[0]:
        # sort flux linkage matrix and reshape to (nd, nq, 2)
        is_rect_interp = True
        for ii, (m, n) in enumerate(zip(jd, jq)):
            Phi_dqh_mean_reg[m, n, :] = Phi_dqh_mean[ii, 0:2]
    elif nd + nq - 1 == OP_matrix.shape[0]:
        # Rebuild 2D grid from xId and xIq
        is_rect_interp = True
        Phi_dqh_mag = self.get_Phi_dqh_mag_mean()
        for m, x in enumerate(XId):
            for n, y in enumerate(XIq):
                # Find indice of current Id value in OP_matrix
                ii = np.where(OP_matrix[:, 1] == x)[0]
                # Find indice of current Iq value in OP_matrix
                jj = np.where(OP_matrix[:, 2] == y)[0]
                # check if (Id, Iq) is in OP_matrix
                kk = np.intersect1d(ii, jj)
                if kk.size > 0:
                    # take values directly from Phi_dqh_mean if (Id, Iq) is in OP_matrix
                    Phi_dqh_mean_reg[m, n, :] = Phi_dqh_mean[kk, 0:2]
                else:
                    # Sum flux values for (Id, Iq): Phi_dq(Id, Iq) = Phi_dq(Id, 0) + Phi_dq(0, Iq)
                    Phi_dqh_mean_reg[m, n, :] = (
                        Phi_dqh_mean[ii, :2] + Phi_dqh_mean[jj, :2] - Phi_dqh_mag[:2]
                    )
    else:
        is_rect_interp = False

    if nd == 1:
        # 1D interpolation along q axis
        Phi_dqh_interp = scp_int.interp1d(XIq, Phi_dqh_mean_reg, kind="linear", axis=1)
    elif nq == 1:
        # 1D interpolation along d axis
        Phi_dqh_interp = scp_int.interp1d(XId, Phi_dqh_mean_reg, kind="linear", axis=0)
    elif is_rect_interp:
        # 2D regular grid interpolation
        Phi_dqh_interp = scp_int.RegularGridInterpolator(
            (XId, XIq), Phi_dqh_mean_reg, method="linear"
        )
    else:
        # 2D scattered interpolation
        Phi_dqh_interp = scp_int.LinearNDInterpolator(
            (OP_matrix[:, 1], OP_matrix[:, 2]), Phi_dqh_mean[:, 0:2]
        )

    # Init dqh flux linkage
    if np.isscalar(Id) and np.isscalar(Iq):
        n_OP = 1
    else:
        n_OP = Id.size
    Phi_dqh = np.zeros((3, n_OP))

    if nd == 1:
        Phi_dqh[0:2, :] = np.squeeze(Phi_dqh_interp(Iq)).T
    elif nq == 1:
        Phi_dqh[0:2, :] = np.squeeze(Phi_dqh_interp(Id)).T
    else:
        Phid_dqh_val = Phi_dqh_interp((Id, Iq))
        # Interpolate Phid and Phiq, Phih is enforced to 0
        if n_OP == 1:
            Phi_dqh[0:2, :] = Phid_dqh_val[:, None]
        else:
            Phi_dqh[0:2, :] = Phid_dqh_val.T

    return Phi_dqh
