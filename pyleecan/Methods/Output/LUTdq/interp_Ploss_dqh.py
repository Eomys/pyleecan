import numpy as np
import scipy.interpolate as scp_int

from ....Functions.Electrical.comp_loss_joule import comp_loss_joule


def interp_Ploss_dqh(self, Id, Iq, N0):
    """Interpolate losses in function of Id and Iq and for given speed

    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    Id : float or ndarray
        current Id
    Iq : float or ndarray
        current Iq
    N0: float
        rotation speed [rpm]

    Returns
    ----------
    Ploss_dqh : float or ndarray
        interpolated losses function of dq currents (N_OP, 5)
        - 1st column : Joule losses
        - 2nd column : stator core losses
        - 3rd column : magnet losses
        - 4th column : rotor core losses
        - 5th column : proximity losses
    """

    p = self.simu.machine.get_pole_pair_number()

    felec = N0 / 60 * p

    type_skin_effect = self.simu.loss.type_skin_effect
    Tsta = self.simu.loss.Tsta

    Ploss_dqh = np.zeros((len(self.output_list), 5))
    for ii, out in enumerate(self.output_list):
        OP = out.elec.OP.copy()
        OP.felec = felec
        Ploss_dqh[ii, 0] = comp_loss_joule(
            lam=self.simu.machine.stator,
            OP=OP,
            T_op=Tsta,
            type_skin_effect=type_skin_effect,
        )
        Ploss_dqh[ii, 1] = out.loss.get_loss_group("stator core", felec)
        Ploss_dqh[ii, 2] = out.loss.get_loss_group("rotor magnets", felec)
        Ploss_dqh[ii, 3] = out.loss.get_loss_group("rotor core", felec)
        Ploss_dqh[ii, 4] = out.loss.get_loss_group("stator winding", felec)

    # Get unique Id, Iq sorted in ascending order
    OP_matrix = self.get_OP_array("N0", "Id", "Iq")
    XId, jd = np.unique(OP_matrix[:, 1], return_inverse=True)
    XIq, jq = np.unique(OP_matrix[:, 2], return_inverse=True)
    nd, nq = XId.size, XIq.size

    Ploss_dqh_mat = np.zeros((nd, nq, 5))
    # Perform 2D interpolation
    if nd * nq == OP_matrix.shape[0]:
        # sort flux linkage matrix and reshape to (nd, nq, 2)
        is_rect_interp = True
        for ii, (m, n) in enumerate(zip(jd, jq)):
            Ploss_dqh_mat[m, n, :] = Ploss_dqh[ii, :]
    elif nd + nq - 1 == OP_matrix.shape[0]:
        # Rebuild 2D grid from xId and xIq
        is_rect_interp = True
        # Find Id=Iq=0
        i0 = self.get_index_open_circuit()
        Ploss_dqh_mag = Ploss_dqh[i0, :]
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
                    Ploss_dqh_mat[m, n, :] = Ploss_dqh[kk, :]
                else:
                    # Sum flux values for (Id, Iq): Phi_dq(Id, Iq) = Phi_dq(Id, 0) + Phi_dq(0, Iq)
                    Ploss_dqh_mat[m, n, :] = (
                        Ploss_dqh[ii, :] + Ploss_dqh[jj, :] - Ploss_dqh_mag
                    )

    else:
        is_rect_interp = False

    if nd == 1:
        # 1D interpolation along q axis
        Ploss_dqh_interp = scp_int.interp1d(XIq, Ploss_dqh_mat, kind="linear", axis=1)
    elif nq == 1:
        # 1D interpolation along d axis
        Ploss_dqh_interp = scp_int.interp1d(XId, Ploss_dqh_mat, kind="linear", axis=0)
    elif is_rect_interp:
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

    # Interpolate losses function of dq currents
    if nd == 1:
        Ploss_dqh = np.squeeze(Ploss_dqh_interp(Iq))
    elif nq == 1:
        Ploss_dqh = np.squeeze(Ploss_dqh_interp(Id))
    else:
        if np.isscalar(Id) and np.isscalar(Iq):
            Ploss_dqh = Ploss_dqh_interp((Id, Iq))[:, None]
        else:
            Ploss_dqh = Ploss_dqh_interp((Id, Iq))

    return Ploss_dqh
