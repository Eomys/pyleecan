def get_Phidqh_mag_harm(self):
    """Get the harmonic magnets flux linkage in DQH frame
    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    Phi_dqh_mag_harm : ndarray
        mean magnets flux linkage in dqh frame (3,)
    """

    Phidqh_mag = self.get_Phidqh_mag()
    Phidqh_mag_freq = Phidqh_mag.time_to_freq()

    # Filter out fondamental
    Phidqh_mag_freq.values[0, :] = 0

    return Phidqh_mag_freq
