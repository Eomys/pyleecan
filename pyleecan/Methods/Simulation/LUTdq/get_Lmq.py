def get_Lmq(self):
    """Get the magnets q-axis inductance
    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    Lmq : ndarray
        magnets q-axis inductance
    """

    Phi_q = self.get_Phidqh_mean()[:, 1]
    Phi_mag = self.get_Phidqh_mag_mean()[1]
    Iq = self.Idqh[:, 1]

    Lmq = (Phi_q - Phi_mag) / Iq

    return Lmq
