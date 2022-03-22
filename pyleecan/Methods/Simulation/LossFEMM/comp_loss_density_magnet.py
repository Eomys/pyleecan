from numpy import sum as np_sum, abs as np_abs, pi, matmul, zeros

import numpy as np

from SciDataTool.Functions.conversions import xy_to_rphi


def comp_loss_density_magnet(self, group, coeff_dict):
    """Calculate eddy-current losses in rotor permanent magnets assuming power density
    is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pmag = Jm^2/sigma_m with Jm = -sigma_m*1j*2pi*f*Az + Jc where Jc=<Jm> on the magnet surface

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    group: str
        Name of part in which to calculate magnet losses

    Returns
    -------
    Pmagnet_density : ndarray
        Magnet loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    coeff_dict: dict
        Dict containing coefficient A and B to calculate overall losses such as P = sum(A*f + B*f^2)
    """

    if self.parent.parent is None:
        raise Exception("Cannot calculate core losses if simu is not in an Output")
    else:
        output = self.parent.parent

    machine = output.simu.machine

    p = machine.get_pole_pair_number()

    per_a = output.geo.per_a
    if output.geo.is_antiper_a:
        per_a *= 2

    if hasattr(machine.rotor, "magnet"):
        magnet = machine.rotor.magnet
    else:
        hole = machine.rotor.hole[0]
        if hasattr(hole, "magnet_0"):
            magnet = hole.magnet_0

    # Get magnet length
    Lmag = magnet.Lmag
    if Lmag is None:
        Lmag = machine.rotor.L1

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    # Get magnet conductivity including skin effect
    sigma_m = magnet.mat_type.elec.get_conductivity(T_op=self.Trot)

    if output.mag is None:
        raise Exception("Cannot calculate magnet losses if OutMag is None")

    if output.mag.meshsolution is None:
        raise Exception("Cannot calculate magnet losses if OutMag.meshsolution is None")
    else:
        meshsol = output.mag.meshsolution

    group_list = list(meshsol.group.keys())

    if group not in group_list:
        raise Exception("Cannot calculate magnet losses for group=" + group)

    label_list = [sol.label for sol in meshsol.solution]

    if "A_z" not in label_list:
        raise Exception("Cannot calculate magnet losses if A_z is not in meshsolution")
    else:
        ind = label_list.index("A_z") + 1

    # Get element indices associated to group
    Igrp = meshsol.group[group]

    # Get element surface associated to group
    Se = meshsol.mesh[0].get_cell_area()[Igrp]

    cell = meshsol.mesh[0].cell["triangle"].connectivity

    nodes_coord = meshsol.mesh[0].node.coordinate

    Pe = np.zeros((cell.shape[0], cell.shape[1], 2))

    Pe[:, :, 0] = nodes_coord[cell, 0]
    Pe[:, :, 1] = nodes_coord[cell, 1]

    Pe = np.mean(Pe, axis=1)

    r, phi = xy_to_rphi(Pe[Igrp, 0], Pe[Igrp, 1])

    theta_mag = np.arange(0, 2 * pi / per_a, pi / p) + pi / p

    list_Imag = list()
    for ii, t in enumerate(theta_mag):
        if ii == 0:
            t0 = 0
        else:
            t0 = theta_mag[ii - 1]
        list_Imag.append(np.where(np.logical_and(t0 <= phi, phi <= t))[0])

    # Get magnetic vector potential over time and for each element center in current group
    Az_dt = meshsol.solution[ind].field
    axes_list = Az_dt.get_axes()
    Time_orig = axes_list[0]
    Time = Time_orig.copy()

    # Check Time axis periodicity in function of group
    is_change_Time = False
    if "rotor" in group:
        if "antiperiod" in Time_orig.symmetries:
            Time.symmetries = {"period": Time_orig.symmetries["antiperiod"]}
            is_change_Time = True
    elif "stator" in group:
        if "period" in Time_orig.symmetries:
            Time.symmetries = {"antiperiod": Time_orig.symmetries["period"]}
            is_change_Time = True
    if is_change_Time:
        Az_dt.axes[0] = Time

    Igrp = np.array(Igrp)
    for ii, kmag in enumerate(list_Imag):
        Se_mag = Se[kmag]
        Az_df = Az_dt.get_magnitude_along(
            "freqs", "indice" + str(Igrp[kmag].tolist()), "z[0]"
        )
        if ii == 0:
            freqs = Az_df["freqs"]
            w = 2 * pi * freqs[:, None]
            Pmagnet_density = np.zeros((w.size, Se.size))
        Az_fft = Az_df["A_z"]
        Az_mean = matmul(Az_fft, Se_mag)[:, None] / np_sum(Se_mag)
        Jm_fft = -1j * sigma_m * w * (Az_fft - Az_mean)
        Pmagnet_density[:, kmag] = np_abs(Jm_fft) ** 2 / sigma_m

    # Calculate coefficients to evaluate magnet losses
    if coeff_dict is not None:
        # Get frequency orders
        n = freqs / felec
        # Integrate loss density over group volume
        I0 = n != 0
        Af = zeros(w.size)
        Af[I0] = (
            Lmag * per_a * matmul(Pmagnet_density[I0, :] / freqs[I0, None] ** 2, Se)
        )
        # Sum over orders
        A = np_sum(Af * n ** 2)
        coeff_dict[group] = {"A": A, "B": 0, "C": 0}

    return Pmagnet_density, freqs
