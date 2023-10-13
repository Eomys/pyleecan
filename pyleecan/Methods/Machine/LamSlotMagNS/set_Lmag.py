def set_Lmag(self, value):
    """Set the Length of the magnet

    Parameters
    ----------
    self : LamSlotMagNS
        A LamSlotMagNS object
    value : float
        Value to set [m]
    """

    self.magnet_north.Lmag = value
    self.magnet_south.Lmag = value
