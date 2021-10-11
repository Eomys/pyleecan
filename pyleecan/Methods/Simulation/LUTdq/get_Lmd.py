def get_Lmd(self, Id, Iq):
    """Get the magnets d-axis inductance
    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    Id : float
        current Id
    Iq : float
        current Iq

    Returns
    ----------
    Lmd : ndarray
        magnets d-axis inductance
    """

    Phi_d = self.interp_Phi_dqh(Id=Id, Iq=Iq)[0]
    Phi_mag = self.get_Phidqh_mag_mean()[0]

    Lmd = (Phi_d - Phi_mag) / Id

    return Lmd
