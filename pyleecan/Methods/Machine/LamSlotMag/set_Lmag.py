def set_Lmag(self, value):
    """Set the Length of the magnet

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object
    value : float
        Value to set [m]
    """

    self.magnet.Lmag = value
