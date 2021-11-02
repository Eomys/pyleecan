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
        XId, jd = np.unique(self.OP_matrix[:, 1], return_inverse=True)
        XIq, jq = np.unique(self.OP_matrix[:, 2], return_inverse=True)
        nd, nq = XId.size, XIq.size

        # Perform 2D interpolation
        if nd * nq == self.OP_matrix.shape[0]:
            # sort flux linkage matrix and reshape to (nd, nq, 2)
            Phi_dqh_mean_reg = np.zeros((nd, nq, 2))
            for ii, (m, n) in enumerate(zip(jd, jq)):
                Phi_dqh_mean_reg[m, n, :] = Phi_dqh_mean[ii, 0:2]
            # regular grid interpolation
            self.Phi_dqh_interp = scp_int.RegularGridInterpolator(
                (XId, XIq),
                Phi_dqh_mean_reg,
                method="linear",
            )
        else:
            # scattered interpolation
            # not working since LinearNDInterpolator is not of same class as RegularGridInterpolator
            self.Phi_dqh_interp = scp_int.LinearNDInterpolator(
                (self.OP_matrix[:, 1], self.OP_matrix[:, 2]), Phi_dqh_mean[:, 0:2]
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
