def get_Lmq(self, Id, Iq):
    """Get the magnets q-axis inductance
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
    Lmq : ndarray
        magnets q-axis inductance
    """

    Phi_q = self.interp_Phi_dqh(Id=Id, Iq=Iq)[1]
    Phi_mag = self.get_Phidqh_mag_mean()[1]

    Lmq = (Phi_q - Phi_mag) / Iq

    return Lmq
