def get_connection_mat(self, Zs=None, p=None):
    """Get the Winding Matrix

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)
    p : int
        Number of pole pairs (Integer >0)

    Returns
    -------
    wind_mat: numpy.ndarray
        Winding Matrix (1, 1, Zs, qs)


    """

    if self.wind_mat is None:
        self.wind_mat = self.comp_connection_mat(Zs=Zs, p=p)

    return self.wind_mat
