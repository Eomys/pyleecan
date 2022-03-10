from numpy import sum as np_sum, abs as np_abs, matmul


def comp_core_losses(self, Bval_fft, freqs, Se, Lst, p, Ce, Ch):
    """Calculate losses in iron core given by group "stator core" or "rotor core"
    assuming power density is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pcore = Ph + Pe = Ch*f*B^2 + Ce*f^2*B^2

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    Bval_fft: ndarray
        magnetic flux density complex amplitude over frequency and for each element center [T]
    freqs: ndarray
        frequency vector [Hz]
    Se: ndarray
        Element surface (Nelem,) [m^2]
    Lst: float
        core stack length [m]
    p: int
        pole pair number
    Ch: float
        hysteresis loss coefficients [W/(m^3*T^2*Hz)]
    Ce: float
        eddy current loss coefficients [W/(m^3*T^2*Hz^2)]

    Returns
    -------
    Pcore : float
        Overall core losses [W]
    Pcore_density : ndarray
        Core losses function of elements and frequency [W]

    """

    # Squared flux density
    Bfft_square = np_abs(Bval_fft) ** 2

    # Eddy-current loss density (or proximity loss density) for each frequency and element
    Pcore_density = Ce * freqs[:, None] ** 2 * Bfft_square

    if Ch != 0:
        # Hysteretic loss density for each frequency and element
        Pcore_density += Ch * freqs[:, None] * Bfft_square

    # Integrate loss density over elements' volume and sum over frequency to get overall loss
    Pcore = Lst * 2 * p * np_sum(matmul(Pcore_density, Se))

    return Pcore, Pcore_density
