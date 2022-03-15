from numpy import sum as np_sum, abs as np_abs, pi, matmul, zeros, where


from SciDataTool import DataFreq, DataTime


def comp_magnet_losses(self, group, freqs, is_fft=True):
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

    # Get magnetic vector potential over time and for each element center in current group
    Az_dt = meshsol.solution[ind].field.get_data_along(
        "time[smallestperiod]", "indice=" + str(Igrp), "z[0]"
    )
    if "antiperiod" in Az_dt.axes[0].symmetries:
        Az_dt.axes[0].symmetries = {"period": Az_dt.axes[0].symmetries["antiperiod"]}

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

    # Check if lambda function exists in coeff_dict
    coeff_dict = output.loss.coeff_dict
    # if group not in coeff_dict:
    #     # Calculate coefficients to evaluate magnet losses
    #     I0 = freqs != 0
    #     coeff = zeros(w.size)
    #     coeff[I0] = (
    #         Lmag * per_a * matmul(np_abs(Jm_val[I0, :] / w[I0, :]) ** 2, Se) / sigma_m
    #     )
    #     coeff_dict[group] = {"A": 0, "B": (2 * pi) ** 2 * coeff}

    return Pmagnet, Pmagnet_density
