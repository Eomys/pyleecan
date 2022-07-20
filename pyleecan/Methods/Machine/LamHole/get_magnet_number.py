def get_magnet_number(self, sym=1):
    """Return the number of magnet on the Lamination

    Parameters
    ----------
    self : LamHole
        A LamHole object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    N_mag : int
        Number of magnets on the lamination
    """

    # Each hole can have several magnets
    nb_mag_per_hole = 0
    for hole in self.get_hole_list():
        nb_mag_per_hole += len(hole.get_magnet_dict())
    # There are Zs / sym holes of each set
    return int(self.get_Zs() / sym * nb_mag_per_hole)
