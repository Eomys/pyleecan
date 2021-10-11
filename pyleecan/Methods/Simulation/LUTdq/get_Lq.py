def get_Lq(self, L_endwinding):
    """Get the total q-axis inductance
    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    L_endwinding : float
        end winding inductance provided by user

    Returns
    ----------
    Lq : ndarray
        q-axis inductance
    """

    Lmq = self.get_Lmq()

    return Lmq + L_endwinding
