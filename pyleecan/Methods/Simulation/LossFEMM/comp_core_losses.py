from numpy import sum as np_sum, matmul, abs as np_abs, zeros, argmin

from SciDataTool import DataTime


def comp_core_losses(self, group, Ce=None, Ch=None, type_calc=1):
    """Calculate losses in iron core given by group "stator core" or "rotor core"
    assuming power density is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pcore = Ph + Pe = Ch*f*B^2 + Ce*f^2*B^2

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    group: str
        Name of part in which to calculate core losses
    freqs: ndarray
        frequency vector [Hz]
    Ch: float
        hysteresis loss coefficients [W/(m^3*T^2*Hz)]
    Ce: float
        eddy current loss coefficients [W/(m^3*T^2*Hz^2)]

    Returns
    -------
    Pcore : float
        Overall core losses [W]
    Pcore_density : ndarray
        Core loss density function of frequency and elements [W/m3]
    """

    if self.parent.parent is None:
        raise Exception("Cannot calculate core losses if simu is not in an Output")
    else:
        output = self.parent.parent

    machine = output.simu.machine

    per_a = output.geo.per_a
    if output.geo.is_antiper_a:
        per_a *= 2

    if "stator" in group:
        Lst = machine.stator.L1
    else:
        Lst = machine.rotor.L1

    if output.mag is None:
        raise Exception("Cannot calculate core losses if OutMag is None")

    if output.mag.meshsolution is None:
        raise Exception("Cannot calculate core losses if OutMag.meshsolution is None")
    else:
        meshsol = output.mag.meshsolution

    group_list = list(meshsol.group.keys())

    if group not in group_list:
        raise Exception("Cannot calculate core losses for group=" + group)

    label_list = [sol.label for sol in meshsol.solution]

    if "B" not in label_list:
        raise Exception("Cannot calculate core losses if B is not in meshsolution")
    else:
        ind = label_list.index("B")

    # Get element indices associated to group
    Igrp = meshsol.group[group]

    # Get element surface associated to group
    Se = meshsol.mesh[0].get_cell_area()[Igrp]

    # cell = meshsol.mesh[0].cell["triangle"].connectivity

    # nodes_coord = meshsol.mesh[0].node.coordinate

    # center_coord = np.zeros((cell.shape[0], cell.shape[1], 2))

    # center_coord[:, :, 0] = nodes_coord[cell, 0]
    # center_coord[:, :, 1] = nodes_coord[cell, 1]

    # center_coord = np.mean(center_coord, axis=1)
    # x = center_coord
    # xi = [0.0273, 0.0101]
    # xi = [0.0219, 0.0079]
    # I0 = np.argmin((x[:, 0] - xi[0]) ** 2 + (x[:, 1] - xi[1]) ** 2)

    # center_coord[I0, :]

    Bvect = meshsol.solution[ind].field
    axes_list = Bvect.get_axes()
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
        for comp in Bvect.components.values():
            comp.axes[0] = Time

    if type_calc == 0:
        # Get magnetic flux density complex amplitude over frequency and for each element center in current group
        Bx = Bvect.components["comp_x"].values[:, Igrp, :]
        By = Bvect.components["comp_y"].values[:, Igrp, :]
        Bsquare = Bx ** 2 + By ** 2

        # B = np.sqrt(Bsquare)

        # B0 = np.sqrt(Bsquare[0, :, 0])

        # Put Bsquare in DataTime to take FFT over time
        Indice = axes_list[1].copy()
        Indice.values = axes_list[1].values[Igrp]
        Bsquare_dt = DataTime(
            name=group + " flux density magnitude",
            symbol="B",
            unit="T",
            axes=[Time, Indice, axes_list[2]],
            values=Bsquare,
        )
        Bfft_square = Bsquare_dt.get_magnitude_along("freqs", "indice", "z[0]")["B"]
    else:

        Bfft = Bvect.get_xyz_along("freqs", "indice=" + str(Igrp), "z[0]")
        freqs = Bfft["freqs"]
        # Bfft_x = Bfft["comp_x"]
        # Bfft_y = Bfft["comp_y"]

        # Imax = np.argmax(Bfft_x[8, :])

        Bfft_square = np_abs(Bfft["comp_x"]) ** 2 + np_abs(Bfft["comp_y"]) ** 2

    # Eddy-current loss density (or proximity loss density) for each frequency and element
    Pcore_density = Ce * freqs[:, None] ** 2 * Bfft_square

    if Ch != 0:
        # Hysteretic loss density for each frequency and element
        Pcore_density += Ch * freqs[:, None] * Bfft_square

    # Integrate loss density over elements' volume and sum over frequency to get overall loss
    Pcore = Lst * per_a * np_sum(matmul(Pcore_density, Se))

    if is_change_Time:
        # Change periodicity back to original periodicity
        for comp in Bvect.components.values():
            comp.axes[0] = Time_orig

    # Check if coefficients exists in coeff_dict
    coeff_dict = output.loss.coeff_dict
    if group not in coeff_dict:
        # Calculate coefficients to evaluate core losses
        coeff = matmul(Bfft_square, Se)
        if Ch == 0:
            A = 0
        else:
            A = Lst * per_a * Ch * coeff
        B = Lst * per_a * Ce * coeff
        coeff_dict[group] = {"A": A, "B": B}

    return Pcore, Pcore_density, freqs
