import numpy as np
import scipy.interpolate as scp_int


def get_Ploss_dqh_interp(self, N0):
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

    p = self.simu.machine.get_pole_pair_number()

    felec = N0 / 60 * p

    Ploss_dqh = np.zeros((len(self.output_list), 5))
    for ii, out in enumerate(self.output_list):
        Ploss_dqh[ii, 0] = out.loss.get_loss_group("stator winding joule", felec)
        Ploss_dqh[ii, 1] = out.loss.get_loss_group("stator core", felec)
        Ploss_dqh[ii, 2] = out.loss.get_loss_group("rotor magnets", felec)
        Ploss_dqh[ii, 3] = out.loss.get_loss_group("rotor core", felec)
        Ploss_dqh[ii, 4] = out.loss.get_loss_group("stator winding", felec)

    # Get unique Id, Iq sorted in ascending order
    OP_matrix = self.get_OP_matrix()
    XId, jd = np.unique(OP_matrix[:, 1], return_inverse=True)
    XIq, jq = np.unique(OP_matrix[:, 2], return_inverse=True)
    nd, nq = XId.size, XIq.size

    # Perform 2D interpolation
    if nd * nq == OP_matrix.shape[0]:
        # sort flux linkage matrix and reshape to (nd, nq, 2)
        Ploss_dqh_mat = np.zeros((nd, nq, 5))
        for ii, (m, n) in enumerate(zip(jd, jq)):
            Ploss_dqh_mat[m, n, :] = Ploss_dqh[ii, :]
        # regular grid interpolation
        Ploss_dqh_interp = scp_int.RegularGridInterpolator(
            (XId, XIq), Ploss_dqh_mat, method="linear"
        )
    else:
        # scattered interpolation
        # not working since LinearNDInterpolator is not of same class as RegularGridInterpolator
        Ploss_dqh_interp = scp_int.LinearNDInterpolator(
            (OP_matrix[:, 1], OP_matrix[:, 2]), Ploss_dqh
        )

    return Ploss_dqh_interp
