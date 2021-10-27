from numpy import sign


def comp_mmf_dir(self, felec=1, current_dir=1, is_plot=False):
    """Compute the rotation direction of the fundamental magnetomotive force induced by the winding

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    felec : float
        Stator current frequency to consider
    current_dir: int
        Stator current rotation direction +/-1
    is_plot: bool
        True to plot fft2 of stator MMF

    Returns
    -------
    mmf_dir : int
        -1 or +1
    """
    p = self.get_pole_pair_number()

    # Compute unit mmf
    # 20 points per pole over time and space is enough to capture rotating direction of fundamental mmf
    MMF, _ = self.comp_mmf_unit(
        Nt=20 * p, Na=20 * p, felec=felec, current_dir=current_dir
    )

    # Extract fundamental from unit mmf
    result_p = MMF.get_harmonics(1, "freqs>0", "wavenumber=" + str(p))
    result_n = MMF.get_harmonics(1, "freqs>0", "wavenumber=" + str(-p))

    if result_p[MMF.symbol][0] > result_n[MMF.symbol][0]:
        result = result_p
    else:
        result = result_n

    # Get frequency and wavenumber of fundamental
    f = result["freqs"][0]
    r = result["wavenumber"][0]

    # Rotating direction is the sign of the mechanical speed of the magnetomotive force fundamental,
    # i.e frequency over wavenumber
    mmf_dir = int(sign(f / r))

    if is_plot:
        MMF.plot_3D_Data("freqs", "wavenumber")

    return mmf_dir
