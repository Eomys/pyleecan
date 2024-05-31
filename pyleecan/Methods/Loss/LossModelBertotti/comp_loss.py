from numpy import abs as np_abs
from numpy import matmul
from numpy import sqrt as np_sqrt
from numpy import sum as np_sum


def comp_loss(self):
    """Calculate loss density in iron core given by group "stator core" or "rotor core"
    assuming power density is given by a Bertotti model

        Pcore = k_hy * f * B^2 + k_ed * (f B)^2 + k_ex * (f B)^1.5

    Parameters
    ----------
    self: LossModelBertotti
        a LossModelBertotti object

    Returns
    -------
    Pcore_density : ndarray
        Core loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    """

    if self.parent.parent.parent is None:
        raise ValueError("Cannot calculate core losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    machine = output.simu.machine

    per_a = output.geo.per_a
    if output.geo.is_antiper_a:
        per_a *= 2

    lamination = machine.stator if "stator" in self.group else machine.rotor
    Lst = lamination.L1
    # Taking into account the stacking factor
    Kf = lamination.Kf1
    rho = lamination.mat_type.struct.rho

    # Compute the coefficients only if at least one is not provided
    if None in [
        self.k_hy,
        self.k_ed,
        self.k_ex,
    ]:
        material = lamination.mat_type
        self.comp_coeff(material)

    # Get loss coefficients
    # The loss data are given in W/kg, but the loss density in pyleecan are computed in W/m^3
    k_hy = self.k_hy / Kf * rho
    k_ed = self.k_ed / Kf * rho
    k_ex = self.k_ex / Kf * rho

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    if output.mag is None:
        raise ValueError("Cannot calculate core losses if OutMag is None")

    if output.mag.meshsolution is None:
        raise ValueError("Cannot calculate core losses if OutMag.meshsolution is None")
    else:
        meshsol = output.mag.meshsolution

    group_list = list(meshsol.group.keys())

    if self.group not in group_list:
        raise ValueError("Cannot calculate core losses for group=" + self.group)

    try:
        solution_B = meshsol["B"]
    except KeyError:
        raise KeyError("Cannot calculate core losses if B is not in meshsolution")

    # Get element indices associated to group
    Igrp = meshsol.group[self.group]

    # Get element surface associated to group
    Se = meshsol.mesh.get_element_area()[Igrp]

    Bvect = solution_B.field
    axes_list = Bvect.get_axes()
    Time_orig = axes_list[0]
    Time = Time_orig.copy()

    # Check Time axis periodicity in function of group
    is_change_Time = False
    if "rotor" in self.group:
        if "antiperiod" in Time_orig.symmetries:
            Time.symmetries = {"period": Time_orig.symmetries["antiperiod"]}
            is_change_Time = True
    if is_change_Time:
        for comp in Bvect.components.values():
            comp.axes[0] = Time

    # # Plot 2D to check periodicity
    # # ii = Igrp[0]
    # ii = 1560
    # Bvect.components["comp_x"].plot_2D_Data(
    #     "time",
    #     "indice[" + str(ii) + "]",
    #     data_list=[Bvect.components["comp_y"]],
    #     legend_list=["Bx", "By"],
    # )

    # Bvect.components["comp_x"].plot_2D_Data(
    #     "freqs",
    #     "indice[" + str(ii) + "]",
    #     data_list=[Bvect.components["comp_y"]],
    #     legend_list=["Bx", "By"],
    # )

    # Compute magnetic flux density FFT
    Bfft = Bvect.get_xyz_along("freqs", "indice=" + str(Igrp), "z=mean")
    freqs = Bfft["freqs"]
    Bfft_magnitude = np_sqrt(np_abs(Bfft["comp_x"]) ** 2 + np_abs(Bfft["comp_y"]) ** 2)

    # Compute the loss density for each element and each frequency
    Pcore_density = k_ed * (freqs[:, None] * Bfft_magnitude) ** 2
    Pcore_density += k_hy * freqs[:, None] * Bfft_magnitude**2
    Pcore_density += k_ex * (freqs[:, None] * Bfft_magnitude) ** 1.5

    if is_change_Time:
        # Change periodicity back to original periodicity
        for comp in Bvect.components.values():
            comp.axes[0] = Time_orig

    # Get frequency orders
    n = freqs / felec

    # Integrate loss density over group volume to get polynomial coefficients
    coeff = Lst * per_a * matmul(Bfft_magnitude**2, Se)
    # Get polynomial coefficient
    B = np_sum(k_ed * coeff * n**2)

    coeff = Lst * per_a * matmul(Bfft_magnitude**1.5, Se)
    # Get polynomial coefficient
    C = np_sum(k_ex * coeff * n**1.5)

    coeff = Lst * per_a * matmul(Bfft_magnitude**2, Se)
    # Get polynomial coefficient
    A = np_sum(k_hy * coeff * n)

    self.coeff_dict = {"1": A, "2": B, "1.5": C}

    return Pcore_density, freqs
