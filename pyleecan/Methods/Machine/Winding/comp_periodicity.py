from numpy import squeeze, abs as np_abs, mod, where, all as np_all, gcd
from numpy.fft import fft


def comp_periodicity(self, wind_mat=None):
    """Computes the winding matrix (anti-)periodicity

    Parameters
    ----------
    self : Winding
        A Winding object
    wind_mat : ndarray
        Winding connection matrix

    Returns
    -------
    per_a: int
        Number of spatial periods of the winding
    is_aper_a: bool
        True if the winding is anti-periodic over space

    """

    if wind_mat is None:
        wind_mat = self.get_connection_mat()

    assert wind_mat.ndim == 4, "dim 4 expected for wind_mat"

    Zs = wind_mat.shape[2]  # Number of Slot
    qs = wind_mat.shape[3]  # Number of phase

    # Summing on all the layers (Nlay_r and Nlay_theta)
    wind_mat2 = wind_mat
    # Avoid to squeeze qs=1 (WRSM)
    if wind_mat.shape[1] == 1:
        wind_mat2 = squeeze(wind_mat2, 1)
    if wind_mat.shape[0] == 1:
        wind_mat2 = squeeze(wind_mat2, 0)

    if wind_mat2.ndim == 4:  # rad and tan > 2
        Nlay = wind_mat2.shape[0] * wind_mat2.shape[1]
        wind_mat2 = wind_mat2.reshape((Nlay, Zs, qs))
    elif wind_mat2.ndim == 2:
        Nlay = 1
        wind_mat2 = wind_mat2[None, :, :]
    else:
        Nlay = wind_mat2.shape[0]

    Nperw = Zs  # Number of electrical period of the winding
    is_aper = True  # True if winding pattern is anti-periodic

    # Looking for the periodicity of each phase
    for q in range(qs):
        # Looking for the periodicity of each layer
        for l in range(Nlay):
            # FFT of connectivity array for the given layer and phase
            wind_mat_ql_fft = fft(wind_mat2[l, :, q])
            # Find indices of nonzero amplitudes
            I0 = where(np_abs(wind_mat_ql_fft) > 1e-3)[0]
            if len(I0) == 0:  # This phase is not present in this layer
                pass  # No impact on symmetry
            else:
                # Periodicity is given by the non zero lowest order
                Nperw_ql = I0[0] if I0[0] != 0 else I0[1]
                Nperw = gcd(Nperw, Nperw_ql)
                if I0[0] == 0:
                    # Anti-periodicity is necessary false if there is a constant component
                    is_aper = False
                else:
                    # Anti-periodicity is true if all non-zero components are odd multiple of periodicity
                    is_aper = is_aper and np_all(mod(I0 / Nperw_ql, 2) == 1)

            if Nperw == 1 and not is_aper:
                # No need to further continue if there is no anti-periodicity
                break

    # Multiply periodicity number by two in case of anti-periodicity
    Nperw = Nperw * 2 if is_aper else Nperw

    return int(Nperw), bool(is_aper)
