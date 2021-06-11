# -*- coding: utf-8 -*-

from numpy import linspace, meshgrid, pi, repeat, sum as np_sum, zeros, mean

from ....Functions.Winding.comp_cond_function import comp_cond_function


def comp_wind_function(self, angle=None, Na=2048, alpha_mmf0=0, per_a=1):
    """Computation of the winding function for the lamination.
    By convention a tooth is centered on the X axis

    Parameters
    ----------
    self : LamSlotMultiWind
        A LamSlotMultiWind object
    angle : ndarray
        Space discretization to compute the winding functions
    Na : int
        Number of angular points for the winding function (not used if angle is set)
    alpha_mmf0 : float
        Angle to shift the winding function (Default value = 0)
    per_a : int
        Spatial periodicity factor

    Returns
    -------
    wf: ndarray
        Winding function Matrix (qs,Na)
    """

    # Space discretization
    if angle is None:
        angle = linspace(0, pi * 2 / per_a, Na, endpoint=False)
    else:
        Na = angle.size

    qs = self.winding.qs  # number of phases
    # Number of point on rad and tan direction
    Nrad, Ntan = self.winding.get_dim_wind()
    Zs = self.get_Zs()  # Number of slot
    Zs0 = int(Zs / per_a)

    slot_angle = self.slot_list[0].comp_angle_active_eq()
    slot_opening = self.slot_list[0].comp_angle_opening()

    wind_mat = self.winding.get_connection_mat(Zs)
    # sum wind_mat along Nlay_rad axis
    wind_mat = np_sum(wind_mat, axis=0)

    # angle of the center of the slots
    # By convention a tooth is centered on the X axis
    alpha_slot = self.alpha[:Zs0]

    # angle of the lay in a slot (Nlay point, end and begin excluded)
    # TODO slot can have different slot_angle
    alpha_lay = linspace(-slot_angle / 2, slot_angle / 2, Ntan + 1, endpoint=False)[1:]

    if alpha_mmf0 != 0:
        angle = (angle - alpha_mmf0) % (2 * pi)

    wf = zeros((qs, Na))
    for n in range(Ntan):
        # [Na, Zs]
        Xalpha_slot, Xangle = meshgrid(alpha_slot + alpha_lay[n], angle)

        Xwind = zeros((1, Zs0, qs))
        Xwind[0, :, :] = wind_mat[n, 0:Zs0, :]
        # Extended winding matrix [Na, Zs, qs]
        Xwind = repeat(Xwind, Na, axis=0)
        # Single winding function in every slot and angle for nth layer [Na, Zs]
        Xwf = -0.5 * comp_cond_function(Xalpha_slot, slot_opening, Xangle)

        for q in range(qs):
            # winding function of qth phase (sum over layers) [qs, Na]
            wf[q, :] += np_sum(Xwind[:, :, q] * Xwf, axis=1)

    if per_a > 1:
        wf = wf - mean(wf, axis=1)[:, None]

    return wf
