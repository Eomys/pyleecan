def get_Ld(self, L_endwinding):
    """Get the total d-axis inductance
    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    L_endwinding : float
        end winding inductance provided by user

    Returns
    ----------
    Ld : ndarray
        d-axis inductance
    """

    Lmd = self.get_Lmd()

    return Lmd + L_endwinding
