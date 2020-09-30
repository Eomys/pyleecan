from numpy import sign


def comp_rot_dir(self):
    """Compute the rotation direction of the winding

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
    MMF = self.comp_mmf_unit(
        Nt=20 * p, Na=20 * p
    )  # 20 points per pole over time and space is enough to capture rotating direction of fundamental mmf

    # Extract fundamental from unit mmf
    results = MMF.get_harmonics(1, "freqs", "wavenumber")

    # Get frequency and wavenumber of fundamental
    f = results["freqs"][0]
    r = results["wavenumber"][0]

    # Rotating direction is the sign of the mechanical speed, i.e frequency over wavenumber
    rot_dir = int(sign(f / r))

    return rot_dir
