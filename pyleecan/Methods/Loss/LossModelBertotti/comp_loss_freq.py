import numpy as np

from ....Functions.labels import ROTOR_LAB, STATOR_LAB


def comp_loss_freq(self):
    """Calculate loss density in iron core given by group "stator core" or "rotor core"
    assuming power density is given by a Bertotti model depending on frequency:

        Pcore = k_hy * f * B^(alpha_B) + k_ed * (f B)^2 + k_ex * (f B)^1.5

    Parameters
    ----------
    self: LossModelBertotti
        a LossModelBertotti object

    Returns
    -------
    Pcore_density : ndarray
        Average core loss density (frequency=0Hz) for all elements [W/m3]
    Pcore_dict: {ndarray}
        Dict containing the array of core losses by contribution and for all frequencies in magnetic flux density [W]
    freqs: ndarray
        frequency vector of magnetic flux density harmonics [Hz]
    """

    if self.parent.parent.parent is None:
        raise ValueError("Cannot calculate core losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    machine = output.simu.machine

    lamination = machine.stator if "stator" in self.group else machine.rotor
    Lst = lamination.L1
    # Taking into account the stacking factor
    if self.is_stacking_factor:
        Kf = lamination.Kf1
    else:
        Kf = 1
    rho = lamination.mat_type.struct.rho

    # Compute the coefficients only if at least one is not provided (the others being enforced by Loss.run())
    if None in [self.k_hy, self.k_ed, self.k_ex, self.alpha_B]:
        material = lamination.mat_type
        self.comp_coeff(material)

    # Get loss coefficients
    # The loss data are given in W/kg, but the loss density in pyleecan are computed in W/m^3
    k_hy = self.k_hy * rho
    k_ed = self.k_ed * rho
    k_ex = self.k_ex * rho
    alpha_B = self.alpha_B

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    if output.mag is None:
        raise ValueError("Cannot calculate core losses if OutMag is None")

    if output.mag.meshsolution is not None:
        # Case with same time periodicities in both stator and rotor frames
        meshsol = output.mag.meshsolution

    elif output.mag.meshsolution_dict is None:
        raise ValueError(
            "Cannot calculate core losses if OutMag.meshsolution and OutMag.meshsolution_dict are both None"
        )
    else:
        # No need to mirror mesh data, fetching the meshsolution matching with the lamination of interest
        if "stator" in self.group:
            meshsol = output.mag.meshsolution_dict[STATOR_LAB + "-0"]
        else:
            meshsol = output.mag.meshsolution_dict[ROTOR_LAB + "-0"]

    group_list = list(meshsol.group.keys())

    if self.group not in group_list:
        raise ValueError("Cannot calculate core losses for group=" + self.group)

    if "B" in meshsol:
        Bvect = meshsol["B"].field
    else:
        raise ValueError("Cannot calculate core losses if B is not in meshsolution")

    # Get mesh spatial symmetries (including (anti)-periodicities)
    per_a = meshsol.mesh.sym

    # Get element indices associated to group
    Igrp = meshsol.group[self.group]

    # Get element surface associated to group
    Se = meshsol.mesh.get_element_area()[Igrp]

    # Compute magnetic flux density FFT
    Bfft = Bvect.get_xyz_along("freqs", "indice=" + str(Igrp), "z=mean")
    freqs = Bfft["freqs"]
    Bfft_square = np.abs(Bfft["comp_x"]) ** 2 + np.abs(Bfft["comp_y"]) ** 2

    # Compute the loss density for each element and each frequency
    Pcore_density_hys = k_hy / Kf * freqs[:, None] * Bfft_square ** (alpha_B / 2)
    Pcore_density_edd = k_ed / Kf * freqs[:, None] ** 2 * Bfft_square
    Pcore_density_exc = k_ex / Kf * freqs[:, None] ** 1.5 * Bfft_square**0.75

    # Sum all core losses contribution and sum over frequencies to get average loss density value per element
    Pcore_density = np.sum(
        Pcore_density_hys + Pcore_density_edd + Pcore_density_exc, axis=0, keepdims=True
    )

    # Integrate volumic density over core volume to get loss value per contribution
    Pcore_hys = Lst * per_a * np.matmul(Pcore_density_hys, Se)
    Pcore_edd = Lst * per_a * np.matmul(Pcore_density_edd, Se)
    Pcore_exc = Lst * per_a * np.matmul(Pcore_density_exc, Se)

    # Sum all core losses contributions
    Pcore = Pcore_hys + Pcore_edd + Pcore_exc

    # Store losses contribution for each frequency in dict
    Pcore_dict = {
        self.group + " losses": Pcore,
        self.group + " hysteresis": Pcore_hys,
        self.group + " eddy current": Pcore_edd,
        self.group + " excess": Pcore_exc,
    }

    # Get hysteresis loss polynomial coefficient
    A = np.sum(Pcore_hys) / felec

    # Get eddy-current loss polynomial coefficient
    B = np.sum(Pcore_edd) / felec**2

    # Get excess loss polynomial coefficient
    C = np.sum(Pcore_exc) / felec**1.5

    # Store polynom coefficients in dict
    self.coeff_dict = {"1.0": A, "2.0": B, "1.5": C}

    return Pcore_density, Pcore_dict, freqs
