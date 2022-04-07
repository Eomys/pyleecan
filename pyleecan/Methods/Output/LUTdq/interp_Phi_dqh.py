import numpy as np
import scipy.interpolate as scp_int


def interp_Phi_dqh(self, Id, Iq):
    """Get the magnets d-axis inductance

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
    Phi_dqh : ndarray
        interpolated flux in dqh frame (3)
    """

    # Compute interpolant at first call
    if self.Phi_dqh_interp is None:

        # Calculate average value of dqh flux linkage
        Phi_dqh_mean = self.get_Phidqh_mean()

        # Get unique Id, Iq sorted in ascending order
        OP_matrix = self.get_OP_matrix()
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
                            Phi_dqh_mean[ii, 0:2] + Phi_dqh_mean[jj, 0:2]
                        )
        else:
            is_rect_interp = False

        # Perform 2D interpolation
        if is_rect_interp:
            # regular grid interpolation
            self.Phi_dqh_interp = scp_int.RegularGridInterpolator(
                (XId, XIq), Phi_dqh_mean_reg, method="linear"
            )
        else:
            # scattered interpolation
            # not working since LinearNDInterpolator is not of same class as RegularGridInterpolator
            self.Phi_dqh_interp = scp_int.LinearNDInterpolator(
                (OP_matrix[:, 1], OP_matrix[:, 2]), Phi_dqh_mean[:, 0:2]
            )

    # Init dqh flux linkage
    if np.isscalar(Id) and np.isscalar(Iq):
        n_OP = 1
    else:
        n_OP = Id.size
    Phi_dqh = np.zeros((3, n_OP))

    # Interpolate Phid and Phiq, Phih is enforced to 0
    Phi_dqh_interp = self.Phi_dqh_interp((Id, Iq))
    if Phi_dqh_interp.ndim == 1:
        Phi_dqh_interp = Phi_dqh_interp[:, None]
    else:
        Phi_dqh_interp = Phi_dqh_interp.T
    Phi_dqh[0:2, :] = Phi_dqh_interp

    return Phi_dqh
