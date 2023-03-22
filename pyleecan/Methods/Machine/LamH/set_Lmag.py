def set_Lmag(self, value):
    """Set the Length of the magnet

    Parameters
    ----------
    self : LamH
        A LamH object
    value : float
        Value to set [m]
    """

    for hole in self.get_hole_list():
        mag_dict = hole.get_magnet_dict()
        for mag in mag_dict.values():
            mag.Lmag = value
