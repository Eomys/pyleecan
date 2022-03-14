from numpy import sum as np_sum, abs as np_abs, pi, matmul, zeros, where


def comp_magnet_losses(self, group, freqs):
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

    if output.mag is None:
        raise Exception("Cannot calculate core losses if OutMag.mesholution is None")

    machine = output.simu.machine

    p = machine.get_pole_pair_number()

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

    # Get magnetic flux density complex amplitude over frequency and for each element center in current group
    Az_val_fft, Se = output.mag.get_fft_from_meshsol(group, label="A_z")

    # Calculate pulsation frequency
    w = 2 * pi * freqs[:, None]

    # Calculate induced currents in magnets
    Jm = -1j * sigma_m * w * Az_val_fft

    # Remove average value to get the sum of circulating current equal to zero
    Jc = 1 / np_sum(Se) * matmul(Jm, Se)
    Jm -= Jc[:, None]

    # Calculate eddy-current loss in magnets
    Pmagnet_density = np_abs(Jm) ** 2 / sigma_m

    # Calculate overall losses
    Pmagnet = Lmag * 2 * p * np_sum(matmul(Pmagnet_density, Se))

    # Check if lambda function exists in coeff_dict
    coeff_dict = output.loss.coeff_dict
    if group not in coeff_dict:
        # Create lambda function to recalculate overall losses function of frequency
        I0 = freqs != 0
        coeff = zeros(w.size)
        coeff[I0] = (
            Lmag * 2 * p * matmul(np_abs(Jm[I0, :] / w[I0, :]) ** 2, Se) / sigma_m
        )
        coeff_dict[group] = {"A": 0, "B": (2 * pi) ** 2 * coeff}
        # coeff_dict[group] = lambda x: np_sum(coeff * (2 * pi * x) ** 2)

    return Pmagnet, Pmagnet_density
