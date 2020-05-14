# -*- coding: utf-8 -*-

from numpy import linspace, meshgrid, pi, repeat, sum as np_sum, zeros
from ....Functions.Winding.comp_cond_function import comp_cond_function


def comp_wind_function(self, Na=2048, alpha_mmf0=0):
    """Computation of the winding function for the lamination.
    By default, there is a slot at alpha_rad = 0

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    Na : int
        Number of angular points for the winding function
    alpha_mmf0 : float
        Angle to shift the winding function (Default value = 0)

    Returns
    -------
    wf: ndarray
        Winding function Matrix (qs,Na)
    """

    qs = self.winding.qs  # number of phases
    # Number of point on rad and tan direction
    Nrad, Ntan = self.winding.get_dim_wind()
    Zs = self.slot.Zs  # Number of slot

    slot_angle = self.slot.comp_angle_wind_eq()

    wind_mat = self.winding.comp_connection_mat(Zs)
    # sum wind_mat along Nlay_rad axis
    wind_mat = np_sum(wind_mat, axis=0)

    # angle of the center of the slots
    alpha_slot = linspace(0, 2 * pi, Zs, endpoint=False)

    # angle of the lay in a slot (Nlay point, end and begin excluded)
    alpha_lay = linspace(-slot_angle / 2, slot_angle / 2, Ntan + 1, endpoint=False)[1:]

    alpha_rad = linspace(0, pi * 2, Na, endpoint=False)

    if alpha_mmf0 != 0:
        alpha_rad = (alpha_rad - alpha_mmf0) % (2 * pi)

    wf = zeros((qs, Na))
    for n in range(Ntan):
        # [Na, Zs]
        Xalpha_slot, Xalpha_rad = meshgrid(alpha_slot + alpha_lay[n], alpha_rad)

        Xwind = zeros((1, Zs, qs))
        Xwind[0, :, :] = wind_mat[n, :, :]
        # Extended winding matrix [Na, Zs, qs]
        Xwind = repeat(Xwind, Na, axis=0)
        # Single winding function in every slot and angle for nth layer [Na, Zs]
        Xwf = -0.5 * comp_cond_function(Xalpha_slot, slot_angle, Xalpha_rad)

        for q in range(qs):
            # winding function of qth phase (sum over layers) [qs, Na]
            wf[q, :] += np_sum(Xwind[:, :, q] * Xwf, axis=1)

    return wf
