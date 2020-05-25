from numpy import take, sign, argmax, cos, abs as np_abs, angle as np_angle


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

    MMF = self.comp_mmf_unit()
    p = self.get_pole_pair_number()

    # Compute rotation direction from unit mmf
    H1 = MMF.get_harmonics(1, "freqs", "wavenumber")

    return sign(H1[2][0])
