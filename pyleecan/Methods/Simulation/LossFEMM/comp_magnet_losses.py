from numpy import sum as np_sum, abs as np_abs, pi, matmul, zeros, where

import numpy as np

from SciDataTool import DataFreq, DataTime
from SciDataTool.Functions.conversions import xy_to_rphi


def comp_magnet_losses(self, group, is_fft=True, type_calc=1):
    """Calculate eddy-current losses in rotor permanent magnets assuming power density
    is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pmag = Jm^2/sigma_m with Jm = -sigma_m*1j*2pi*f*Az + Jc where Jc=<Jm> on the magnet surface

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    group: str
        Name of part in which to calculate magnet losses
    freqs: ndarray
        frequency vector [Hz]

    Returns
    -------
    Pmagnet : float
        Overall magnet losses [W]
    Pmagnet_density : ndarray
        Magnet loss density function of frequency and elements [W/m3]
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
    # Get magnet conductivity
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
    # x = Pe
    # xi = [0.0273, 0.0101]
    # xi = [0.0206, 0.0072]
    # I0 = np.argmin((Pe[:, 0] - xi[0]) ** 2 + (Pe[:, 1] - xi[1]) ** 2)

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

    # output.mag.meshsolution.plot_contour(
    #     "time[3]",
    #     index=3,
    #     group_names=["stator core", "stator winding", "rotor core", "rotor magnets"],
    #     # clim=[1e5, 1e6],
    #     # cmap="jet",
    #     # is_below_above=True,
    # )

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

    if type_calc == 0:
        # Calculate pulsation frequency
        w = 2 * pi * freqs[:, None]
        Smag = np_sum(Se)
        if is_fft:
            Az_df = Az_dt.get_data_along("freqs", "indice", "z[0]")
            Az_fft = Az_df.values[:, :, 0]
            Jm_fft = 1j * sigma_m * w * (-Az_fft + matmul(Az_fft, Se)[:, None] / Smag)

            Jm_df = DataFreq(
                name="Current density",
                symbol="J_m",
                unit="A/m^2",
                values=Jm_fft,
                axes=Az_df.axes,
            )

            Jm_val = Jm_df.get_along("time[smallestperiod]", "indice")["J_m"]

        else:
            dAz_dt = Az_dt.get_along("time=derivate", "indice", "z[0]")["A_z"]
            Jm_val = sigma_m * (-dAz_dt + matmul(dAz_dt, Se)[:, None] / Smag)

            Jm_dt = DataTime(
                name="Current density",
                symbol="J_m",
                unit="A/m^2",
                values=Jm_val,
                axes=Az_dt.axes,
            )

            Jm_dt.plot_2D_Data(
                "time", "indice[0]", data_list=[Jm_df], legend_list=["diff", "fft"]
            )

            Jm_dt.plot_2D_Data(
                "freqs", "indice[0]", data_list=[Jm_df], legend_list=["diff", "fft"]
            )

        # Check integration constant
        # matmul(Jm_val, Se)

        # Calculate eddy-current loss in magnets
        Pmag_density_dt = DataTime(
            name="Loss density",
            symbol="L_m",
            unit="W/m^3",
            values=np_abs(Jm_val) ** 2 / sigma_m,
            axes=Az_dt.axes,
        )

        Pmagnet_density = Pmag_density_dt.get_magnitude_along("freqs", "indice")["L_m"]

        # Calculate overall losses
        Pmagnet = Lmag * per_a * np_sum(matmul(Pmagnet_density, Se))

    else:
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
        Pmagnet = Lmag * per_a * np_sum(matmul(Pmagnet_density, Se))

    # Check if lambda function exists in coeff_dict
    coeff_dict = output.loss.coeff_dict
    if group not in coeff_dict:
        # Calculate coefficients to evaluate magnet losses
        I0 = freqs != 0
        B = zeros(w.size)
        B[I0] = Lmag * per_a * matmul(Pmagnet_density[I0, :] / freqs[I0, None] ** 2, Se)
        coeff_dict[group] = {"A": 0, "B": B}

    return Pmagnet, Pmagnet_density, freqs
