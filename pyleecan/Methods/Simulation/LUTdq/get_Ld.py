def get_Ld(self, Id, Iq, L_endwinding=0):
    """Get the total d-axis inductance
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
    Ld : ndarray
        d-axis inductance
    """

    Lmd = self.get_Lmd(Id=Id, Iq=Iq)

    return Lmd + L_endwinding
