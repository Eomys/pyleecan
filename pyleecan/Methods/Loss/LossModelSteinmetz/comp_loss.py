from numpy import abs as np_abs
from numpy import matmul
from numpy import sqrt as np_sqrt
from numpy import sum as np_sum


def comp_loss(self):
    """Calculate loss density in iron core given by group "stator core" or "rotor core"
    assuming power density is given by a Steinmetz model:

        Pcore = Ph + Pe = k_hy * f^alpha_f * B^self.alpha_B + k_ed * f^2 * B^2

    Parameters
    ----------
    self: LossModelSteinmetz
        a LossModelSteinmetz object

    Returns
    -------
    Pcore_density : ndarray
        Core loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    """

    if self.parent.parent.parent is None:
        raise Exception("Cannot calculate core losses if simu is not in an Output")
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
        self.alpha_f,
        self.alpha_B,
    ]:
        material = lamination.mat_type
        self.comp_coeff(material)

    # Get loss coefficients
    # The loss data are given in W/kg, but the loss density in pyleecan are computed in W/m^3
    k_hy = self.k_hy / Kf * rho
    k_ed = self.k_ed / Kf * rho
    alpha_f = self.alpha_f
    alpha_B = self.alpha_B

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

    # Extract solution
    try:
        solution_B = meshsol["B"]
    except ValueError:
        raise ValueError("Cannot calculate core losses if B is not in meshsolution")

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

    # Compute magnetic flux density FFT
    Bfft = Bvect.get_xyz_along("freqs", "indice=" + str(Igrp), "z=mean")
    freqs = Bfft["freqs"]
    Bfft_magnitude = np_sqrt(np_abs(Bfft["comp_x"]) ** 2 + np_abs(Bfft["comp_y"]) ** 2)

    # Compute the loss density for each element and each frequency
    Pcore_density = k_ed * freqs[:, None] ** 2 * Bfft_magnitude ** 2
    Pcore_density += k_hy * freqs[:, None] ** alpha_f * Bfft_magnitude ** alpha_B

    if is_change_Time:
        # Change periodicity back to original periodicity
        for comp in Bvect.components.values():
            comp.axes[0] = Time_orig

    # Get frequency orders
    n = freqs / felec

    # Integrate loss density over group volume to get polynomial coefficients
    coeff = Lst * per_a * matmul(Bfft_magnitude ** 2, Se)
    A = np_sum(k_ed * coeff * n ** 2)
    coeff = Lst * per_a * matmul(Bfft_magnitude ** alpha_B, Se)
    B = np_sum(k_hy * coeff * n ** alpha_f)
    self.coeff_dict = {"2": A, str(alpha_f): B}

    return Pcore_density, freqs
