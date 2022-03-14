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

    N0_ref = self.output_list[0].elec.OP.N0

    axes_dict = self.output_list[0].loss.axes_dict

    freqs = axes_dict["freqs"].get_values() * N0 / N0_ref

    Ploss_dqh = np.zeros((len(self.output_list), 5))
    for ii, out in enumerate(self.output_list):
        out_dict = out.simu.loss.comp_losses(out, freqs)
        if out_dict["Pjoule"] is not None:
            Ploss_dqh[ii, 0] = out_dict["Pjoule"]
        if out_dict["Pstator"] is not None:
            Ploss_dqh[ii, 1] = out_dict["Pstator"]
        if out_dict["Pmagnet"] is not None:
            Ploss_dqh[ii, 2] = out_dict["Pmagnet"]
        if out_dict["Protor"] is not None:
            Ploss_dqh[ii, 3] = out_dict["Protor"]
        if out_dict["Pprox"] is not None:
            Ploss_dqh[ii, 4] = out_dict["Pprox"]

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
