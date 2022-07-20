def get_magnet_number(self, sym=1):
    """Return the number of magnet on the Lamination

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    N_mag : int
        Number of magnets on the lamination
    """

    p = self.get_pole_pair_number()
    return int(2 * p / sym)
