from numpy import sign


def comp_rot_dir(self, N0=1000, felec=1):
    """Compute the rotation direction of the fundamental magnetic field induced by the winding
    WARNING: rot_dir = -1 to have positive rotor rotating direction, i.e. rotor position moves towards positive angle

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    rot_dir : int
        -1 or +1
    """
    p = self.get_pole_pair_number()

    # Compute unit mmf
    # 20 points per pole over time and space is enough to capture rotating direction of fundamental mmf
    MMF, _ = self.comp_mmf_unit(Nt=20 * p, Na=20 * p, felec=felec, N0=N0)

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

    # Rotating direction is the sign of the mechanical speed of the magnetic field fundamental, i.e frequency over wavenumber
    rot_dir = int(sign(f / r))

    return rot_dir
