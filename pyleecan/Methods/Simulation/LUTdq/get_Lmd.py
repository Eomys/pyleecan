def get_Lmd(self):
    """Get the magnets d-axis inductance
    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    Lmd : ndarray
        magnets d-axis inductance
    """

    Phi_d = self.get_Phidqh_mean()[:, 0]
    Phi_mag = self.get_Phidqh_mag_mean()[0]
    Id = self.Idqh[:, 0]

    Lmd = (Phi_d - Phi_mag) / Id

    return Lmd
