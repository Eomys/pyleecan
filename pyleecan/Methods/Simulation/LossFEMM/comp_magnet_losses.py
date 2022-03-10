from numpy import sum as np_sum, abs as np_abs, pi, matmul


def comp_magnet_losses(self, Az_val_fft, freqs, Se, Lmag, p, sigma_m):
    """Calculate eddy-current losses in rotor permanent magnets assuming power density
    is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pmag = Jm^2/sigma_m with Jm = -sigma_m*1j*2pi*f*Az + Jc where Jc=<Jm> on the magnet surface

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    Az_val_fft: ndarray
        magnetic vector potential complex amplitude over frequency and for each element center in rotor magnets [Wb]
    freqs: ndarray
        frequency vector [Hz]
    Se: ndarray
        Element surface (Nelem,) [m^2]
    sigma_m: float
        electrical conductivity [S/m]
    Lmag: float
        magnet length [m]
    p: int
        pole pair number

    Returns
    -------
    Pmagnet : float
        Overall magnet losses [W]
    Pmagnet_density : ndarray
        Magnet loss density function of element and frequency [W]

    """

    w = 2 * pi * freqs[:, None]

    Jm = -1j * sigma_m * w * Az_val_fft

    Jc = 1 / np_sum(Se) * matmul(Jm, Se)

    Jm -= Jc[:, None]

    Pmagnet_density = np_abs(Jm) ** 2 / sigma_m

    Pmagnet = Lmag * 2 * p * np_sum(matmul(Pmagnet_density, Se))

    return Pmagnet, Pmagnet_density
