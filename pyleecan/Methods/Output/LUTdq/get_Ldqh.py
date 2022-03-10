def get_Ldqh(self, Id, Iq, L_endwinding=0, Phi_dqh=None):
    """Get the total dqh inductance

    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    Id : float
        current Id
    Iq : float
        current Iq
    L_endwinding : float
        end winding inductance provided by user
    Phi_dqh: ndarray
        Stator winding dqh flux

    Returns
    ----------
    Ldqh : ndarray
        ddqh inductance
    """

    Lmdqh = self.get_Lmdqh(Id=Id, Iq=Iq, Phi_dqh=Phi_dqh)

    return Lmdqh + L_endwinding
