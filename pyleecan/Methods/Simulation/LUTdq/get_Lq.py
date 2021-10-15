def get_Lq(self, Id, Iq, L_endwinding=0):
    """Get the total q-axis inductance
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

    Returns
    ----------
    Lq : ndarray
        q-axis inductance
    """

    Lmq = self.get_Lmq(Id=Id, Iq=Iq)

    return Lmq + L_endwinding
